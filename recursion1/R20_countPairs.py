from unittest import TestCase


def countPairs(s: str) -> int:
    """
    We'll say that a "pair" in a string is two instances of a char separated by a char. So "AxA" the A's make a pair.
    Pair's can overlap, so "AxAxA" contains 3 pairs -- 2 for A and 1 for x. Recursively compute the number of pairs in
    the given string.
    
    Examples:
    countPairs("axa") → 1
    countPairs("axax") → 2
    countPairs("axbx") → 1
    """
    pass


class Test(TestCase):
    def test1(self):
        self.assertEqual(1, countPairs("axa"))

    def test2(self):
        self.assertEqual(2, countPairs("axax"))

    def test3(self):
        self.assertEqual(1, countPairs("axbx"))

    def test4(self):
        self.assertEqual(0, countPairs("hi"))

    def test5(self):
        self.assertEqual(3, countPairs("hihih"))

    def test6(self):
        self.assertEqual(3, countPairs("ihihhh"))

    def test7(self):
        self.assertEqual(0, countPairs("ihjxhh"))

    def test8(self):
        self.assertEqual(0, countPairs(""))

    def test9(self):
        self.assertEqual(0, countPairs("a"))

    def test10(self):
        self.assertEqual(0, countPairs("aa"))
