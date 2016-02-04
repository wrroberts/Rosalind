#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Enumerating k-mers lexicographically
Rosalind ID: LEXF
Rosalind #: 023
URL: http://rosalind.info/problems/lexf/
'''

#First Solution
from itertools import product

with open('data/rosalind_lexf.txt') as input_data:
	letters,n = input_data.readlines()
	letters = ''.join(letters.split())
	n = int(n)

k_mers = [''.join(item) for item in product(letters,repeat=n)]

with open('output/023_LEXF_output.txt','w') as output_file:
	output_file.write(k_mers[0])
	for item in k_mers[1:]:
		output_file.write('\n'+item)
		
#Second Solution
k = 4
str = 'L Q K U'
k_mer = alphabet

for l in range(k-1):
	k_mer = [i+j for i in alphabet for j in k_mer]
for i in k_mer: print i

#Third Solution
from itertools import product
handle = open('data/rosalind_lexf.txt','rU')
dna = handle.readline().split()
n = int(handle.readline().strip())
combs = list(product(dna,repeat=n))
print "\n".join(["".join(x) for x in combs])
