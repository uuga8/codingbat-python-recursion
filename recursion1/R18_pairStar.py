from unittest import TestCase


def pairStar(s: str) -> str:
    """
    Given a string, compute recursively a new string where identical chars that are adjacent in the original string are
    separated from each other by a "*".
    
    Examples:
    pairStar("hello") → "hel*lo"
    pairStar("xxyy") → "x*xy*y"
    pairStar("aaaa") → "a*a*a*a"
    """
    if len(s) < 2:
        return s
    else:
        return (s[0] + "*" if s[0] == s[1] else s[0]) + pairStar(s[1:])


class Test(TestCase):
    def test1(self):
        self.assertEqual("hel*lo", pairStar("hello"))

    def test2(self):
        self.assertEqual("x*xy*y", pairStar("xxyy"))

    def test3(self):
        self.assertEqual("a*a*a*a", pairStar("aaaa"))

    def test4(self):
        self.assertEqual("a*a*ab", pairStar("aaab"))

    def test5(self):
        self.assertEqual("a*a", pairStar("aa"))

    def test6(self):
        self.assertEqual("a", pairStar("a"))

    def test7(self):
        self.assertEqual("", pairStar(""))

    def test8(self):
        self.assertEqual("noadjacent", pairStar("noadjacent"))

    def test9(self):
        self.assertEqual("ab*ba", pairStar("abba"))
