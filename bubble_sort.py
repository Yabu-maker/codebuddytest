#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
冒泡排序法 (Bubble Sort)
"""


def bubble_sort(arr: list) -> list:
    """
    对列表进行冒泡排序（升序），返回新列表，不修改原列表。

    算法思路：
      1. 从前往后依次比较相邻元素，若前者大于后者则交换。
      2. 每一轮结束后，最大的元素会"冒泡"到末尾。
      3. 重复 N-1 轮，每轮比较范围缩小 1。
    """
    n = len(arr)
    if n <= 1:
        return arr.copy()

    result = arr.copy()

    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        # 如果本轮没有发生交换，说明已经有序，提前结束
        if not swapped:
            break

    return result


def bubble_sort_inplace(arr: list) -> None:
    """
    原地冒泡排序（升序），直接修改传入的列表。
    """
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


if __name__ == "__main__":
    # 简单测试
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 1, 4, 2, 8],
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [1],
        [],
    ]

    for case in test_cases:
        original = case[:]
        sorted_list = bubble_sort(case)
        print(f"{original} → {sorted_list}")

    print("\n原地排序测试:")
    arr = [3, 6, 1, 8, 2, 9, 4]
    print(f"排序前: {arr}")
    bubble_sort_inplace(arr)
    print(f"排序后: {arr}")
