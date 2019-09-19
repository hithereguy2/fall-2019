"""
Program: bisection_sqrt_list.py
This program uses a binary search algorithm to calculate the square root
of a non-negative integer.

Users are prompted to input a list of numbers separated by a space.
The resulting sqrt approximations are printed to the console.

Reference:  https://www.wikiwand.com/en/Binary_search_algorithm.
"""

import math


input_str = input('Enter list of numbers:')
input_list = input_str.split()
numbers = [ int(x) for x in input_list ]

for x in input_listnumbers:
    # Do Binary Search for floor(sqrt(x)) 
    start = 1
    end = x
    ans = 0
    while (start <= end) : 
        # Base cases (b)
        if (x == 0 or x == 1) : 
            ans = x
            break

        mid = (start + end) // 2

        # If x is a perfect square 
        if (mid*mid == x) : 
            ans = mid
            break 

        # Since we need floor, we update  
        # answer when mid*mid is smaller 
        # than x, and move closer to sqrt(x) 
        if (mid * mid < x) : 
            start = mid + 1
            ans = mid 

        else : 
            # If mid*mid is greater than x 
            end = mid-1

    if ans**2 == x:
        print(f"The exact square root of {x} is {ans}\n")
    else:
        print(f"The approximate square root of {x} is {ans} and the exact value is  {math.sqrt(x)}")
        print (f'The error is {((math.sqrt(x)-ans)/math.sqrt(x))*100:.2f}%\n')
