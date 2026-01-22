__author__ = 'andrii'
from urllib.request import urlopen
import sys

def fetch_url(url):
    """Fetch and print contents from a URL"""
    try:
        with urlopen(url) as response:
            for line in response:
                print(line.decode("utf-8"), end='')
        return True
    except Exception as e:
        print(f"Error fetching URL: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    # Updated to a working URL - Python's README from the official repository
    target_url = "https://raw.githubusercontent.com/python/cpython/main/README.rst"
    fetch_url(target_url)
