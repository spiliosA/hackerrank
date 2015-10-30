# https://www.hackerrank.com/challenges/angry-professor
# Problem Statement
# 
# The professor is conducting a course on Discrete Mathematics to a class of N students. He is angry at the lack of their discipline, and he decides to cancel the class if there are fewer than K students present after the class starts.
# 
# Given the arrival time of each student, your task is to find out if the class gets cancelled or not.
# 
# Input Format
# 
# The first line of the input contains T, the number of test cases. Each test case contains two lines.
# The first line of each test case contains two space-separated integers, N and K.
# The next line contains N space-separated integers, a1,a2,…,aN, representing the arrival time of each student.
# 
# If the arrival time of a given student is a non-positive integer (ai≤0), then the student enters before the class starts. If the arrival time of a given student is a positive integer (ai>0), the student enters after the class has started.
# 
# Output Format
# 
# For each testcase, print "YES" (without quotes) if the class gets cancelled and "NO" (without quotes) otherwise. 


sentinel = '' # ends when this string is seen

i = 0
x = []
try:
    for line in iter(raw_input, sentinel):
        if i == 0 :
            case_num = int(line)
        else :
            x.append(map(int,line.split()))
        i+=1
except EOFError:
    pass

for i in range(0,len(x),2):
    min     = int(x[i][1])
    on_time = sum(1 for number in x[i+1] if number <= 0)
    if on_time >= min :
        print "NO"
    else :
        print "YES"
