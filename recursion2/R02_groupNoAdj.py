from unittest import TestCase
from typing import List


def groupNoAdj(start: int, nums: List[int], target: int) -> bool:
    """
    Given an array of ints, is it possible to choose a group of some of the ints, such that the group sums to the given
    target with this additional constraint: If a value in the array is chosen to be in the group, the value immediately
    following it in the array must not be chosen. (No loops needed.)
    
    Examples:
    groupNoAdj(0, [2, 5, 10, 4], 12) → true
    groupNoAdj(0, [2, 5, 10, 4], 14) → false
    groupNoAdj(0, [2, 5, 10, 4], 7) → false
    """
    if start >= len(nums):
        return target == 0
    else:
        return groupNoAdj(start + 2, nums, target - nums[start]) or groupNoAdj(start + 1, nums, target)


class Test(TestCase):
    def test1(self):
        self.assertTrue(groupNoAdj(0, [2, 5, 10, 4], 12))

    def test2(self):
        self.assertFalse(groupNoAdj(0, [2, 5, 10, 4], 14))

    def test3(self):
        self.assertFalse(groupNoAdj(0, [2, 5, 10, 4], 7))

    def test4(self):
        self.assertTrue(groupNoAdj(0, [2, 5, 10, 4, 2], 7))

    def test5(self):
        self.assertTrue(groupNoAdj(0, [2, 5, 10, 4], 9))

    def test6(self):
        self.assertTrue(groupNoAdj(0, [10, 2, 2, 3, 3], 15))

    def test7(self):
        self.assertFalse(groupNoAdj(0, [10, 2, 2, 3, 3], 7))

    def test8(self):
        self.assertTrue(groupNoAdj(0, [], 0))

    def test9(self):
        self.assertTrue(groupNoAdj(0, [1], 1))

    def test10(self):
        self.assertFalse(groupNoAdj(0, [9], 1))

    def test11(self):
        self.assertTrue(groupNoAdj(0, [9], 0))
