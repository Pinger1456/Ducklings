"""Entry point for the Ducklings screensaver."""

from ducklings.screensaver import DucklingScreensaver

if __name__ == '__main__':
    try:
        screensaver = DucklingScreensaver()
        screensaver.run()
    except KeyboardInterrupt:
        print("\nScreensaver stopped.")
