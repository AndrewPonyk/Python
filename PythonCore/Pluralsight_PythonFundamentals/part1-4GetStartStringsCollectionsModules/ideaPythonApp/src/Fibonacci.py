import sys

__author__ = 'andrii'

def fib(n):
    if n > 1:
        return fib(n-2) + fib(n-1);
    return n;

print(fib(4));