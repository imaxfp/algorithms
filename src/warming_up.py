import math
from functools import reduce


def find_hypotenuse(a, b):
    """
    Find hypotenuse for triangle with sides 'a' and 'b'
    For example:
    a = 3
    b = 4
    c = 5
    :param number:
    :return:
    """
    c = (a ** 2 + b ** 2) ** 0.5
    return c


def find_the_number_of_hundreds(number):
    """
    For example:
    1975 -> 9
    """
    number = number // 100 % 10
    return number


def sum_of_numbers(number):
    """
    For example:
    179 -> 17
    """
    result = reduce(lambda a, x: a + x, number)
    return result


def clock(minutes):
    """
    Program should return amount of hours and minutes as a tuple.
    Pay attention if more than 24h in minutes clock should reset amount of hours to 0
    For example:
    150 -> 2:30
    1441 -> 0:1
    """
    while minutes > 1440:
        minutes -= 1440
    H = minutes // 60 % 60
    M = minutes % 60
    time = (H, M)
    return time


def time_slot_difference(start_h, start_min, start_sec, end_h, end_min, end_sec):
    """
    You have two time slots with 3 numbers - hours, minutes, seconds in one 24 hour period of time.
    find the difference in seconds in this period
    For example:
    1,1,1 and 2,2,2 -> 3661
    """
    allSekStart = start_sec + start_min * 60 + start_h * 3600
    allSekEnd = end_sec + end_min * 60 + end_h * 3600
    result = allSekEnd - allSekStart
    return result


def find_the_max(arr_numbers):
    """
    For example:
    1,1,4,7 -> 7
    """
    # return max(arr_numbers)
    return max(arr_numbers)


def is_leap_year(year):
    """
    Return true if year is leap (the year is leap if year multiple 4 and NOT multiple by 100. Or  multiple by 400)
    For example:
    2007 -> FALSE
    2000 -> TRUE
    """
    if year % 4 == 0:
        return True
    return False
