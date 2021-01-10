from unittest import TestCase


def endX(s: str) -> str:
    """
    Given a string, compute recursively a new string where all the lowercase 'x' chars have been moved to the end of the
    string.
    
    Examples:
    endX("xxre") → "rexx"
    endX("xxhixx") → "hixxxx"
    endX("xhixhix") → "hihixxx"
    """
    if not s:
        return ""
    else:
        if s[0] == "x":
            return endX(s[1:]) + "x"
        else:
            return s[0] + endX(s[1:])


class Test(TestCase):
    def test1(self):
        self.assertEqual("rexx", endX("xxre"))

    def test2(self):
        self.assertEqual("hixxxx", endX("xxhixx"))

    def test3(self):
        self.assertEqual("hihixxx", endX("xhixhix"))

    def test4(self):
        self.assertEqual("hiy", endX("hiy"))

    def test5(self):
        self.assertEqual("h", endX("h"))

    def test6(self):
        self.assertEqual("x", endX("x"))

    def test7(self):
        self.assertEqual("xx", endX("xx"))

    def test8(self):
        self.assertEqual("", endX(""))

    def test9(self):
        self.assertEqual("bxx", endX("bxx"))

    def test10(self):
        self.assertEqual("baxx", endX("bxax"))

    def test11(self):
        self.assertEqual("aaaxxx", endX("axaxax"))
