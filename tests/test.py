import unittest

from mintstrument import SMBus, MPR_device


class SMBusTest(unittest.TestCase):
    def test_feature_one(self):
        atd = {0x18: MPR_device}
        bus = SMBus(atd)
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
