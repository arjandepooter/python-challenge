"""
http://huge:file@www.pythonchallenge.com/pc/return/italy.html
"""
from io import BytesIO
from itertools import cycle

import requests
from PIL import Image

IMAGE = "http://huge:file@www.pythonchallenge.com/pc/return/wire.png"


def iter_lengths(start=100):
    yield start

    while start > 1:
        start -= 1
        yield start
        yield start


def solve():
    data = BytesIO(requests.get(IMAGE).content)
    im = Image.open(data)
    pixels = iter(im.getdata())
    result = Image.new(im.mode, (100, 100), (255, 255, 255))
    position = (-1, 0)
    directions = cycle([(1, 0), (0, 1), (-1, 0), (0, -1)])

    for length, direction in zip(iter_lengths(), directions):
        dx, dy = direction
        for _ in range(length):
            x, y = position
            position = (x + dx, y + dy)
            pixel = next(pixels)
            result.putpixel(position, pixel)

    result.show()


if __name__ == "__main__":
    solve()
