#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Subsets
Rosalind ID: SSET
Rosalind #: 044
URL: http://rosalind.info/problems/sset/
'''

with open('data/rosalind_sset.txt') as input_data:
	n = int(input_data.read().strip())

sset = 1
for i in xrange(n):
	sset = (sset*2)%1000000
	
print sset
with open('output/044_SSET_output.txt','w') as output_data:
	output_data.write(str(sset))

#Alternate solution

sset = pow(2,n,1000000)

print sset
