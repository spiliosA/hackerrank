# https://www.hackerrank.com/challenges/anagram

from math import *

def is_anagram(word):
    ret_val = 0
    w_len = len(word)
    if w_len%2 != 0 :
        return -1
    else :
        wordA = word[:w_len/2]
        wordB = word[w_len/2:]
        for i in range(0,(w_len/2)):
            pos = wordB.find(wordA[i])
            if   pos > -1:
                wordB = wordB[:pos] + wordB[(pos+1):]

    return len(wordB)
                


sentinel = '' # ends when this string is seen
i = 0
x = []
try:
    for line in iter(raw_input, sentinel):
        if i == 0 :
            pass
        else :
            print is_anagram(str(line))
        i+=1
except EOFError:
    pass
