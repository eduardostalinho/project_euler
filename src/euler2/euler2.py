# -*- coding: utf-8 -*-

def fibonacci():
    a, b = 0, 1
    fib = []
    while True:
        fib.append(b)
        a, b = b, a + b
        if b > 4000000:
            break;
    return fib

sum_of_evens_of_fib = sum([x for x in fibonacci() if x % 2 == 0])
