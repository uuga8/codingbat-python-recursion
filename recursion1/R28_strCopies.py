from unittest import TestCase


def strCopies(s: str, sub: str, n: int) -> bool:
    """
    Given a string and a non-empty substring 'sub', compute recursively if at least 'n' copies of 'sub' appear in the
    string somewhere, possibly with overlapping. 'N' will be non-negative.
    
    Examples:
    strCopies("catcowcat", "cat", 2) → true
    strCopies("catcowcat", "cow", 2) → false
    strCopies("catcowcat", "cow", 1) → true
    """

    if n == 0:
        return True
    if len(s) < len(sub):
        return False
    else:
        return strCopies(s[1:], sub, n-1) if s[0: len(sub)] == sub else strCopies(s[1:], sub, n)


class Test(TestCase):
    def test1(self):
        self.assertTrue(strCopies("catcowcat", "cat", 2))

    def test2(self):
        self.assertFalse(strCopies("catcowcat", "cow", 2))

    def test3(self):
        self.assertTrue(strCopies("catcowcat", "cow", 1))

    def test4(self):
        self.assertTrue(strCopies("iiijjj", "i", 3))

    def test5(self):
        self.assertFalse(strCopies("iiijjj", "i", 4))

    def test6(self):
        self.assertTrue(strCopies("iiijjj", "ii", 2))

    def test7(self):
        self.assertFalse(strCopies("iiijjj", "ii", 3))

    def test8(self):
        self.assertFalse(strCopies("iiijjj", "x", 3))

    def test9(self):
        self.assertTrue(strCopies("iiijjj", "x", 0))

    def test10(self):
        self.assertTrue(strCopies("iiiiij", "iii", 3))

    def test11(self):
        self.assertFalse(strCopies("iiiiij", "iii", 4))

    def test12(self):
        self.assertTrue(strCopies("ijiiiiij", "iiii", 2))

    def test13(self):
        self.assertFalse(strCopies("ijiiiiij", "iiii", 3))
