from unittest import TestCase


def triangle(rows: int) -> int:
    """
    We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3
    blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle
    with the given number of rows.
    
    Examples:
    triangle(0) → 0
    triangle(1) → 1
    triangle(2) → 3
    """
    if rows == 0:
        return 0
    else:
        return rows + triangle(rows-1)

class Test(TestCase):
    def test1(self):
        self.assertEqual(0, triangle(0))

    def test2(self):
        self.assertEqual(1, triangle(1))

    def test3(self):
        self.assertEqual(3, triangle(2))

    def test4(self):
        self.assertEqual(6, triangle(3))

    def test5(self):
        self.assertEqual(10, triangle(4))

    def test6(self):
        self.assertEqual(15, triangle(5))

    def test7(self):
        self.assertEqual(21, triangle(6))
