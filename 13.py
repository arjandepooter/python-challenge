"""
http://huge:file@www.pythonchallenge.com/pc/return/disproportional.html
"""
from xmlrpc.client import ServerProxy

SERVER = "http://www.pythonchallenge.com/pc/phonebook.php"


def solve():
    with ServerProxy(SERVER) as proxy:
        print(proxy.phone("Bert"))


if __name__ == "__main__":
    solve()
