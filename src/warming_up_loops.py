from functools import reduce
from numpy import long


def even_numbers_range(a, b):
    """
    Return all even numbers from 'a' to 'b'
    For example:
    :param a: = 2
    :param b: = 5
    :return: [2,4]

    """
    return list(filter(lambda x: x % 2 == 0, range(a, b)))


def factorial(n):
    """
    Get factorial of the number 'n'
    :param n: 4
    :return: 24
    """
    return long(reduce(lambda x, y: x * y, [i for i in range(1, n + 1)]))


def divisors_of_a_number(n):
    """
    :param n: 32
    :return: 1 2 4 8 16 32
    """
    return list(filter(lambda i: n % i == 0, [i for i in range(1, n + 1)]))


def list_of_squares(n):
    """
    Return list of all squares but not more than 'n'
    :param n: 15
    :return: 1,4,9
    """
    return None


def minimal_divisor(n):
    """
    Find the minimal divisor of the 'n'
    :param n: 15
    :return: 3
    """
    return None


def find_count_of_numbers_greater_then_index_number(arr, index):
    """
    For example:
    :param arr: [1 2 3 4 5]
    :param index: 0
    :return: 4
    """
    return None


def reverse_array(r):
    return None


def shift_array_to_right(array, pivot):
    """
    Restriction - additional array cannot be used
    Example:
    :param array: 4 5 3 4 2 3
    :param pivot: 6
    :return: 3 4 5 3 4 2
    """
    return None


def find_max(nums):
    return None
