import math
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
    l = list()
    for i in range(1, n):
        if i ** 2 < n:
            l.append(i ** 2)
        else:
            break
    return l


def minimal_divisor(n):
    """
    Find the minimal divisor of the 'n'
    :param n: 15
    :return: 3
    """
    min_div = 0
    for i in range(2, n):
        if n % i == 0:
            min_div = i
            break
    return min_div


def find_count_of_numbers_greater_then_index_number(arr, index):
    """
    For example:
    :param arr: [1 2 3 4 5]
    :param index: 0
    :return: 4
    """
    c = 0
    for i in range(index + 1, len(arr)):
        if arr[i] > arr[index]:
            c += 1
        else:
            break

    return c
