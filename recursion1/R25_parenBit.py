from unittest import TestCase


def parenBit(s: str) -> str:
    """
    Given a string that contains a single pair of parenthesis, compute recursively a new string made of only of the
    parenthesis and their contents, so "xyz(abc)123" yields "(abc)".
    
    Examples:
    parenBit("xyz(abc)123") → "(abc)"
    parenBit("x(hello)") → "(hello)"
    parenBit("(xy)1") → "(xy)"
    """

    if len(s) == 0:
        return ""
    else:
        if s[0] == "(" and s[-1] == ")":
            return s[0:]
        elif s[0] == "(":
            return parenBit(s[0: -1])
        elif s[-1] == ")":
            return parenBit(s[1:])
        else:
            return parenBit(s[1: -1])


class Test(TestCase):
    def test1(self):
        self.assertEqual("(abc)", parenBit("xyz(abc)123"))

    def test2(self):
        self.assertEqual("(hello)", parenBit("x(hello)"))

    def test3(self):
        self.assertEqual("(xy)", parenBit("(xy)1"))

    def test4(self):
        self.assertEqual("(possible)", parenBit("not really (possible)"))

    def test5(self):
        self.assertEqual("(abc)", parenBit("(abc)"))

    def test6(self):
        self.assertEqual("(abc)", parenBit("(abc)xyz"))

    def test7(self):
        self.assertEqual("(abc)", parenBit("(abc)x"))

    def test8(self):
        self.assertEqual("(x)", parenBit("(x)"))

    def test9(self):
        self.assertEqual("()", parenBit("()"))

    def test10(self):
        self.assertEqual("(ipsa)", parenBit("res (ipsa) loquitor"))

    def test11(self):
        self.assertEqual("(not really)", parenBit("hello(not really)there"))







