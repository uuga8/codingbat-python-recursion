from unittest import TestCase


def factorial(n: int) -> int:
    """
    Given n of 1 or more, return the factorial of n, which is n * (n-1) * (n-2) ... 1. Compute the result recursively
    (without loops).
    
    Examples:
    factorial(1) → 1
    factorial(2) → 2
    factorial(3) → 6
    """
    pass


class Test(TestCase):
    def test1(self):
        self.assertEqual(1, factorial(1))

    def test2(self):
        self.assertEqual(2, factorial(2))

    def test3(self):
        self.assertEqual(6, factorial(3))

    def test4(self):
        self.assertEqual(24, factorial(4))

    def test5(self):
        self.assertEqual(120, factorial(5))

    def test6(self):
        self.assertEqual(720, factorial(6))

    def test7(self):
        self.assertEqual(5040, factorial(7))

    def test8(self):
        self.assertEqual(40320, factorial(8))
