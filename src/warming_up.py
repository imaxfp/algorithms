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
    return math.sqrt(a ** 2 + b ** 2)


def find_the_number_of_hundreds(number):
    """
    For example:
    1975 -> 9
    """

    return [int(i) for i in str(number)][-3]


def sum_of_numbers(number):
    """
    For example:
    179 -> 17
    """
    # return sum([int(i) for i in str(number)])
    # return reduce(lambda a, b: a + b, [int(i) for i in str(number)])
    tmp = 0
    for i in [int(i) for i in str(number)]:
        tmp += i
    return tmp


def clock(minutes):
    """
    Program should return amount of hours and minutes as a tuple.
    Pay attention if more than 24h in minutes clock should reset amount of hours to 0
    For example:
    150 -> 2:30
    1441 -> 0:1
    """
    if minutes == 0: return 0, 0
    while minutes > 1440: minutes -= 1440
    return int(minutes / 60), minutes % 60


def time_slot_difference(start_h, start_min, start_sec, end_h, end_min, end_sec):
    """
    You have two time slots with 3 numbers - hours, minutes, seconds in one 24 hour period of time.
    find the difference in seconds in this period
    For example:
    1,1,1 and 2,2,2 -> 3661
    """
    start_in_sec = (start_h * 60 * 60) + (start_min * 60) + start_sec
    end_in_sec = (end_h * 60 * 60) + (end_min * 60) + end_sec
    return end_in_sec - start_in_sec


def find_the_max(arr_numbers):
    """
    For example:
    1,1,4,7 -> 7
    """
    # return max(arr_numbers)
    max = 0
    for i in arr_numbers:
        if max < i: max = i
    return max


def is_leap_year(year):
    """
    Return true if year is leap (the year is leap if year multiple 4 and NOT multiple by 100. Or  multiple by 400)
    For example:
    2007 -> FALSE
    2000 -> TRUE
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
