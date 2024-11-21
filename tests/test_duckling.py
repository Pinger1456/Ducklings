"""Testing basic process - duckling"""
import unittest
from ducklings.duckling import Duckling


class TestDuckling(unittest.TestCase):
    """Testing Duckling"""
    def setUp(self):
        """Set up a Duckling instance for testing."""
        self.duckling = Duckling()

    def test_initial_state(self):
        """Test the initial state of a duckling."""
        self.assertIn(self.duckling.direction, ['left', 'right'])
        self.assertIn(self.duckling.body, ['chubby', 'very chubby'])
        self.assertIsNotNone(self.duckling.part_to_display_next)

    def test_get_next_body_part(self):
        """Test the sequence of body parts."""
        parts = [self.duckling.get_next_body_part() for _ in range(3)]
        self.assertEqual(len(parts), 3)  # Should have three parts
        self.assertIsNone(self.duckling.part_to_display_next)


if __name__ == '__main__':
    unittest.main()
