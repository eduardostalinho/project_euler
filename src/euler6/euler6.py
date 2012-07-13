# -*- coding: utf-8 -*-

def sum_of_squares(number):
    numbers = range(1, number + 1)
    return sum([(x ** 2) for x in numbers])

def square_of_sums(number):
    numbers = range(1, number + 1)
    return sum(numbers) ** 2

def difference(number):
    return abs(sum_of_squares(number) - square_of_sums(number))
