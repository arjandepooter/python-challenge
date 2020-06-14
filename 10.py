"""
http://huge:file@www.pythonchallenge.com/pc/return/bull.html
"""


def eq_chunks(s):
    cur = ""
    result = []

    for c in s:
        if len(cur) == 0 or c == cur[0]:
            cur += c
        else:
            result.append((cur[0], len(cur)))
            cur = c

    result.append((cur[0], len(cur)))

    return result


def conway(n, current="1"):
    assert all(c.isnumeric() for c in current)
    for _ in range(n):
        yield current
        current = "".join([f"{l}{c}" for c, l in eq_chunks(current)])


if __name__ == "__main__":
    result = len(list(conway(31))[30])
    print(f"http://huge:file@www.pythonchallenge.com/pc/return/{result}.html")
