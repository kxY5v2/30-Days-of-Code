'''
Objective:
    Welcome to the last day! Today, we're discussing bitwise operations. 
    Check out the Tutorial tab for learning materials and an instructional 
    video!    

Task:
    Given set S = {1, 2, 3, ..., N}. Find two integers A and B (where A < B),
    from set S such that the value of A&B is the maximum possible
    adn also less than a given integer, K. In the case, & represents the bitwise
    AND operator.

Input Format:
    The first line contains an integer ,T, the number of test cases.
    Each of the T subsequent lines defines a test case as 2 space-separated integers
    N and K, respecitvely.

Constraints:
    1 <= T <= 10^30
    2 <= N <= 10^3
    2 <= K <= N

Output Format:
    For each test case, print the maximum possible value of A & B on a new line.

Sample Input:
    3
    5 2
    8 5
    2 2    

Sample Output:
    1
    4
    0

Explanation:
    N = 5, K = 2, S = {1, 2, 3, 4, 5}
    All possible values of A and B are:
        1. A = 1, B = 2; A & B = 0
        2. A = 1, B = 3; A & B = 1 
        3. A = 1, B = 4; A & B = 0
        4. A = 1, B = 5; A & B = 1
        5. A = 2, B = 3; A & B = 2
        6. A = 2, B = 4; A & B = 0 
        7. A = 2, B = 5; A & B = 0
        8. A = 3, B = 4; A & B = 0
        9. A = 3, B = 5; A & B = 1
        10. A = 4, B = 5; A & B = 4  
    The maximum possible value of A&B that is also < (K = 2)
    is 1, so we print 1 on a new line.    
'''

import math
import os
import random
import re
import sys

def max_bit(n, k):
    max = 0
    for i in range(1, n+1):
        for j in range(1, i):
            h = i & j
            if max < h < k:
                max = h
            if max == k - 1:
                return max
    return max

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        print(max_bit(n,k))
