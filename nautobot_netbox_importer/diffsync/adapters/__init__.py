"""DiffSync adapters for nautobot-netbox-importer."""

from packaging import version

from .nautobot import NautobotDiffSync
from .netbox import NetBox210DiffSync, NetBox3XDiffSync

netbox_adapters = {
    version.parse("2.10.3"): NetBox210DiffSync,
    version.parse("2.10.4"): NetBox210DiffSync,
    version.parse("2.10.5"): NetBox210DiffSync,
    version.parse("2.10.6"): NetBox210DiffSync,
    version.parse("2.10.7"): NetBox210DiffSync,
    version.parse("2.10.8"): NetBox210DiffSync,
    version.parse("3.0.0"): Netbox3XDiffSync,
    version.parse("3.0.1"): Netbox3XDiffSync,
    version.parse("3.0.2"): Netbox3XDiffSync,
    version.parse("3.0.3"): Netbox3XDiffSync,
    version.parse("3.0.4"): Netbox3XDiffSync,
    version.parse("3.0.5"): Netbox3XDiffSync,
    version.parse("3.0.6"): Netbox3XDiffSync,
    version.parse("3.0.7"): Netbox3XDiffSync,
    version.parse("3.0.8"): Netbox3XDiffSync,
    version.parse("3.0.9"): Netbox3XDiffSync,
    version.parse("3.0.10"): Netbox3XDiffSync,
    version.parse("3.0.11"): Netbox3XDiffSync,
    version.parse("3.0.12"): Netbox3XDiffSync,
    version.parse("3.1.0"): NetBox3XDiffSync,
    version.parse("3.1.1"): NetBox3XDiffSync,
    version.parse("3.1.2"): NetBox3XDiffSync,
    version.parse("3.1.3"): NetBox3XDiffSync,
    version.parse("3.1.4"): NetBox3XDiffSync,
    version.parse("3.1.5"): NetBox3XDiffSync,
    version.parse("3.1.6"): NetBox3XDiffSync,
    version.parse("3.1.7"): NetBox3XDiffSync,
    version.parse("3.1.8"): NetBox3XDiffSync,
    version.parse("3.1.9"): NetBox3XDiffSync,
    version.parse("3.1.10"): NetBox3XDiffSync,
    version.parse("3.1.11"): NetBox3XDiffSync,
    version.parse("3.2.0"): NetBox3XDiffSync,
    version.parse("3.2.1"): NetBox3XDiffSync,
    version.parse("3.2.2"): NetBox3XDiffSync,
    version.parse("3.2.3"): NetBox3XDiffSync,
    version.parse("3.2.4"): NetBox3XDiffSync,
    version.parse("3.2.5"): NetBox3XDiffSync,
    version.parse("3.2.6"): NetBox3XDiffSync,
    version.parse("3.2.7"): NetBox3XDiffSync,
    version.parse("3.2.8"): NetBox3XDiffSync,
    version.parse("3.2.9"): NetBox3XDiffSync,
}

__all__ = (
    "netbox_adapters",
    "NautobotDiffSync",
)
