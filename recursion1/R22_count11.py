from unittest import TestCase


def count11(s: str) -> int:
    """
    Given a string, compute recursively (no loops) the number of "11" substrings in the string. The "11" substrings
    should not overlap.
    
    Examples:
    count11("11abc11") → 2
    count11("abc11x11x11") → 3
    count11("111") → 1
    """
    if len(s) < 2:
        return 0
    else:
        if s[0:2] == "11":
            return 1 + count11(s[2:])
        else:
            return 0 + count11(s[1:])


class Test(TestCase):
    def test1(self):
        self.assertEqual(2, count11("11abc11"))

    def test2(self):
        self.assertEqual(3, count11("abc11x11x11"))

    def test3(self):
        self.assertEqual(1, count11("111"))

    def test4(self):
        self.assertEqual(2, count11("1111"))

    def test5(self):
        self.assertEqual(0, count11("1"))

    def test6(self):
        self.assertEqual(0, count11(""))

    def test7(self):
        self.assertEqual(0, count11("hi"))

    def test8(self):
        self.assertEqual(4, count11("11x111x1111"))

    def test9(self):
        self.assertEqual(1, count11("1x111"))

    def test10(self):
        self.assertEqual(0, count11("1Hello1"))
