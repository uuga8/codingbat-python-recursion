from unittest import TestCase
from typing import List


def groupSum6(start: int, nums: List[int], target: int) -> bool:
    """
    Given an array of ints, is it possible to choose a group of some of the ints, beginning at the start index, such
    that the group sums to the given target? However, with the additional constraint that all 6's must be chosen. (No
    loops needed.)
    
    Examples:
    groupSum6(0, [5, 6, 2], 8) → true
    groupSum6(0, [5, 6, 2], 9) → false
    groupSum6(0, [5, 6, 2], 7) → false
    """
    if start == len(nums):
        return target == 0
    else:
        if nums[start] == 6:
            return groupSum6(start + 1, nums, target - nums[start])
        else:
            return groupSum6(start + 1, nums, target - nums[start]) or groupSum6(start + 1, nums, target)


class Test(TestCase):
    def test1(self):
        self.assertTrue(groupSum6(0, [5, 6, 2], 8))

    def test2(self):
        self.assertFalse(groupSum6(0, [5, 6, 2], 9))

    def test3(self):
        self.assertFalse(groupSum6(0, [5, 6, 2], 7))

    def test4(self):
        self.assertTrue(groupSum6(0, [1], 1))

    def test5(self):
        self.assertFalse(groupSum6(0, [9], 1))

    def test6(self):
        self.assertTrue(groupSum6(0, [], 0))

    def test7(self):
        self.assertTrue(groupSum6(0, [3, 2, 4, 6], 8))

    def test8(self):
        self.assertTrue(groupSum6(0, [6, 2, 4, 3], 8))

    def test9(self):
        self.assertFalse(groupSum6(0, [5, 2, 4, 6], 9))

    def test10(self):
        self.assertFalse(groupSum6(0, [6, 2, 4, 5], 9))

    def test11(self):
        self.assertFalse(groupSum6(0, [3, 2, 4, 6], 3))

    def test12(self):
        self.assertTrue(groupSum6(0, [1, 6, 2, 6, 4], 12))

    def test13(self):
        self.assertTrue(groupSum6(0, [1, 6, 2, 6, 4], 13))

    def test14(self):
        self.assertFalse(groupSum6(0, [1, 6, 2, 6, 4], 4))

    def test15(self):
        self.assertFalse(groupSum6(0, [1, 6, 2, 6, 4], 9))

    def test16(self):
        self.assertTrue(groupSum6(0, [1, 6, 2, 6, 5], 14))

    def test17(self):
        self.assertTrue(groupSum6(0, [1, 6, 2, 6, 5], 15))
