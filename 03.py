"""
http://www.pythonchallenge.com/pc/def/equality.html
"""
import re


def solve(txt: str):
    result = re.findall(r"[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]", txt)
    return "".join(result)


if __name__ == "__main__":
    with open("inputs/03.in") as f:
        print(f"http://www.pythonchallenge.com/pc/def/{solve(f.read())}.html")
