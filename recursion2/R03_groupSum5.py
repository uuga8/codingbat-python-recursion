from unittest import TestCase
from typing import List


def groupSum5(start: int, nums: List[int], target: int) -> bool:
    """
    Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given
    target with these additional constraints: all multiples of 5 in the array must be included in the group. If the
    value immediately following a multiple of 5 is 1, it must not be chosen. (No loops needed.)
    
    Examples:
    groupSum5(0, [2, 5, 10, 4], 19) → true
    groupSum5(0, [2, 5, 10, 4], 17) → true
    groupSum5(0, [2, 5, 10, 4], 12) → false
    """
    if start >= len(nums):
        return target == 0
    else:
        if nums[start] % 5 == 0:
            if start < len(nums) - 1 and nums[start + 1] == 1:
                return groupSum5(start + 2, nums, target - nums[start])
            else:
                return groupSum5(start + 1, nums, target - nums[start])
        else:
            return groupSum5(start + 1, nums, target - nums[start]) or groupSum5(start + 1, nums, target)


class Test(TestCase):
    def test1(self):
        self.assertTrue(groupSum5(0, [2, 5, 10, 4], 19))

    def test2(self):
        self.assertTrue(groupSum5(0, [2, 5, 10, 4], 17))

    def test3(self):
        self.assertFalse(groupSum5(0, [2, 5, 10, 4], 12))

    def test4(self):
        self.assertFalse(groupSum5(0, [2, 5, 4, 10], 12))

    def test5(self):
        self.assertFalse(groupSum5(0, [3, 5, 1], 4))

    def test6(self):
        self.assertTrue(groupSum5(0, [3, 5, 1], 5))

    def test7(self):
        self.assertTrue(groupSum5(0, [1, 3, 5], 5))

    def test8(self):
        self.assertFalse(groupSum5(0, [3, 5, 1], 9))

    def test9(self):
        self.assertFalse(groupSum5(0, [2, 5, 10, 4], 7))

    def test10(self):
        self.assertTrue(groupSum5(0, [2, 5, 10, 4], 15))

    def test11(self):
        self.assertFalse(groupSum5(0, [2, 5, 10, 4], 11))

    def test12(self):
        self.assertTrue(groupSum5(0, [1], 1))

    def test13(self):
        self.assertFalse(groupSum5(0, [9], 1))

    def test14(self):
        self.assertTrue(groupSum5(0, [9], 0))
