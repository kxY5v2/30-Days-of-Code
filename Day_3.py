'''
Objective:
    In this challenge, we learn about conditional statements. Check out 
    the Tutorial tab for learning materials and an instructional video.

Task:
    Given an integer, n, preform the following conditional actions:
        If n is odd, print Weird.
        If n is even and in the inclusive range 2 to 5, print Not Weird.
        If n is even and in the inclusice range of 6 to 20, print Weird
        If n is even and greater than 20, print Not Weird
        Complete the stub code provided in your editor to print whether
        or not n is weird.

Input Format:
    A single line containing a positive integer n.

Constraints:
    1 <= n <= 100

Output Format:
    Print Weird if the number is weird; otherwise, print Not Weird

Sample Input 0:
    3
Sample Output 0:
    Weird
Sample Input 1:
    24
Sample Output 1:
    Not Weird

Explanation:
    Sample Case 0: n=3
    n is odd and odd numbers are weird, so we print weird.
    Sample Case 1: n=24
    n > 30 and n is even so it is not weird. Thus we print Not Weird
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())
    
    if(N % 2 == 1):
        # N is odd
        print('Weird')
    else:
        if N > 20:
            print('Not Weird')
        elif N < 5 and N >= 2:
            print('Not Weird')
        else:
            print('Weird')
