from unittest import TestCase
from typing import List


def array6(nums: List[int], index: int) -> bool:
    """
    Given an array of ints, compute recursively if the array contains a 6. We'll use the convention of considering only
    the part of the array that begins at the given index. In this way, a recursive call can pass index+1 to move down
    the array. The initial call will pass in index as 0.
    
    Examples:
    array6([1, 6, 4], 0) → true
    array6([1, 4], 0) → false
    array6([6], 0) → true
    """
    if not nums:
        return False
    else:
        if nums[index] == 6:
            return True
        elif index == len(nums)-1:
            return False
        else:
            return array6(nums, index+1)


class Test(TestCase):
    def test1(self):
        self.assertTrue(array6([1, 6, 4], 0))

    def test2(self):
        self.assertFalse(array6([1, 4], 0))

    def test3(self):
        self.assertTrue(array6([6], 0))

    def test4(self):
        self.assertFalse(array6([], 0))

    def test5(self):
        self.assertTrue(array6([6, 2, 2], 0))

    def test6(self):
        self.assertFalse(array6([2, 5], 0))

    def test7(self):
        self.assertTrue(array6([1, 9, 4, 6, 6], 0))
