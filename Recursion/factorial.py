#!/usr/env/bin python3

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)