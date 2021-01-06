from unittest import TestCase



def fibonacci(n: int) -> int:
    """
    The fibonacci sequence is a famous bit of mathematics, and it happens to have a recursive definition. The first two
    values in the sequence are 0 and 1 (essentially 2 base cases). Each subsequent value is the sum of the previous two
    values, so the whole sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. Define a recursive fibonacci(n) method that
    returns the nth fibonacci number, with n=0 representing the start of the sequence.
    
    Examples:
    fibonacci(0) → 0
    fibonacci(1) → 1
    fibonacci(2) → 1
    """

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class Test(TestCase):
    def test1(self):
        self.assertEqual(0, fibonacci(0))

    def test2(self):
        self.assertEqual(1, fibonacci(1))

    def test3(self):
        self.assertEqual(1, fibonacci(2))

    def test4(self):
        self.assertEqual(2, fibonacci(3))

    def test5(self):
        self.assertEqual(3, fibonacci(4))

    def test6(self):
        self.assertEqual(5, fibonacci(5))

    def test7(self):
        self.assertEqual(8, fibonacci(6))
