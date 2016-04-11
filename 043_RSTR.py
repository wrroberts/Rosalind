#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Matching Random Motifs
Rosalind ID: RSTR
Rosalind #: 043
URL: http://rosalind.info/problems/rstr/
'''

with open('data/rosalind_rstr.txt') as input_data:
	N, gc_content, dna = input_data.read().strip().split()
	N = int(N)
	gc_content = float(gc_content)
	
codon_count = [0,0]
for codon in dna:
	if codon in ['C','G']:
		codon_count[0] += 1
	elif codon in ['A','T']:
		codon_count[1] += 1
		
dna_prob = ((0.5*gc_content)**codon_count[0])*((0.5*(1-gc_content))**codon_count[1])

prob = 1 - (1-dna_prob)**N

print prob
with open('output/043_RSTR_output.txt','w') as output_data:
	output_data.write(str(prob))
