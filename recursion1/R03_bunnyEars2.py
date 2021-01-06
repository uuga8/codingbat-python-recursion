from unittest import TestCase


def bunnyEars2(bunnies: int) -> int:
    """
    We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The even
    bunnies (2, 4, ..) we'll say have 3 ears, because they each have a raised foot. Recursively return the number of
    "ears" in the bunny line 1, 2, ... n (without loops or multiplication).
    
    Examples:
    bunnyEars2(0) → 0
    bunnyEars2(1) → 2
    bunnyEars2(2) → 5
    """
    if bunnies == 0:
        return 0
    else:
        if bunnies % 2 == 0:
            return 3 + bunnyEars2(bunnies-1)
        else:
            return 2 + bunnyEars2(bunnies-1)

class Test(TestCase):
    def test1(self):
        self.assertEqual(0, bunnyEars2(0))

    def test2(self):
        self.assertEqual(2, bunnyEars2(1))

    def test3(self):
        self.assertEqual(5, bunnyEars2(2))

    def test4(self):
        self.assertEqual(7, bunnyEars2(3))

    def test5(self):
        self.assertEqual(10, bunnyEars2(4))

    def test6(self):
        self.assertEqual(12, bunnyEars2(5))

    def test7(self):
        self.assertEqual(15, bunnyEars2(6))
