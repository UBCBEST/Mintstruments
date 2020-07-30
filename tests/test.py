import unittest

from mintstrument import SMBus, MPR_device


class SMBusTest(unittest.TestCase):
    def test_block_pressure_read(self):
        atd = {0x18: MPR_device}
        bus = SMBus(atd)
        bus.write_i2c_block_data(0x18, 0, [0xAA, 0, 0])
        res = bus.read_i2c_block_data(0x18, 0, 4)
        self.assertListEqual(res, [0, 0, 0, 10])


if __name__ == "__main__":
    unittest.main()
