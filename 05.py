"""
http://www.pythonchallenge.com/pc/def/peak.html
"""
import pickle

import requests

URL = "http://www.pythonchallenge.com/pc/def/banner.p"


def solve():
    data = requests.get(URL).content
    for row in pickle.loads(data):
        for c, l in row:
            print(c * l, end="")
        print()


if __name__ == "__main__":
    solve()
