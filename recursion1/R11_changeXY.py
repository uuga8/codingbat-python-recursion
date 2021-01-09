from unittest import TestCase


def changeXY(s: str) -> str:
    """
    Given a string, compute recursively (no loops) a new string where all the lowercase 'x' chars have been changed to
    'y' chars.
    
    Examples:
    changeXY("codex") → "codey"
    changeXY("xxhixx") → "yyhiyy"
    changeXY("xhixhix") → "yhiyhiy"
    """

    if not s:
        return ""
    else:
        if s[0] == "x":
            return "y" + changeXY(s[1:])
        else:
            return s[0] + changeXY(s[1:])

class Test(TestCase):
    def test1(self):
        self.assertEqual("codey", changeXY("codex"))

    def test2(self):
        self.assertEqual("yyhiyy", changeXY("xxhixx"))

    def test3(self):
        self.assertEqual("yhiyhiy", changeXY("xhixhix"))

    def test4(self):
        self.assertEqual("hiy", changeXY("hiy"))

    def test5(self):
        self.assertEqual("h", changeXY("h"))

    def test6(self):
        self.assertEqual("y", changeXY("x"))

    def test7(self):
        self.assertEqual("", changeXY(""))

    def test8(self):
        self.assertEqual("yyy", changeXY("xxx"))

    def test9(self):
        self.assertEqual("yyhyyi", changeXY("yyhxyi"))
