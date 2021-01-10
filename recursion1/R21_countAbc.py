from unittest import TestCase


def countAbc(s: str) -> int:
    """
    Count recursively the total number of "abc" and "aba" substrings that appear in the given string.
    
    Examples:
    countAbc("abc") → 1
    countAbc("abcxxabc") → 2
    countAbc("abaxxaba") → 2
    """
    if len(s) < 3:
        return 0
    else:
        return (1 if s[0: 3] == "aba" or s[0: 3] == "abc" else 0) + countAbc(s[1:])


class Test(TestCase):
    def test1(self):
        self.assertEqual(1, countAbc("abc"))

    def test2(self):
        self.assertEqual(2, countAbc("abcxxabc"))

    def test3(self):
        self.assertEqual(2, countAbc("abaxxaba"))

    def test4(self):
        self.assertEqual(2, countAbc("ababc"))

    def test5(self):
        self.assertEqual(0, countAbc("abxbc"))

    def test6(self):
        self.assertEqual(1, countAbc("aaabc"))

    def test7(self):
        self.assertEqual(0, countAbc("hello"))

    def test8(self):
        self.assertEqual(0, countAbc(""))

    def test9(self):
        self.assertEqual(0, countAbc("ab"))

    def test10(self):
        self.assertEqual(1, countAbc("aba"))

    def test11(self):
        self.assertEqual(0, countAbc("aca"))
