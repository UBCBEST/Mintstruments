from typing import Dict

from .mock_smbus2 import mock_smbus2 as msb
from .mpr_device import MPR_device


def SMBus(address_to_device: Dict):
    """address_to_device should be a dictionary mapping integers to mock_smbus2 objects."""
    return msb(address_to_device)
