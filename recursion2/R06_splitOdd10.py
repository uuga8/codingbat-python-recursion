from unittest import TestCase
from typing import List


def splitOdd10(nums: List[int]) -> bool:
    """
    Given an array of ints, is it possible to divide the ints into two groups, so that the sum of one group is a
    multiple of 10, and the sum of the other group is odd. Every int must be in one group or the other. Write a
    recursive helper method that takes whatever arguments you like, and make the initial call to your recursive helper
    from splitOdd10(). (No loops needed.)
    
    Examples:
    splitOdd10([5, 5, 5]) → true
    splitOdd10([5, 5, 6]) → false
    splitOdd10([5, 5, 6, 1]) → true
    """
    pass


class Test(TestCase):
    def test1(self):
        self.assertTrue(splitOdd10([5, 5, 5]))

    def test2(self):
        self.assertFalse(splitOdd10([5, 5, 6]))

    def test3(self):
        self.assertTrue(splitOdd10([5, 5, 6, 1]))

    def test4(self):
        self.assertTrue(splitOdd10([6, 5, 5, 1]))

    def test5(self):
        self.assertTrue(splitOdd10([6, 5, 5, 1, 10]))

    def test6(self):
        self.assertFalse(splitOdd10([6, 5, 5, 5, 1]))

    def test7(self):
        self.assertTrue(splitOdd10([1]))

    def test8(self):
        self.assertFalse(splitOdd10([]))

    def test9(self):
        self.assertTrue(splitOdd10([10, 7, 5, 5]))

    def test10(self):
        self.assertFalse(splitOdd10([10, 0, 5, 5]))

    def test11(self):
        self.assertTrue(splitOdd10([10, 7, 5, 5, 2]))
