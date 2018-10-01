from typing import List


def add(*args: List[List[int]]):
    current_sums = args[0]
    for i in range(1, len(args)):
        current_sums = add_helper(current_sums, args[i])
    return current_sums


def add_helper(m1: List[List[int]], m2: List[List[int]]):
    result: List[List[int]] = []
    if len(m1) != len(m2):
        raise ValueError('Given matrices are not the same size.')
    for i in range(len(m1)):
        if len(m1[i]) != len(m2[i]):
            raise ValueError('Given matrices are not the same size.')
        result.append([])
        for j in range(len(m1[i])):
            result[i].append(m1[i][j] + m2[i][j])
    return result
