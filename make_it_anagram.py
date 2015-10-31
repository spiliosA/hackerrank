#https://www.hackerrank.com/challenges/make-it-anagram/submissions/code/14911631

sentinel = '' # ends when this string is seen
x = []
try:
    for line in iter(raw_input, sentinel):
        x.append(line)
except EOFError:
    pass

if len(x[0]) > len(x[1]) :
    wordA = x[0]
    wordB = x[1]
else :
    wordA = x[1]
    wordB = x[0]

cnt = 0
for i in range (0,len(wordB)):
    posA = wordA.find(wordB[i])
    if posA > -1:
        wordA = wordA[:posA] + wordA[(posA+1):]
        cnt+=1

print len(wordA) + len(wordB) - cnt
