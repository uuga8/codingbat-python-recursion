from unittest import TestCase
from typing import List


def array11(nums: List[int], index: int) -> int:
    """
    Given an array of ints, compute recursively the number of times that the value 11 appears in the array. We'll use
    the convention of considering only the part of the array that begins at the given index. In this way, a recursive
    call can pass index+1 to move down the array. The initial call will pass in index as 0.
    
    Examples:
    array11([1, 2, 11], 0) → 1
    array11([11, 11], 0) → 2
    array11([1, 2, 3, 4], 0) → 0
    """
    if not nums or index == len(nums):
        return 0
    else:
        return (1 if nums[index] == 11 else 0) + array11(nums, index+1)


class Test(TestCase):
    def test1(self):
        self.assertEqual(1, array11([1, 2, 11], 0))

    def test2(self):
        self.assertEqual(2, array11([11, 11], 0))

    def test3(self):
        self.assertEqual(0, array11([1, 2, 3, 4], 0))

    def test4(self):
        self.assertEqual(3, array11([1, 11, 3, 11, 11], 0))

    def test5(self):
        self.assertEqual(1, array11([11], 0))

    def test6(self):
        self.assertEqual(0, array11([1], 0))

    def test7(self):
        self.assertEqual(0, array11([], 0))

    def test8(self):
        self.assertEqual(2, array11([11, 2, 3, 4, 11, 5], 0))
