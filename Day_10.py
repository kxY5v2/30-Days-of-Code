'''
Objective:
    Today, we're working with binary numbers. Check out this tutorial
    tab for learning materials and an instructional video!

Task:
    Given a base-10 integer, n, convert it to binary (base-2). Then find and print
    the base-10 integer denoting the maximum number of consecutive 1's in n's binary
    representation. When working with different bases, it is common to show 
    the base as a subscript.

Example:
    n = 125
    The binary representation of 125(10) is 1111101(2). In base 10, there are 5 and 1 
    consecutive ones in two groups. Print the maximum, 5.

Input Format:
    A single integer n
Constraints:
    1 <= n <= 10^6

Output Format:
    Print a single base-10 integer that denotes the maximum number of consecutive 1's in the
    binary representation of n.

Sample Input 1:
    5
Sample Output 1:
    1

Sample Input 2:
    13
Sample Output 2:
    2

Explanation:
    Sample Case 1:
        The binary representation of 5(10) is 101(2), so the maximum number of consecutive
        1's is 1.
    Sample Case 2:
        The binary representation of 13(10) is 1101(2), so the maximum number of consecutive
        1's is 2.
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    # Convert to base-2
    bin_n = "{0:b}".format(n)

    # Split to sections of continuous 1's
    split_n = re.split("0+", bin_n)
    
    # Find largest number of continuous 1's
    highest_ones = max(split_n)

    # Find the length (number of digits) of in-a-row ones
    num_ones = len(highest_ones)

    print(num_ones)
