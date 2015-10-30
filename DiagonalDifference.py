# https://www.hackerrank.com/challenges/diagonal-difference
# Problem Statement

#You are given a square matrix of size N×N. Can you calculate the absolute difference of the sums across the two main diagonals?
# Input Format
#  The first line contains a single integer N. The next N lines contain the rows of N integers describing the matrix.
# Output Format
#  Output a single integer equal to the absolute difference in the sums across the diagonals.

# Sample Input
#  3
#  11 2 4
#  4 5 6
#  10 8 -12

# Sample Output
# 15

import math

def diagonalsum(m):
    return sum(m[i][i] for i in xrange(0, len(m)))

def revdiagonalsum(m):
    return sum(m[i][(len(m)-1)-i] for i in xrange(0, len(m)))

sentinel = '' # ends when this string is seen
i = 0
x = []
try:
    for line in iter(raw_input, sentinel):
        if i == 0 :
            pass
        else :
            x.append(map(int,line.split()))
        i+=1
except EOFError:
    pass

print abs(diagonalsum(x) - revdiagonalsum(x))
