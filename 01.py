"""
http://www.pythonchallenge.com/pc/def/map.html
"""

INPUT = """
g fmnc wms bgblr rpylqjyrc gr zw fylb.
rfyrq ufyr amknsrcpq ypc dmp.
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.
"""


def solve(txt: str):
    result = ""
    for c in txt:
        if c.isalpha():
            result += chr((2 + ord(c) - ord("a")) % 26 + ord("a"))
        else:
            result += c

    return result


if __name__ == "__main__":
    print(solve(INPUT))
    print(f"http://www.pythonchallenge.com/pc/def/{solve('map')}.html")
