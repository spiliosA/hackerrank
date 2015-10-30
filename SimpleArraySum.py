# https://www.hackerrank.com/challenges/simple-array-sum
#Problem Statement
#You are given an array of integers of size N. Can you find the sum of the elements in the array?

#Input
# The first line of input consists of an integer N. The next line contains N space-separated integers representing the array elements.
# Sample: 
#  6
#  1 2 3 4 10 11
#
#
#Output
# Output a single value equal to the sum of the elements in the array.
# For the sample above you would just print 31 since 1+2+3+4+10+11=31.

sentinel = '' # ends when this string is seen
try:
    for line in iter(raw_input, sentinel):
        x = line
except EOFError:
    pass

a = map(int,x.split())
print sum(a)
