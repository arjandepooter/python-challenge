"""
http://huge:file@www.pythonchallenge.com/pc/return/5808.html
"""
from io import BytesIO

import requests
from PIL import Image

IMAGE = "http://huge:file@www.pythonchallenge.com/pc/return/cave.jpg"


def solve():
    data = BytesIO(requests.get(IMAGE).content)
    im = Image.open(data)
    w, h = im.size

    im1 = Image.new(im.mode, (w // 2, h))
    im2 = Image.new(im.mode, (w // 2, h))

    for y in range(h):
        for x in range(w):
            (im1 if (x + y) % 2 == 0 else im2).putpixel(
                (x // 2, y), im.getpixel((x, y))
            )

    im1.show()
    im2.show()


if __name__ == "__main__":
    solve()
