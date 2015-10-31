#!/usr/bin/env python

# read input

def search_letters(wordA,wordB,score) :
	max_score=0
	for c in wordA:
		score=0
		pos = wordB.find(c)
		if pos > -1 :
			print "Letter matched"
			score+=1
			search_letters(wordA[1:],wordB[pos:],score)
			
			
			
	if score>max_score:
		max_score=score
	return max_score

print search_letters('ABCDEF','FBDAMN',0)
