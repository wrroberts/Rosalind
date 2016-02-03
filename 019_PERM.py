#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Enumerating Gene Orders
Rosalind ID: PERM
Rosalind #: 19
URL: http://rosalind.info/problems/perm/
'''

#First Solution

from itertools import permutations

def factorial(n):
	if n < 2:
		return 1
	else:
		return n*factorial(n-1)

with open('data/rosalind_perm.txt') as input_data:
	perm_set = range(1,int(input_data.read())+1)

perm_list = map(list,list(permutations(perm_set)))

with open('output/019_PERM_output.txt','w') as output_data:
	output_data.write(str(factorial(len(perm_set))))
	for permutation in perm_list:
		output_data.write('\n'+' '.join(map(str,permutation)))
