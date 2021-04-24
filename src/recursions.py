def reverse_array_rec(arr):
    """
    :param arr: 1,2,3,4,5
    :return: 5,4,3,2,1
    """

    def swap(arr, first, last):
        if first == last: return arr
        tmp = arr[first]
        arr[first] = arr[last]
        arr[last] = tmp
        return swap(arr, first + 1, last - 1)

    return swap(arr, 0, len(arr) - 1)


def fibonacci_number(n):
    """
    The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence,
    such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

    Restriction: loops cannot be used

    Input: n = 2
    Output: 1
    Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
    0, 1, 1, 2, 3, 5, 8, 13
    """

    def fibonacci_number(previous, current, iteration, n):
        if iteration == n: return current
        return fibonacci_number(current, previous + current, iteration + 1, n)

    return fibonacci_number(0, 1, 1, n)
