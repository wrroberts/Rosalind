#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Expected Number of Restriction Sites
Rosalind ID: EVAL
Rosalind #: 047
URL: http://rosalind.info/problems/eval/
'''

with open('data/rosalind_eval.txt') as input_data:
	n, dna, gc_content = intput_data.readlines()
	n = int(n.strip())
	dna = dna.strip()
	gc_content = map(float, gc_content.split())
	
codon_count = [dna.count('C')+dna.count('G'), dna.count('A')+dna.count('T')]

substring_slots = n - len(dna) + 1

expected substrings = []
for gc_value in gc_content:
	dna_prob = ((0.5*gc_value)**codon_count[0])*((0.5*(1-gc_value))**codon_count[1])
	expected_substrings.append(str(dna_prob*substring_slots))
	
print ' '.join(expected_substrings)
with open('output/047_EVAL_output.txt','w') as output_data:
	output_data.write(' '.join(expected_substrings))