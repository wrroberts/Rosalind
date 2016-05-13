#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Creating a Character Table from Genetic Strings
Rosalind ID: CSTR
Rosalind #: 066
URL: http://rosalind.info/problems/cstr/
'''

def char_table_from_strings(dna_list):
	ch_table = set()
	for i, ch in enumerate(dna_list[0]):
		ch_array = [int(dna[i] == ch) for dna in dna_list]
		if 1 < sum(ch_array) < len(dna_list)-1:
			ch_table.add(''.join(map(str,ch_array)))
			
	return ch_table
	
def main():
	with open('data/rosalind_cstr.txt') as input_data:
		dna_list = [line.strip() for line in input_data.readlines()]
		
	character_table = char_table_from_strings(dna_list)
	
	print '\n'.join(character_table)
	with open('output/066_CSTR_output.txt','w') as output_data:
		output_data.write('\n'.join(character_table))
		
if __name__ == '__main__':
	main()
	
# Second solution

with open('data/rosalind_cstr.txt') as input_data:
	dna_list = [line.strip() for line in input_data.readlines()]
	
for i in xrange(len(dna_list[0]):
	nucleotides = [ seq[i] for seq in dna_list ]
	non_trivial = len([True for c in 'ACTG' if nucleotides.count(c) > 1]) > 1
	if non_trivial:
		print ''.join([('1' if seq[i] == dna_list[0][i] else '0') for seq in dna_list])
		
		