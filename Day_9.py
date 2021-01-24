'''
Objective:
    Today we are learning about an algorithmic concept called recursion.
    Check out the Tutorial tab for learning materials and an instructional
    video.

Recursive Method for Calculating Factorial:
    factorial(n) = {1                  N <= 1
                    N * factorial(n-1) otherwise
                    }

Function Description:
    Complete the factorial function in the editor below. Be sure to
    use recursion. Factorial has the following parameter.
    int n: an integer
Returns:
    int: the factorial of n
Note:
    If you fail to use recursion or fail to name your recursive function
    factorial or Factorial, you will get a score of 0.

Input Format:
    A single integer, n (the argument to pass to factorial)

Constraints:
    2 <= n <= 12
    Your submission must contain a recursive function named factorial

Sample Input:
    3
Sample Output:
    6

Explanation:
    Consider the following steps. After the recursive calls from 1 to 3
    results are accumulated from step 3 to 1
        1. factorial(3) = 3 * factorial(2) = 3 * 2 = 6
        2. factorial(2) = 2 * factorial(1) = 2 * 1 = 2
        3. factorial(1) = 1
'''

import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

if __name__ == '__main__':
    n = int(input())
    result = factorial(n)
    print(result)