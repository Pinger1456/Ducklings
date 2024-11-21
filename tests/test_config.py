"""Test for parameters of config file"""
import unittest
from ducklings.config import DUCKLING_WIDTH, PAUSE, DENSITY


class TestConfig(unittest.TestCase):
    """Test Config"""
    def test_constants(self):
        """Test that constants have expected values."""
        self.assertTrue(isinstance(DUCKLING_WIDTH, int))
        self.assertTrue(0 < PAUSE < 1)
        self.assertTrue(0 <= DENSITY <= 1)


if __name__ == '__main__':
    unittest.main()
