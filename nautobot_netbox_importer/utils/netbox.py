"""Utility functions for working with Netbox."""
import json
import os
import requests
import urllib3
import pynetbox


class ApiEndpoint:  # pylint: disable=too-few-public-methods
    """Base class to represent interactions with an API endpoint."""

    class Meta:
        """Meta data for ApiEndpoint class."""

        abstract = True

    def __init__(self, base_url: str, verify: bool = True):
        """Create API connection."""
        self.base_url = base_url
        self.verify = verify
        self.headers = {"Accept": "*/*"}
        self.params = {}

        if verify is False:
            urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    def validate_url(self, path):
        """Validate URL formatting is correct.
        Args:
            path (str): URI path for API endpoint
        Returns:
            str: Formatted URL path for API endpoint
        """
        if not self.base_url.endswith("/") and not path.startswith("/"):
            full_path = f"{self.base_url}/{path}"
        else:
            full_path = f"{self.base_url}{path}"
        if not full_path.endswith("/"):
            return full_path
        return full_path

    def api_call(
        self, path: str, method: str = "GET", params: dict = {}, payload: dict = {}
    ):  # pylint: disable=dangerous-default-value
        """Send Request to API endpoint of type `method`. Defaults to GET request.
        Args:
            path (str): API path to send request to.
            method (str, optional): API request method. Defaults to "GET".
            params (dict, optional): Additional parameters to send to API. Defaults to None.
            payload (dict, optional): Message payload to be sent as part of API call.
        Raises:
            Exception: Error thrown if request errors.
        Returns:
            dict: JSON payload of API response.
        """
        url = self.validate_url(path)

        if not params:
            params = self.params
        else:
            params = {**self.params, **params}

        resp = requests.request(
            method=method,
            headers=self.headers,
            url=url,
            params=params,
            verify=self.verify,
            data=payload,
        )
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(f"Error in communicating to Netbox API: {err}")
            return {}
        return resp.json()


class NetboxApi(ApiEndpoint):  # pylint: disable=too-few-public-methods
    """Representation of interactions with Netbox API."""

    def __init__(self, base_url: str, priv_key_path: str, token: str, threading: bool, verify: bool = True):
        """Create Netbox API connection."""
        super().__init__(base_url=base_url)
        self.base_url = base_url
        self.verify = verify
        self.priv_key_path = priv_key_path
        self.token = token
        self.threading = threading
        self.netbox_api

        try:
          if token:
            netbox_api = pynetbox.api(base_url, token=token, threading=threading)
          if priv_key:
            netbox_api = pynetbox.api(base_url, private_key_file=priv_key_path, threading=threading)
        except ValueError:
          print(f"Error communicating with the netbox API, token or private key not defined.")

    def get_netbox_devices(self, netbox_api: ApiEndpoint, filter: str):
        """Get Hosts from Netbox API endpoint."""

        if filter is not None:
          devices = netbox_api.dcim.devices.filter()
        else:
          devices = netbox_api.dcim.devices.all()

        return devices