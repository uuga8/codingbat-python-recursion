from unittest import TestCase


def allStar(s: str) -> str:
    """
    Given a string, compute recursively a new string where all the adjacent chars are now separated by a "*".
    
    Examples:
    allStar("hello") → "h*e*l*l*o"
    allStar("abc") → "a*b*c"
    allStar("ab") → "a*b"
    """
    if len(s) < 2:
        return s
    else:
        return s[0] + "*" + allStar(s[1:])


class Test(TestCase):
    def test1(self):
        self.assertEqual("h*e*l*l*o", allStar("hello"))

    def test2(self):
        self.assertEqual("a*b*c", allStar("abc"))

    def test3(self):
        self.assertEqual("a*b", allStar("ab"))

    def test4(self):
        self.assertEqual("a", allStar("a"))

    def test5(self):
        self.assertEqual("", allStar(""))

    def test6(self):
        self.assertEqual("3*.*1*4", allStar("3.14"))

    def test7(self):
        self.assertEqual("C*h*o*c*o*l*a*t*e", allStar("Chocolate"))
