from unittest import TestCase



def count8(n: int) -> int:
    """
    Given a non-negative int n, compute recursively (no loops) the count of the occurrences of 8 as a digit, except that
    an 8 with another 8 immediately to its left counts double, so 8818 yields 4. Note that mod (%) by 10 yields the
    rightmost digit (126 % 10 is 6), while divide (/) by 10 removes the rightmost digit (126 / 10 is 12).
    
    Examples:
    count8(8) → 1
    count8(818) → 2
    count8(8818) → 4
    """
    if n < 8:
        return 0
    else:

        return (1 if n % 10 == 8 else 0) + \
               (1 if n % 10 == 8 and (n // 10) % 10 == 8 else 0) \
               + count8(n // 10)


class Test(TestCase):
    def test1(self):
        self.assertEqual(1, count8(8))

    def test2(self):
        self.assertEqual(2, count8(818))

    def test3(self):
        self.assertEqual(4, count8(8818))

    def test4(self):
        self.assertEqual(4, count8(8088))

    def test5(self):
        self.assertEqual(0, count8(123))

    def test6(self):
        self.assertEqual(2, count8(81238))

    def test7(self):
        self.assertEqual(6, count8(88788))

    def test8(self):
        self.assertEqual(1, count8(8234))

    def test9(self):
        self.assertEqual(1, count8(2348))

    def test10(self):
        self.assertEqual(3, count8(23884))

    def test11(self):
        self.assertEqual(0, count8(0))

    def test12(self):
        self.assertEqual(5, count8(1818188))

    def test13(self):
        self.assertEqual(5, count8(8818181))

    def test14(self):
        self.assertEqual(1, count8(1080))

    def test15(self):
        self.assertEqual(3, count8(188))

    def test16(self):
        self.assertEqual(9, count8(88888))

    def test17(self):
        self.assertEqual(2, count8(9898))
