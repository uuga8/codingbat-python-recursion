from unittest import TestCase
from typing import List


def groupSum(start: int, nums: List[int], target: int) -> bool:
    """
    Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given
    target? This is a classic backtracking recursion problem. Once you understand the recursive backtracking strategy in
    this problem, you can use the same pattern for many problems to search a space of choices. Rather than looking at
    the whole array, our convention is to consider the part of the array starting at index 'start' and continuing to the
    end of the array. The caller can specify the whole array simply by passing start as 0. No loops are needed -- the
    recursive calls progress down the array.
    
    Examples:
    groupSum(0, [2, 4, 8], 10) → true
    groupSum(0, [2, 4, 8], 14) → true
    groupSum(0, [2, 4, 8], 9) → false
    """

    if start == len(nums):
        return target == 0
    else:
        return groupSum(start + 1, nums, target - nums[start]) or groupSum(start + 1, nums, target)


class Test(TestCase):
    def test1(self):
        self.assertTrue(groupSum(0, [2, 4, 8], 10))

    def test2(self):
        self.assertTrue(groupSum(0, [2, 4, 8], 14))

    def test3(self):
        self.assertFalse(groupSum(0, [2, 4, 8], 9))

    def test4(self):
        self.assertTrue(groupSum(0, [2, 4, 8], 8))

    def test5(self):
        self.assertTrue(groupSum(1, [2, 4, 8], 8))

    def test6(self):
        self.assertFalse(groupSum(1, [2, 4, 8], 2))

    def test7(self):
        self.assertTrue(groupSum(0, [1], 1))

    def test8(self):
        self.assertFalse(groupSum(0, [9], 1))

    def test9(self):
        self.assertTrue(groupSum(1, [9], 0))

    def test10(self):
        self.assertTrue(groupSum(0, [], 0))

    def test11(self):
        self.assertTrue(groupSum(0, [10, 2, 2, 5], 17))

    def test12(self):
        self.assertTrue(groupSum(0, [10, 2, 2, 5], 15))
