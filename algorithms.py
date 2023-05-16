"""Implementations of some sorting"""
import random

from Interfaces import List


def linear_search(a: List, x):
    # todo
    for i in range(0, len(a) - 1):
        if a[i] == x:
            return i
    return None


def binary_search(a: List, x):
    # todo
    l = 0
    r = len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return None


def _merge(a0: List, a1: List, a: List):
    # todo
    cp = 0
    while 0 < len(a0) and 0 < len(a1):
        if a0[0] < a1[0]:
            a[cp] = a0.pop(0)
        else:
            a[cp] = a1.pop(0)
        cp += 1
    while 0 < len(a0):
        a[cp] = a0.pop(0)
        cp += 1
    while 0 < len(a1):
        a[cp] = a1.pop(0)
        cp += 1
    return a

def merge_sort(a: List):
    # todo
    if len(a) <= 1:
        return a
    a0 = merge_sort(a[0:len(a) // 2])
    a1 = merge_sort(a[len(a) // 2:len(a)])
    return _merge(a0, a1, a)



def _partition(a, start, end):
    pivot = a[start]
    l = start + 1
    while l <= end and a[l] <= pivot:
        l += 1
    r = end
    while r >= start and a[r] > pivot:
        r -= 1
    while l < r:
        a[l], a[r] = a[r], a[l]
        l += 1
        r -= 1
        while l <= end and a[l] <= pivot:
            l += 1
        while r >= start and a[r] > pivot:
            r -= 1
    a[start], a[r] = a[r], a[start]
    return r

def _quick_sort_f(a: List, start, end):
    # todo
    if start >= end:
        return

    pivot_index = start
    left_index = start + 1
    right_index = end

    while left_index <= right_index:
        if a[left_index] > a[pivot_index] and a[right_index] < a[pivot_index]:
            a[left_index], a[right_index] = a[right_index], a[left_index]

        if a[left_index] <= a[pivot_index]:
            left_index += 1

        if a[right_index] >= a[pivot_index]:
            right_index -= 1

    a[pivot_index], a[right_index] = a[right_index], a[pivot_index]

    _quick_sort_f(a, start, right_index - 1)
    _quick_sort_f(a, right_index + 1, end)

def _quick_sort_r(a: List, start, end):
    # todo
    if start >= end:
        return

    pivot_index = random.randint(start, end)
    a[start], a[pivot_index] = a[pivot_index], a[start]

    left_index = start + 1
    right_index = end

    while left_index <= right_index:
        if a[left_index] > a[start] and a[right_index] < a[start]:
            a[left_index], a[right_index] = a[right_index], a[left_index]

        if a[left_index] <= a[start]:
            left_index += 1

        if a[right_index] >= a[start]:
            right_index -= 1

    a[start], a[right_index] = a[right_index], a[start]

    _quick_sort_r(a, start, right_index - 1)
    _quick_sort_r(a, right_index + 1, end)


def quick_sort(a: List, p=True):
    """
    sorts an ArrayList a using the quick sort algorithm.
    If parameter p is True, the quick sort algorithm uses a randomly chosen element from a as pivot.
    Otherwise, the quick sort algorithm uses the first element as pivot.
    """
    if p:
        _quick_sort_r(a, 0, a.size() - 1)
    else:
        _quick_sort_f(a, 0, a.size() - 1)
