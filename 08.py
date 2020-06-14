"""
http://www.pythonchallenge.com/pc/def/integrity.html
"""
import bz2

USERNAME = b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
PASSWORD = b"BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"


def solve():
    un = bz2.decompress(USERNAME).decode("utf-8")
    pw = bz2.decompress(PASSWORD).decode("utf-8")

    return (un, pw)


if __name__ == "__main__":
    un, pw = solve()
    print(f"http://{un}:{pw}@www.pythonchallenge.com/pc/return/good.html")
