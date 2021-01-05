from unittest import TestCase


def bunnyEars(bunnies: int) -> int:
    """
    We have a number of bunnies and each bunny has two big floppy ears. We want to compute the total number of ears
    across all the bunnies recursively (without loops or multiplication).
    
    Examples:
    bunnyEars(0) → 0
    bunnyEars(1) → 2
    bunnyEars(2) → 4
    """
    if bunnies == 0:
        return 0
    else:
        return 2 + bunnyEars(bunnies-1)

class Test(TestCase):
    def test1(self):
        self.assertEqual(0, bunnyEars(0))

    def test2(self):
        self.assertEqual(2, bunnyEars(1))

    def test3(self):
        self.assertEqual(4, bunnyEars(2))

    def test4(self):
        self.assertEqual(6, bunnyEars(3))

    def test5(self):
        self.assertEqual(8, bunnyEars(4))

    def test6(self):
        self.assertEqual(10, bunnyEars(5))

    def test7(self):
        self.assertEqual(24, bunnyEars(12))

    def test8(self):
        self.assertEqual(100, bunnyEars(50))
