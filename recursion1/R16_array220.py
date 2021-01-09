from unittest import TestCase
from typing import List


def array220(nums: List[int], index: int) -> bool:
    """
    Given an array of ints, compute recursively if the array contains somewhere a value followed in the array by that
    value times 10. We'll use the convention of considering only the part of the array that begins at the given index.
    In this way, a recursive call can pass index+1 to move down the array. The initial call will pass in index as 0.
    
    Examples:
    array220([1, 2, 20], 0) → true
    array220([3, 30], 0) → true
    array220([3], 0) → false
    """
    if not nums or index == len(nums)-1:
        return False
    else:
        if nums[index+1] == nums[index]*10:
            return True
        else:
            return array220(nums, index+1)


class Test(TestCase):
    def test1(self):
        self.assertTrue(array220([1, 2, 20], 0))

    def test2(self):
        self.assertTrue(array220([3, 30], 0))

    def test3(self):
        self.assertFalse(array220([3], 0))

    def test4(self):
        self.assertFalse(array220([], 0))

    def test5(self):
        self.assertTrue(array220([3, 3, 30, 4], 0))

    def test6(self):
        self.assertFalse(array220([2, 19, 4], 0))

    def test7(self):
        self.assertFalse(array220([20, 2, 21], 0))

    def test8(self):
        self.assertTrue(array220([20, 2, 21, 210], 0))

    def test9(self):
        self.assertTrue(array220([2, 200, 2000], 0))

    def test10(self):
        self.assertTrue(array220([0, 0], 0))

    def test11(self):
        self.assertFalse(array220([1, 2, 3, 4, 5, 6], 0))

    def test12(self):
        self.assertTrue(array220([1, 2, 3, 4, 5, 50, 6], 0))

    def test13(self):
        self.assertFalse(array220([1, 2, 3, 4, 5, 51, 6], 0))
