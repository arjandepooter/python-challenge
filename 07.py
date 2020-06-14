"""
http://www.pythonchallenge.com/pc/def/oxygen.html
"""
from io import BytesIO

import requests
from PIL import Image


def solve():
    data = BytesIO(
        requests.get("http://www.pythonchallenge.com/pc/def/oxygen.png").content
    )
    im = Image.open(data)

    result = ""
    for x in range(0, im.width, 7):
        (r, g, b, _) = im.getpixel((x, 48))
        if r == g == b:
            result += chr(r)

    return result


if __name__ == "__main__":
    print(solve())
    w = "".join(map(chr, [105, 110, 116, 101, 103, 114, 105, 116, 121]))
    print(f"http://www.pythonchallenge.com/pc/def/{w}.html")
