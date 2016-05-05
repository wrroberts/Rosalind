#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Wobble Bonding and RNA Secondary Structures
Rosalind ID: RNAS
Rosalind #: 064
URL: http://rosalind.info/problems/rnas/
'''

def wobble_bonding(rna):
	'''Returns the number of noncrossing bonding graphs for a given RNA sequence.'''
	if len(rna) <= 3:
		return 1
	
	else:
		if rna in wobble_dict:
			return wobble_dict[rna]
			
		else:
			subintervals = []
			for i in xrange(4, len(rna)):
				if rna[0] in matchings[rna[i]]:
					subintervals.append([rna[1:i],rna[i+1:]])
					
			wobble_dict[rna] = (sum([wobble_bonding(subint[0])*wobble_bonding(subint[1]) for subint in subintervals]) + wobble_bonding(rna[1:]))
			
			return wobble_dict[rna]
			
with open('data/rosalind_rnas.txt') as input_data:
	rna = input_data.read().strip()
	
matchings = {'A':'U', 'U':'AG', 'C':'G', 'G':'CU'}
wobble_dict = {}
wobble = wobble_bonding(rna)

print wobble
with open('output/064_RNAS_output.txt','w') as output_file:
	output_file.write(str(wobble))
