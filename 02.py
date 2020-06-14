"""
http://www.pythonchallenge.com/pc/def/ocr.html
"""


def solve(txt: str):
    return "".join(c for c in txt if c.isalpha())


if __name__ == "__main__":
    with open("inputs/02.in") as f:
        print(f"http://www.pythonchallenge.com/pc/def/{solve(f.read())}.html")
