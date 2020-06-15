"""
http://huge:file@www.pythonchallenge.com/pc/return/uzi.html
"""
from calendar import isleap
from datetime import date


def solve():
    valid_dates = []
    for year in range(1006, 2000, 10):
        d = date(year, 1, 27)
        if d.weekday() == 1 and isleap(year):
            valid_dates.append(d)

    print(valid_dates[-2])


if __name__ == "__main__":
    solve()
