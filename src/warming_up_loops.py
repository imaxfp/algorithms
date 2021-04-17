import math


def even_numbers_range(a, b):
    """
    Return all even numbers from 'a' to 'b'
    For example:
    a = 2
    b = 5
    return = [2,4]
    :param number:
    :return:
    """
    return list(filter(lambda x: x % 2 == 0, range(a, b)))


def find_the_number_of_hundreds(number):
    """
    For example:
    1975 -> 9
    """

    return [int(i) for i in str(number)][-3]
