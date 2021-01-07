from unittest import TestCase

def sumDigits(n: int) -> int:
    """
    Given a non-negative int n, return the sum of its digits recursively (no loops). Note that mod (%) by 10 yields the
    rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
    
    Examples:
    sumDigits(126) → 9
    sumDigits(49) → 13
    sumDigits(12) → 3
    """
    if n == 0:
        return 0
    else:
        return int(n % 10 + sumDigits(n / 10))


class Test(TestCase):
    def test1(self):
        self.assertEqual(9, sumDigits(126))

    def test2(self):
        self.assertEqual(13, sumDigits(49))

    def test3(self):
        self.assertEqual(3, sumDigits(12))

    def test4(self):
        self.assertEqual(1, sumDigits(10))

    def test5(self):
        self.assertEqual(1, sumDigits(1))

    def test6(self):
        self.assertEqual(0, sumDigits(0))

    def test7(self):
        self.assertEqual(10, sumDigits(730))

    def test8(self):
        self.assertEqual(4, sumDigits(1111))

    def test9(self):
        self.assertEqual(5, sumDigits(11111))

    def test10(self):
        self.assertEqual(3, sumDigits(10110))
