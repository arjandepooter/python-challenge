"""
http://www.pythonchallenge.com/pc/def/channel.html
"""
import re
from io import BytesIO
from zipfile import ZipFile

import requests

URL = "http://www.pythonchallenge.com/pc/def/channel.zip"
PATTERN = re.compile(r"Next nothing is (\d+)", flags=re.DOTALL)


def solve():
    data = BytesIO(requests.get(URL).content)
    zp = ZipFile(data)

    print(zp.open("readme.txt").read().decode("utf-8"))

    return "".join(c.decode("utf-8") for c in loop_zip(zp, "90052"))


def loop_zip(zp: ZipFile, current):
    comments = []
    while True:
        filename = f"{current}.txt"
        content = zp.open(filename).read().decode("utf-8")

        comments.append(zp.getinfo(filename).comment)
        if (m := PATTERN.match(content)) is not None:
            current = m.group(1)
        else:
            return comments


if __name__ == "__main__":
    print(solve())
