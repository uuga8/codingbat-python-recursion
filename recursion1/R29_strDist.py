from unittest import TestCase


def strDist(s: str, sub: str) -> int:
    """
    Given a string and a non-empty substring 'sub', compute recursively the largest substring which starts and ends with
    'sub' and return its length.
    
    Examples:
    strDist("catcowcat", "cat") → 9
    strDist("catcowcat", "cow") → 3
    strDist("cccatcowcatxx", "cat") → 9
    """
    if len(s) < len(sub):
        return 0
    else:
        if s[0: len(sub)] == sub and s[-len(sub):] == sub:
            return len(s)
        elif s[0: len(sub)] == sub and s[-len(sub):] != sub:
            return strDist(s[0: -1], sub)
        elif s[0: len(sub)] != sub and s[-len(sub):] == sub:
            return strDist(s[1:], sub)
        else:
            return strDist(s[1: -1], sub)


class Test(TestCase):
    def test1(self):
        self.assertEqual(9, strDist("catcowcat", "cat"))

    def test2(self):
        self.assertEqual(3, strDist("catcowcat", "cow"))

    def test3(self):
        self.assertEqual(9, strDist("cccatcowcatxx", "cat"))

    def test4(self):
        self.assertEqual(12, strDist("abccatcowcatcatxyz", "cat"))

    def test5(self):
        self.assertEqual(3, strDist("xyx", "x"))

    def test6(self):
        self.assertEqual(1, strDist("xyx", "y"))

    def test7(self):
        self.assertEqual(0, strDist("xyx", "z"))

    def test8(self):
        self.assertEqual(1, strDist("z", "z"))

    def test9(self):
        self.assertEqual(0, strDist("x", "z"))

    def test10(self):
        self.assertEqual(0, strDist("", "z"))

    def test11(self):
        self.assertEqual(13, strDist("hiHellohihihi", "hi"))

    def test12(self):
        self.assertEqual(5, strDist("hiHellohihihi", "hih"))

    def test13(self):
        self.assertEqual(1, strDist("hiHellohihihi", "o"))
