#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Point Mutations
Rosalind ID: HAMM
Rosalind #: 006
URL: http://rosalind.info/problems/hamm/
'''

'''First Solution'''

with open('rosalind_hamm.txt') as input_data:
	s,t = input_data.readlines()
	s = s.rstrip()
	t = t.rstrip()

def diff_letters(a,b):
	return sum ( a[i] != b[i] for i in range(len(a)))
	
diff_letters(s,t)
