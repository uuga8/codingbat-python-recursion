from unittest import TestCase


def stringClean(s: str) -> str:
    """
    Given a string, return recursively a "cleaned" string where adjacent chars that are the same have been reduced to a
    single char. So "yyzzza" yields "yza".
    
    Examples:
    stringClean("yyzzza") → "yza"
    stringClean("abbbcdd") → "abcd"
    stringClean("Hello") → "Helo"
    """
    if len(s) < 2:
        return s
    else:
        if s[0] == s[1]:
            return stringClean(s[1:])
        else:
            return s[0] + stringClean(s[1:])


class Test(TestCase):
    def test1(self):
        self.assertEqual("yza", stringClean("yyzzza"))

    def test2(self):
        self.assertEqual("abcd", stringClean("abbbcdd"))

    def test3(self):
        self.assertEqual("Helo", stringClean("Hello"))

    def test4(self):
        self.assertEqual("XabcY", stringClean("XXabcYY"))

    def test5(self):
        self.assertEqual("12ab45", stringClean("112ab445"))

    def test6(self):
        self.assertEqual("", stringClean(""))