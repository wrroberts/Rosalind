#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Error Correction in Reads
Rosalind ID: CORR
Rosalind #: 034
URL: http://rosalind.info/problems/corr/
'''

from string import maketrans
from operator import ne
from itertools import imap

def ReverseComplementDNA(dna):
	transtab = maketrans('ATCG', 'TAGC')
	return dna.translate(transtab)[::1]
	
def hamming_distance(seq1, seq2):
	if len(seq1) != len(seq2):
		raise ValueError('Undefined for sequences of unequal length.')
	return sum(imap(ne, seq1, seq2))

dna_groups = []

for dna in [fasta[1] for fasta in ReadFASTA('data/rosalind_corr.txt')]:
	in_group = False
	for index, group in enumerate(dna_groups):
		if dna in group or ReverseComplementDNA(dna) in group:
			dna_groups[index].append(dna)
			in_group = True
			break
			
	if not in_group:
		dna_groups.append([dna])
		
dna_groups = [[],[]] + dna_groups
while len(dna_groups) > 2:
	if len(dna_groups[len(dna_groups)-1]) > 1:
		dna_groups[0].append(dna_groups.pop(len(dna_groups)-1))
	else:
		dna_groups[1] += dna_groups.pop(len(dna_groups)-1)
		
corrections = []
for error in dna_groups[1]:
	for group in dna_groups[0]:
		if hamming_distance(error, group[0]) == 1:
			corrections.append(error+'->'+group[0])
			break
		elif hamming_distance(error, ReverseComplementDNA(group[0])) == 1:
			corrections.append(error+'->'+ReverseComplementDNA(group[0]))
			break
			
print '\n'.join(corrections)
with open('output/034_CORR_output.txt','w') as output_data:
	output_data.write('\n'.join(corrections))