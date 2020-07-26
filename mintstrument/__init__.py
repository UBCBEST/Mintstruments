from typing import Dict

from mock_smbus2 import mock_smbus2


def SMBus(ver, _address_to_device: Dict):
    """ _address_to_device should be a dictionary mapping integers to mock_smbus2 objects.
    """
    return mock_smbus2(_address_to_device)

