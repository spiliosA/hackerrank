#https://www.hackerrank.com/challenges/kaprekar-numbers/

import math

def is_kaprekar(k):
    if k ==1 :
        return 1

    i = 0
    po = str(int(math.pow(k,2)))
    while i < len(po)-1:
        head = po[:i+1]
        tail = po[i+1:]

        if int(head)+int(tail) == k:
            if int(tail) <> 0 :
                return 1
        i += 1
    return 0


x = []
try:
    for line in iter(raw_input, ''):
        x.append(int(line))
except EOFError:
    pass

ret_val = ""
for i in range(x[0],x[1]):
    if is_kaprekar(i) :
        ret_val += " " + str(i)

if ret_val == "":
    print "INVALID RANGE"
else :
    print ret_val[1:]

