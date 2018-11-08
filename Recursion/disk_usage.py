#!/usr/bin/env python3


import os


# O(n)
def disk_usage(path):
    total = os.path.getsize(path)
    if os.path.isdir(path):
        for item in os.listdir(path):
            total += disk_usage(os.path.join(path, item))

    return total
