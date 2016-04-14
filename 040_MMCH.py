#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Maximum Matching and RNA Secondary Structures
Rosalind ID: MMCH
Rosalind #: 040
URL: http://rosalind.info/problems/mmch/
'''

from math import factorial

def nPr(n, k):
	return factorial(n)/factorial(n-k)
	
rna = ReadFASTA('data/rosalind_mmch.txt')[0][1]

AU_nom = [rna.count(nucleotide) for nucleotide in 'AU']
GC_num = [rna.count(nucleotide) for nucleotide in 'GC']

max_matchings = nPr(max(AU_num), min(AU_num))*nPr(max(GC_num), min(GC_num))

print max_matchings
with open('output/040_MMCH_output.txt','w') as output_data:
	output_data.write(str(max_matchings))
