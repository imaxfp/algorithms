from Cython.Compiler.ExprNodes import ListNode


def reverse_array_rec(arr, head, tail):
    """
    :param arr: 1,2,3,4,5
    :return: 5,4,3,2,1
    """
    if head >= tail: return arr
    arr[head], arr[tail] = arr[tail], arr[head]
    return reverse_array_rec(arr, head + 1, tail - 1)


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


def add_two_numbers(l1, l2):
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order, and each of their nodes contains a single digit.
    Add the two numbers and return the sum as a linked list.
    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Input: l1 = [2,4,3], l2 = [5,6,4]
    Output: [7,0,8]
    Explanation: 342 + 465 = 807.
    """

    def add_two_numbers(l1, l2, index, dozens, res_l: list) -> list:
        if index >= len(l1): return res_l
        sum = l1[index] + l2[index]
        if dozens == 1:
            sum += 1
            dozens = 0
        if sum >= 10:
            sum -= 10
            dozens = 1
        res_l.append(sum)
        return add_two_numbers(l1, l2, index + 1, dozens, res_l)

    return add_two_numbers(l1, l2, 0, 0, list())


def letter_combinations_phone_number(num):
    """
    Given a string containing digits from 2-9 inclusive, 
    return all possible letter combinations that the number could represent. Return the answer in any order.
    A mapping of digit to letters (just like on the telephone buttons) is given below. 
    Note that 1 does not map to any letters.

    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]    
    :return: 
    """

    def brute_force_rec(latter_index, first_arr, second_arr, res: list) -> list:
        if len(first_arr) <= latter_index: return res
        first_latter = first_arr[latter_index]
        res.extend(list(map(lambda x: first_latter + x, second_arr)))
        return brute_force_rec(latter_index + 1, first_arr, second_arr, res)

    tel = {2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
    arr_c = list(map(lambda x: tel.get(x), [int(x) for x in str(num)]))

    return brute_force_rec(0, [s for s in str(arr_c[0])], [s for s in str(arr_c[1])], list())


if __name__ == "__main__":
    print()
