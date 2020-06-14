import re
import sys

import requests

URL = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
PATTERN = re.compile(r".*and the next nothing is (\d+)", flags=re.DOTALL)


def solve(nothing):
    while True:
        print(f"Fetching nothing {nothing}", file=sys.stderr)
        data = requests.get(URL, params={"nothing": nothing}).text
        if (m := PATTERN.match(data)) is not None:
            nothing = m.group(1)
        else:
            return (nothing, data)


if __name__ == "__main__":
    print(solve("12345"))
    print(f"http://www.pythonchallenge.com/pc/def/{solve('8022')[1]}")
