def reverse_array_classic(arr):
    """
    :param arr: 1,2,3,4,5
    :return: 5,4,3,2,1
    """
    # return list.reverse(arr)

    # 1 find indexes for swap elements
    head = 0
    tail = len(arr) - 1

    # 2 stop reverse if middle array established
    # 2 TODO or

    # algo for swapping elements places
    while head != tail:
        print(arr)
        tmp = arr[head]
        arr[head] = arr[tail]
        arr[tail] = tmp
        head += 1
        tail -= 1

    return arr


def reverse_array_rec(arr, head, tail):
    """
    # 1. detect the condition for STOP recursion
    # 2. send to recursion 'arr' and parameters 'head' and 'tail'
    # 3. implement the logic of recursion
    # 4. call self

    :param arr:
    :param head:
    :param tail:
    :return:
    """
    return None


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
    return None
