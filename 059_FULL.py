#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Inferring Peptide from Full Spectrum
Rosalind ID: FULL
Rosalind #: 059
URL: http://rosalind.info/problems/full/
'''

def ProteinWeightDict():
	'''Returns a dictionary that translates Protein to Monoisotopic Mass.'''
	
	with open('data/protein_mass_table.txt') as input_data:
		protein_weight_dict = {line.strip().split()[0]:float(line.strip().split()[1]) for line in input_data.readlines()}
		
	return protein_weight_dict

def find_weight_match(current_w, w_list):
	for weight in w_list:
		for item in ProteinMatchDict().items():
			if abs(item[1] - (weight - current)) < 0.01:
				return item[0]
				
	return -1
	
if __name__ == '__main__':
	with open('data/rosalind_full.txt') as input_data:
		weights = [float(line.strip()) for line in input_data.readlines()]
		
	# Given that len(weights) = 2n+3
	n = (len(weights)-3)/2
	
	# Initialize the variables
	protein = ''
	current = weights[1]
	myw = [w for w in weights[2:]]
	
	# Iteratively build the protein
	while len(protein) < n:
		temp = find_weight_match(current, myw)
		if temp == -1:
			break
		else:
			protein += temp
			current += ProteinWeightDict()[temp]
			myw = filter(lambda w: w-current > 0, myw)
			
	print protein
	with open('output/059_FULL_output.txt','w') as output_file:
		output_file.write(protein)