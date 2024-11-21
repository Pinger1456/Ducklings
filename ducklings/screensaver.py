"""Screensaver logic for Ducklings project."""

import random
import sys
import time
import shutil
from typing import List, Optional
from ducklings.duckling import Duckling
from ducklings.config import DUCKLING_WIDTH, PAUSE, DENSITY


class DucklingScreensaver:
    """Main class to manage the Duckling screensaver."""

    def __init__(self):
        self.width = shutil.get_terminal_size()[0] - 1
        self.lanes: List[Optional[Duckling]] = [None] * (self.width // DUCKLING_WIDTH)

    def run(self):
        """Runs the screensaver."""
        print("Duckling Screensaver. Press Ctrl-C to quit...")
        time.sleep(2)

        while True:
            self.update_screen()

    def reset(self):
        """Resets the screensaver."""
        self.lanes = [None] * (self.width // DUCKLING_WIDTH)
        print("Screensaver reset.")

    def update_screen(self):
        """Updates the screen by moving ducklings."""
        for lane_num, duckling in enumerate(self.lanes):
            if duckling is None and random.random() <= DENSITY:
                self.lanes[lane_num] = Duckling()

            if self.lanes[lane_num] is not None:
                print(self.lanes[lane_num].get_next_body_part(), end='')
                if self.lanes[lane_num].part_to_display_next is None:
                    self.lanes[lane_num] = None
            else:
                print(' ' * DUCKLING_WIDTH, end='')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE)
