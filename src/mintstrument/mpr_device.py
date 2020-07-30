import time

from collections.abc import Iterable

from .i2c_device import I2C_device


class MPR_device(I2C_device):

    PRESSURE_CMD = [0xAA, 0, 0]

    def __init__(self):
        self._address = 0x18  # by default
        self._buff = []
        self._ptr = 0

    def _read(self, sender, register=0, size=1):
        return self._buff[register : register + size]

    def _write(self, value, register=0, size=1):
        if not isinstance(value, Iterable):
            raise RuntimeError("parameter :value: must be an iterable")

        for i in range(size):
            if value[i] == self.PRESSURE_CMD[self._ptr]:
                self._ptr += 1
            else:
                self._ptr = 0
            if self._ptr == len(self.PRESSURE_CMD):
                self._buff = self._get_pressure()
                self._ptr = 0

    def _get_pressure(self):
        return [0, 0, 0, 10]
