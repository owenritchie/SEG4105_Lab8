import unittest

from src.core.strength import estimate_frames, meets_contract, status


class StrengthTests(unittest.TestCase):
    def test_empty_hive_is_zero(self):
        self.assertEqual(estimate_frames(18.0, 34.5, 45), 0.0)

    def test_strong_hive_meets_contract(self):
        frames = estimate_frames(28.0, 34.5, 50)
        self.assertTrue(meets_contract(frames))

    def test_status_bands(self):
        self.assertEqual(status(9.0), "OK")
        self.assertEqual(status(7.5), "WATCH")
        self.assertEqual(status(5.0), "ALERT")


if __name__ == "__main__":
    unittest.main()
