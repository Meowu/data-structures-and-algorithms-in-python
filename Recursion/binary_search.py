#!/usr/bin/env python3


def binary_search(data, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(data)
    if low > high:
        return False
    mid = (low + high) // 2
    if target == data[mid]:
        return True
    elif target > data[mid]:
        return binary_search(data, target, mid + 1, high)
    else:
        return binary_search(data, target, low, mid - 1)


if __name__ == "__main__":
    items = [1, 4, 5, 7, 12, 23, 34, 35, 46]
    binary_search(items, 12)
