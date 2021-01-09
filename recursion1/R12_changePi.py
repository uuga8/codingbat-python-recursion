from unittest import TestCase


def changePi(s: str) -> str:
    """
    Given a string, compute recursively (no loops) a new string where all appearances of "pi" have been replaced by
    "3.14".
    
    Examples:
    changePi("xpix") → "x3.14x"
    changePi("pipi") → "3.143.14"
    changePi("pip") → "3.14p"
    """
    if not s:
        return ""
    if len(s) == 1:
        return s[0]
    else:
        if s[0] == "p" and s[1] == "i":
            return "3.14" + changePi(s[2:])
        else:
            return s[0] + changePi(s[1:])


class Test(TestCase):
    def test1(self):
        self.assertEqual("x3.14x", changePi("xpix"))

    def test2(self):
        self.assertEqual("3.143.14", changePi("pipi"))

    def test3(self):
        self.assertEqual("3.14p", changePi("pip"))

    def test4(self):
        self.assertEqual("3.14", changePi("pi"))

    def test5(self):
        self.assertEqual("hip", changePi("hip"))

    def test6(self):
        self.assertEqual("p", changePi("p"))

    def test7(self):
        self.assertEqual("x", changePi("x"))

    def test8(self):
        self.assertEqual("", changePi(""))

    def test9(self):
        self.assertEqual("3.14xx", changePi("pixx"))
