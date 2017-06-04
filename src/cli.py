"""
latviski

Usage:
  lv add <part-of-speech> <word>
  lv test <word>
"""

from docopt import docopt
from src.latviski import Latviski

def main():
    """Main CLI entry point."""
    options = docopt(__doc__, version="0.0.1")
    Latviski().run_command(options)
