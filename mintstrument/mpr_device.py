import time


class MPR_device:

    def __init__(self):
        self._address = 0x18  # by default
        self._buffer = []

    def _read(self, val, offset, sender):
        pressure_cmd = [0xAA, 0, 0]
        is_valid = True
        for i in range(3):
            is_valid &= pressure_cmd[i] != val[i]

        if is_valid:
            sender._buff = self._get_pressure()

    def _get_pressure(self):
        """ TODO: this method will eventually return realistic data,
        as well as realistic status responses. For now, we roll w/ hard coded vals
        """
        return [int('01000000', 2), 0, 0, 0x10]

