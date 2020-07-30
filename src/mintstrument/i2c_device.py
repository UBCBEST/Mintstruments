"""
I2C Device abstract base class

This file defines the abstract base class for i2c devices, which are meant
to be accessed through the mock_smbus2 class.

One can think of these as Finite State Machines.
(https://en.wikipedia.org/wiki/Finite-state_machine)

To make your own device, subclass from this abstract base class, and add whatever
you need to make your FSM work for your needs.

"""
from typing import Iterable, TYPE_CHECKING
from abc import ABC, abstractmethod

if TYPE_CHECKING:
    from mock_smbus2 import mock_smbus2


class I2C_device(ABC):
    @abstractmethod
    def __init__(self):
        # TODO: Refactor into array, or some other type
        #       of constant size
        self.buff: List = None

    @abstractmethod
    def _read(self, sender: "mock_smbus2", register: int = 0, size: int = 1):
        """
        This is read from the SMBus' perspective.
        I.e. When SMBus is trying to read, it will
        call this method.
        """
        pass

    @abstractmethod
    def _write(self, value: Iterable, sender: "mock_smbus2", register=0, size=1):
        """
        Much like the _read method, this is the write
        from the SMBus perspective. Mostly, this should
        just be modifying the state of the device.
        """
        pass
