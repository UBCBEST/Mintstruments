import unittest

from mintstrument import SMBus, MPR_device


class SMBusTest(unittest.TestCase):
    def setUp(self):
        atd = {0x18: MPR_device}
        self.bus = SMBus(atd)

    def test_byte_read_write(self):
        byte_sequence = [0xAA, 0, 0]
        expected_ret = [0, 0, 0, 10]
        actual_ret = []
        for i, byte in enumerate(byte_sequence):
            self.bus.write_byte_data(0x18, i, [byte])
        for i, byte in enumerate(expected_ret):
            ret = self.bus.read_byte_data(0x18, i)
            actual_ret.extend(ret)
        self.assertListEqual(actual_ret, expected_ret)

    def test_word_read_write(self):
        byte_sequence = [[0xAA, 0], [0, 0]]
        expected_ret = [0, 0, 0, 10]
        actual_ret = []
        for i, byte in enumerate(byte_sequence):
            self.bus.write_word_data(0x18, 2 * i, byte)
        for i, byte in enumerate(expected_ret):
            ret = self.bus.read_word_data(0x18, 2 * i)
            actual_ret.extend(ret)
        self.assertListEqual(actual_ret, expected_ret)

    def test_block_read_write(self):
        self.bus.write_i2c_block_data(0x18, 0, [0xAA, 0, 0])
        res = self.bus.read_i2c_block_data(0x18, 0, 4)
        self.assertListEqual(res, [0, 0, 0, 10])


if __name__ == "__main__":
    unittest.main()
