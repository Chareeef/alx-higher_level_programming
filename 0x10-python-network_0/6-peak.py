#!/usr/bin/python3
"""This module contains the find_peak() function"""


def find_peak(nums):
    """Return the peak of an unsorted list of integers"""

    if type(nums) is not list or nums == []:
        return None

    peak = nums[0]
    # print(nums)

    for i in range(1, len(nums) - 1):
        # print(nums[i], ' ?')
        if nums[i - 1] < nums[i] and nums[i + 1] < nums[i]:
            peak = nums[i] if nums[i] > peak else peak

        if i == len(nums) - 2:
            # print(nums[i + 1], ' !')
            if nums[i + 1] > peak:
                peak = nums[i + 1]

    return peak


if __name__ == "__main__":
    print(find_peak([1, 2, 4, 6, 3]))
    print(find_peak([4, 2, 1, 2, 3, 1]))
    print(find_peak([2, 2, 2]))
    print(find_peak([-2, -4, 2, 1]))
    print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
