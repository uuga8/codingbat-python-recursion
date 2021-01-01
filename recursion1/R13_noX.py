from unittest import TestCase


def noX(s: str) -> str:
    """
    Given a string, compute recursively a new string where all the 'x' chars have been removed.
    
    Examples:
    noX("xaxb") → "ab"
    noX("abc") → "abc"
    noX("xx") → ""
    """
    pass


class Test(TestCase):
    def test1(self):
        self.assertEqual("ab", noX("xaxb"))

    def test2(self):
        self.assertEqual("abc", noX("abc"))

    def test3(self):
        self.assertEqual("", noX("xx"))

    def test4(self):
        self.assertEqual("", noX(""))

    def test5(self):
        self.assertEqual("ab", noX("axxbxx"))
