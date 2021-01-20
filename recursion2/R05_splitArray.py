from unittest import TestCase
from typing import List

def splitArray(nums: List[int]) -> bool:
    """
    Given an array of ints, is it possible to divide the ints into two groups, so that the sums of the two groups are
    the same. Every int must be in one group or the other. Write a recursive helper method that takes whatever arguments
    you like, and make the initial call to your recursive helper from splitArray(). (No loops needed.)
    
    Examples:
    splitArray([2, 2]) → true
    splitArray([2, 3]) → false
    splitArray([5, 2, 3]) → true
    """

    total = sum(nums)

    def list_sum(nums: List[int], index: int, first_half: int) -> bool:
        if index == len(nums):
            return first_half == total - first_half
        else:
            return list_sum(nums, index + 1, first_half + nums[index]) or \
                   list_sum(nums, index + 1, first_half)

    return total % 2 == 0 and list_sum(nums, index=0, first_half=0)


class Test(TestCase):
    def test1(self):
        self.assertTrue(splitArray([2, 2]))

    def test2(self):
        self.assertFalse(splitArray([2, 3]))

    def test3(self):
        self.assertTrue(splitArray([5, 2, 3]))

    def test4(self):
        self.assertFalse(splitArray([5, 2, 2]))

    def test5(self):
        self.assertTrue(splitArray([1, 1, 1, 1, 1, 1]))

    def test6(self):
        self.assertFalse(splitArray([1, 1, 1, 1, 1]))

    def test7(self):
        self.assertTrue(splitArray([]))

    def test8(self):
        self.assertFalse(splitArray([1]))

    def test9(self):
        self.assertFalse(splitArray([3, 5]))

    def test10(self):
        self.assertTrue(splitArray([5, 3, 2]))

    def test11(self):
        self.assertTrue(splitArray([2, 2, 10, 10, 1, 1]))

    def test12(self):
        self.assertFalse(splitArray([1, 2, 2, 10, 10, 1, 1]))
