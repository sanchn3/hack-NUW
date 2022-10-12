# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:45:20 2022

@author: sanch
Consider the divisors of 30: 1, 2, 3, 5, 6, 10, 15, 30. It can be seen that for each divisor d of 30, d + 30 / d is prime.

Find the sum of all positive integers n not exceeding 100,000,000 such that for every divisor d of n, d + n/d is prime.
"""
import sympy

def sum_of_prime_int_values(x):
    sum_ = 0 
    for d in range(1,x+1):
        val = ((d + x)/d)
        if val.is_integer():
            if sympy.isprime(int(val)):
                sum_ += val
    return sum_

while __name__ == "__main__":
    x = int(input("Enter 0 to quit\nSum of the Positive Integers such that for every divisor d of n, d + n/d is prime.\nEnter Value of n: "))
    if x == 0:break
    #x=30
    print("Sum of the Positive Integers such that for every divisor d of {0}, d + {0}/d is prime. \nSum = {1}".format(x,sum_of_prime_int_values(x)))