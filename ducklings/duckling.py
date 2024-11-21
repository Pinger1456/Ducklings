"""Duckling class definition."""

import random
from ducklings.config import (LEFT, RIGHT, CHUBBY, VERY_CHUBBY, OPEN, CLOSED,
                              OUT, UP, DOWN, HEAD, BODY, FEET, BEADY,
                              WIDE, HAPPY, ALOOF)


class Duckling:
    """Represents a single duckling."""

    def __init__(self):
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])
        self.eyes = BEADY if self.body == CHUBBY \
            else random.choice([BEADY, WIDE, HAPPY, ALOOF])
        self.part_to_display_next = HEAD

    @staticmethod
    def get_head_str():
        """Returns the string of the duckling's head."""
        head_str = '>'
        # Logic for the head (similar to original code)
        return head_str

    @staticmethod
    def get_body_str():
        """Returns the string of the duckling's body."""
        body_str = '('
        # Logic for the body
        return body_str

    def get_feet_str(self):
        """Returns the string of the duckling's feet."""
        return ' ^^ ' if self.body == CHUBBY else ' ^ ^ '

    def get_next_body_part(self):
        """Returns the next body part to be displayed."""
        if self.part_to_display_next == HEAD:
            self.part_to_display_next = BODY
            return self.get_head_str()
        if self.part_to_display_next == BODY:
            self.part_to_display_next = FEET
            return self.get_body_str()
        if self.part_to_display_next == FEET:
            self.part_to_display_next = None
            return self.get_feet_str()
        return None
