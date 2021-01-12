from unittest import TestCase


def strCount(s: str, sub: str) -> int:
    """
    Given a string and a non-empty substring 'sub', compute recursively the number of times that 'sub' appears in the
    string, without the sub strings overlapping.
    
    Examples:
    strCount("catcowcat", "cat") → 2
    strCount("catcowcat", "cow") → 1
    strCount("catcowcat", "dog") → 0
    """
    if len(s) < len(sub):
        return 0
    else:
        if s[0: len(sub)] == sub:
            return 1 + strCount(s[len(sub):], sub)
        else:
            return strCount(s[1:], sub)


class Test(TestCase):
    def test1(self):
        self.assertEqual(2, strCount("catcowcat", "cat"))

    def test2(self):
        self.assertEqual(1, strCount("catcowcat", "cow"))

    def test3(self):
        self.assertEqual(0, strCount("catcowcat", "dog"))

    def test4(self):
        self.assertEqual(2, strCount("cacatcowcat", "cat"))

    def test5(self):
        self.assertEqual(2, strCount("xyx", "x"))

    def test6(self):
        self.assertEqual(4, strCount("iiiijj", "i"))

    def test7(self):
        self.assertEqual(2, strCount("iiiijj", "ii"))

    def test8(self):
        self.assertEqual(1, strCount("iiiijj", "iii"))

    def test9(self):
        self.assertEqual(2, strCount("iiiijj", "j"))

    def test10(self):
        self.assertEqual(1, strCount("iiiijj", "jj"))

    def test11(self):
        self.assertEqual(4, strCount("aaabababab", "ab"))

    def test12(self):
        self.assertEqual(1, strCount("aaabababab", "aa"))

    def test13(self):
        self.assertEqual(6, strCount("aaabababab", "a"))
