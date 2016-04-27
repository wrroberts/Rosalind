#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Motzkin Numbers and RNA Secondary Structures
Rosalind ID: MOTZ
Rosalind #: 048
URL: http://rosalind.info/problems/motz/
'''

def Noncrossing(rna):
	'''Returns the number of noncrossing bonding graphs for a given RNA sequence.'''
	if len(rna) <= 1:
		return 1
		
	else:
		if rna in noncross_dict:
			return noncross_dict[rna]
		
		else:
			subintervals = []
			for i in xrange(1, len(rna)):
				if rna[0] == matchings[rna[i]]:
					subintervals.append([rna[1:i],rna[i+1:]])
					
			noncross_dict[rna] = (sum([Noncrossing(subint[0])*Noncrossing(subint[1]) for subint in subintervals]) + Noncrossing(rna[1:])) % 1000000
			
			return noncross_dict[rna]
			
rna = ReadFASTA('data/rosalind_motz.txt')[0][1]
matchings = {'A':'U', 'U':'A', 'C':'G', 'G':'C'}
noncross_dict = {}
noncross = Noncrossing(rna)

print noncross
with open('output/048_MOTZ_output.txt','w') as output_file:
	output_file.write(str(noncross))
