"""
http://huge:file@www.pythonchallenge.com/pc/return/evil.html
"""
from io import BytesIO

import requests
from PIL import Image

DATA = "http://huge:file@www.pythonchallenge.com/pc/return/evil2.gfx"


def solve():
    data = requests.get(DATA).content

    for offset in range(5):
        img_data = bytes(b for b in data[offset::5])
        Image.open(BytesIO(img_data)).show()


if __name__ == "__main__":
    solve()
