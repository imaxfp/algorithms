import math
from functools import reduce

from numpy import long


def rotate_the_array_to_the_right(nums, k):
    """
    Given an array, rotate the array to the right by k steps, where k is non-negative.
    :return:

    Input: nums = [1,2,3,4, - 5,6,7], k = 3
    Output: [5,6,7, - 1,2,3,4]
    Explanation:
    rotate 1 steps to the right: [7,1,2,3,4,5,6]
    rotate 2 steps to the right: [6,7,1,2,3,4,5]
    rotate 3 steps to the right: [5,6,7,1,2,3,4]
    """
    pivot_element = nums[k]
    for i in range(0, k):
        head = nums[i]
        nums[i] = nums[k + 1]
        nums[k] = head
        k += 1
    nums[len(nums) - 1] = pivot_element

    return nums


def get_indexes_the_sum_of_two_numbers(nums, target):
    """
    Given an array of integers nums and an integer target,
    return indices of the two numbers such that they add up to target.

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    for i in range(0, len(nums) - 1):
        for j in range(0, len(nums) - 1):
            if nums[i] + nums[j] == target: return (i, j)
    return 0


def two_sum_problem(nums, target):
    """
    https://web.stanford.edu/class/cs9/sample_probs/TwoSum.pdf

    Restriction - the complexity of the algo should be higher than O(n*n)
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1].
    """
    for i in range(0, len(nums)):
        for j in range(0, len(nums)):
            if i != j and nums[i] + nums[j] == target: return [i, j]


def find_GCD__greatest_common_divisor(a, b):
    """
    Brut force https://www.youtube.com/watch?v=jFd-6EPfnec&ab_channel=KhanAcademy
    Euclidian algorithm https://www.youtube.com/watch?v=JUzYl1TYMcU&ab_channel=LearnMathTutorials

    :param a:
    :param b:
    :return:
    """
    return None
