from unittest import TestCase


def countX(s: str) -> int:
    """
    Given a string, compute recursively (no loops) the number of lowercase 'x' chars in the string.
    
    Examples:
    countX("xxhixx") → 4
    countX("xhixhix") → 3
    countX("hi") → 0
    """
    if s == "":
        return 0
    else:
        return (1 if s[-1] == "x" else 0) + countX(s[0: -1])


class Test(TestCase):
    def test1(self):
        self.assertEqual(4, countX("xxhixx"))

    def test2(self):
        self.assertEqual(3, countX("xhixhix"))

    def test3(self):
        self.assertEqual(0, countX("hi"))

    def test4(self):
        self.assertEqual(0, countX("h"))

    def test5(self):
        self.assertEqual(1, countX("x"))

    def test6(self):
        self.assertEqual(0, countX(""))

    def test7(self):
        self.assertEqual(0, countX("hihi"))
