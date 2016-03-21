#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Ordering Strings of Varying Lengths Lexicographically
Rosalind ID: LEXV
Rosalind #: 039
URL: http://rosalind.info/problems/lexv/
'''

from itertools import product

with open('data/rosalind_lexv.txt') as input_data:
	A,n = [line.strip() for line in input_data.readlines()]
	A = ['*'] + A.split()
	n = int(n)

lexv = []
for item in product(A, repeat = n):
	if '*' not in item:
		lexv.append(''.join(item))
	
	else:
		for i in range(1,n):
		if ''.join(item[i:n]) == '*'*(n-i) and '*' not in item[:i]:
			lexv.append(''.join(item).replace('*',''))

with open('output/039_LEXV_output.txt','w') as output_data:
	output_data.write('\n'.join(lexv))