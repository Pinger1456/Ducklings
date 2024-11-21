"""Test for ducklings/screensaver.py"""
import unittest
from ducklings.screensaver import DucklingScreensaver
from ducklings.duckling import Duckling


class TestDucklingScreensaver(unittest.TestCase):
    """Testing screensaver"""
    def setUp(self):
        """Set up a DucklingScreensaver instance for testing."""
        self.screensaver = DucklingScreensaver()

    def test_initial_lanes(self):
        """Test that lanes are initialized correctly."""
        self.assertEqual(len(self.screensaver.lanes), self.screensaver.width // 5)
        self.assertTrue(all(lane is None for lane in self.screensaver.lanes))

    def test_run_method(self):
        """Test the run method (simulation of one frame)."""
        self.screensaver.lanes[0] = Duckling()  # Place a duckling in the first lane
        self.screensaver.update_screen()
        self.assertIsInstance(self.screensaver.lanes[0], Duckling)
        # Ensure the duckling is updated


if __name__ == '__main__':
    unittest.main()
