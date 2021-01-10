from unittest import TestCase


def countHi2(s: str) -> int:
    """
    Given a string, compute recursively the number of times lowercase "hi" appears in the string, however do not count
    "hi" that have an 'x' immediately before them.
    
    Examples:
    countHi2("ahixhi") → 1
    countHi2("ahibhi") → 2
    countHi2("xhixhi") → 0
    """
    if len(s) < 2:
        return 0
    else:
        if s[0: 3] == "xhi":
            return 0 + countHi2(s[3:])
        elif s[0: 2] == "hi":
            return 1 + countHi2(s[2:])
        else:
            return 0 + countHi2(s[1:])


class Test(TestCase):
    def test1(self):
        self.assertEqual(1, countHi2("ahixhi"))

    def test2(self):
        self.assertEqual(2, countHi2("ahibhi"))

    def test3(self):
        self.assertEqual(0, countHi2("xhixhi"))

    def test4(self):
        self.assertEqual(1, countHi2("hixhi"))

    def test5(self):
        self.assertEqual(2, countHi2("hixhhi"))

    def test6(self):
        self.assertEqual(3, countHi2("hihihi"))

    def test7(self):
        self.assertEqual(3, countHi2("hihihix"))

    def test8(self):
        self.assertEqual(2, countHi2("xhihihix"))

    def test9(self):
        self.assertEqual(0, countHi2("xxhi"))

    def test10(self):
        self.assertEqual(1, countHi2("hixxhi"))

    def test11(self):
        self.assertEqual(1, countHi2("hi"))

    def test12(self):
        self.assertEqual(0, countHi2("xxxx"))

    def test13(self):
        self.assertEqual(0, countHi2("h"))

    def test14(self):
        self.assertEqual(0, countHi2("x"))

    def test15(self):
        self.assertEqual(0, countHi2(""))
