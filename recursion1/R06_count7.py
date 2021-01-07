from unittest import TestCase


def count7(n: int) -> int:
    """
    Given a non-negative int n, return the count of the occurrences of 7 as a digit, so for example 717 yields 2. (no
    loops). Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the
    rightmost digit (126 / 10 is 12).
    
    Examples:
    count7(717) → 2
    count7(7) → 1
    count7(123) → 0
    """
    if n < 7:
        return 0
    else:

        return (1 if n % 10 == 7 else 0) + count7(n // 10)


class Test(TestCase):
    def test1(self):
        self.assertEqual(2, count7(717))

    def test2(self):
        self.assertEqual(1, count7(7))

    def test3(self):
        self.assertEqual(0, count7(123))

    def test4(self):
        self.assertEqual(2, count7(77))

    def test5(self):
        self.assertEqual(1, count7(7123))

    def test6(self):
        self.assertEqual(3, count7(771237))

    def test7(self):
        self.assertEqual(4, count7(771737))

    def test8(self):
        self.assertEqual(2, count7(47571))

    def test9(self):
        self.assertEqual(6, count7(777777))

    def test10(self):
        self.assertEqual(4, count7(70701277))

    def test11(self):
        self.assertEqual(5, count7(777576197))

    def test12(self):
        self.assertEqual(0, count7(99999))
