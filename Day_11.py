'''
Objective:
    Today, we are building our knowledge of arrays by adding another 
    dimension. Check out the tutorial tab for learning materials and an
    instructional video.

Context:
    Given a 6 x 6 2D Array, A:
        1 1 1 0 0 0
        0 1 0 0 0 0
        1 1 1 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
        0 0 0 0 0 0
    We define an hourglass in A to be the subset of values with indicies
    a b c
      d
    e f g
    There are 16 hour in A, and an hourglass sum is the sum of hourglass'
    values.

Task:
    Calculate the hourglass sum for every hourglass in A, then print the
    maximum hourglass sum.

Example:
    In the array shown above, the maximum hourglass sum is 7 for the 
    hourglass in the top left corner.

Input Format:
    There are 6 lines of input, where each line contains 6 space-separated
    integers that describe the 2D Array A.

Constraints:
    -9 <= A[i][j] <= 9
    0 <= i, j, <= 5

Output Format:
    19

Explanation:
    A contains the following hourglasses:
        111 110 100 000
         0   0   0   0
        111 110 100 000

        010 100 000 000
         1   1   0   0
        002 024 244 440

        111 110 100 000
         0   2   4   4
        000 002 020 200

        002 024 244 440
         0   0   2   0
        001 012 124 240
    
    The hourglass with the maximum sum (19) is:
        2 4 4
          2
        1 2 4  
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    res = []
    for x in range(0, 4):
        for y in range(0, 4):
            s = sum(arr[x][y:y+3]) + arr[x+1][y+1] + sum(arr[x+2][y:y+3])
            res.append(s)
    print(max(res))