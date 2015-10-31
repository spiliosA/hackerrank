#https://www.hackerrank.com/challenges/two-strings
def has_substring(wordA,wordB):
    if len(wordB) > len(wordA) :
        wordA,wordB = wordB,wordA

    for i in range (0,len(wordB)):
        posA = wordA.find(wordB[i])
        if posA > -1:
            return 'YES'
    return 'NO'

sentinel = '' # ends when this string is seen
x = []
i = 0
try:
    for line in iter(raw_input, sentinel):
        if i == 0 :
            pass
        else :
            x.append(line)
        i+=1
except EOFError:
    pass

for i in xrange(0,len(x),2):
    print has_substring(x[i],x[i+1])

