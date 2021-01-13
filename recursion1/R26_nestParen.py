from unittest import TestCase


def nestParen(s: str) -> bool:
    """
    Given a string, return true if it is a nesting of zero or more pairs of parenthesis, like "(())" or "((()))".
    Suggestion: check the first and last chars, and then recur on what's inside them.
    
    Examples:
    nestParen("(())") → true
    nestParen("((()))") → true
    nestParen("(((x))") → false
    """
    if len(s) == 0:
        return True
    return s[0] == "(" and s[-1] == ")" and nestParen(s[1: -1])


class Test(TestCase):
    def test1(self):
        self.assertTrue(nestParen("(())"))

    def test2(self):
        self.assertTrue(nestParen("((()))"))

    def test3(self):
        self.assertFalse(nestParen("(((x))"))

    def test4(self):
        self.assertFalse(nestParen("((())"))

    def test5(self):
        self.assertFalse(nestParen("((()()"))

    def test6(self):
        self.assertTrue(nestParen("()"))

    def test7(self):
        self.assertTrue(nestParen(""))

    def test8(self):
        self.assertFalse(nestParen("(yy)"))

    def test9(self):
        self.assertTrue(nestParen("(())"))

    def test10(self):
        self.assertFalse(nestParen("(((y))"))

    def test11(self):
        self.assertFalse(nestParen("((y)))"))

    def test12(self):
        self.assertTrue(nestParen("((()))"))

    def test13(self):
        self.assertFalse(nestParen("(())))"))

    def test14(self):
        self.assertFalse(nestParen("((yy())))"))
