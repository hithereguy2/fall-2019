# bisection_sqrt_list.py
import math
# Use input
input_list = [12, 100, 234, 123123123, 28397236511599]

for x in input_list:
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
