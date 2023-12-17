#!/usr/bin/python3
"""This module contains the find_peak() function"""


def find_peak(nums):
    """Return the peak of an unsorted list of integers"""

    # Edge cases

    if type(nums) is not list or nums == []:
        return None
    elif len(nums) == 1:
        return nums[0]
    elif nums[0] >= nums[1]:
        return nums[0]
    elif nums[-1] >= nums[-2]:
        return nums[-1]

    # O(log(n)) Implementation

    n = len(nums) - 1
    mid = n // 2

    while mid > 0:
        if nums[mid] >= nums[mid + 1] and nums[mid] >= nums[mid + 1]:
            return nums[mid]
        elif nums[mid] <= nums[mid + 1]:
            return find_peak(nums[mid + 1:])
        else:
            return find_peak(nums[0: mid])
