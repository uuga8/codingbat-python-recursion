from unittest import TestCase


def powerN(base: int, n: int) -> int:
    """
    Given 'base' and 'n' that are both 1 or more, compute recursively (no loops) the value of base to the n power,
    so powerN(3, 2) is 9 (3 squared).
    
    Examples:
    powerN(3, 2) is 9 (3 squared).
    powerN(3, 1) → 3
    powerN(3, 2) → 9
    powerN(3, 3) → 27
    """
    if base == 1 or n == 0:
        return 1
    else:
        return base * powerN(base, n-1)


class Test(TestCase):
    def test1(self):
        self.assertEqual(3, powerN(3, 1))

    def test2(self):
        self.assertEqual(9, powerN(3, 2))

    def test3(self):
        self.assertEqual(27, powerN(3, 3))

    def test4(self):
        self.assertEqual(2, powerN(2, 1))

    def test5(self):
        self.assertEqual(4, powerN(2, 2))

    def test6(self):
        self.assertEqual(8, powerN(2, 3))

    def test7(self):
        self.assertEqual(16, powerN(2, 4))

    def test8(self):
        self.assertEqual(32, powerN(2, 5))

    def test9(self):
        self.assertEqual(10, powerN(10, 1))

    def test10(self):
        self.assertEqual(100, powerN(10, 2))
