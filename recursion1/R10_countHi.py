from unittest import TestCase


def countHi(s: str) -> int:
    """
    Given a string, compute recursively (no loops) the number of times lowercase "hi" appears in the string.
    
    Examples:
    countHi("xxhixx") → 1
    countHi("xhixhix") → 2
    countHi("hi") → 1
    """
    if len(s) < 2:
        return 0
    return (1 if s[-2:] == "hi" else 0) + countHi(s[: -1])


class Test(TestCase):
    def test1(self):
        self.assertEqual(1, countHi("xxhixx"))

    def test2(self):
        self.assertEqual(2, countHi("xhixhix"))

    def test3(self):
        self.assertEqual(1, countHi("hi"))

    def test4(self):
        self.assertEqual(2, countHi("hihih"))

    def test5(self):
        self.assertEqual(0, countHi("h"))

    def test6(self):
        self.assertEqual(0, countHi(""))

    def test7(self):
        self.assertEqual(4, countHi("ihihihihih"))

    def test8(self):
        self.assertEqual(5, countHi("ihihihihihi"))

    def test9(self):
        self.assertEqual(3, countHi("hiAAhi12hi"))

    def test10(self):
        self.assertEqual(3, countHi("xhixhxihihhhih"))
