#https://www.hackerrank.com/challenges/palindrome-index/submissions/code/14912348
def is_palindrome(word):
    if word == word[::-1]:
        return 1

i = 0
try:
    for line in iter(raw_input, ''):
        if i == 0 :
            pass
        else :
            if is_palindrome(line) == 1:
                print -1
            else :
                for j in xrange(0,len(line)) :
                    if is_palindrome(line[:j] + line[(j+1):]) == 1:
                        print j
                        break
                
        i+=1
except EOFError:
    pass
