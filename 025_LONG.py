#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem title: Genome Assembly as Shortest Substring
Rosalind ID: LONG
Rosalind #: 025
URL: http://rosalind.info/problems/long/
'''

from scripts import ReadFASTA

def MergeMaxOverlap(str_list):
	max_length = -1
	for prefix_index in xrange(len(str_list)):
		for suffix_index in [num for num in range(len(str_list)) if num != prefix_index]:
			prefix, suffix = str_list[prefix_index], str_list[suffix_index]
			i = 0
			while prefix[i:] != suffix[0:len(prefix[i:])]:
				i += 1
			if len(prefix) -i > max_length:
				max_length = len(prefix) - i
				max_indicies = [prefix_index, suffix_index]
	return [str_list[j] for j in range(len(str_list)) if j not in max_indicies] + [str_list[max_indicies[0]] + str_list[max_indicies[1][max_length:]]

def LongestCommonSuperstring(str_list):
	while len(str_list) > 1:
		str_list = MergeMaxOverlap(str_list)
	return str_list[0]

if __name__ == '__main__':
	dna_list = [fasta[1] for fasta in ReadFASTA('data/rosalind_long.txt')]
	super_string = LongestCommonSuperstring(dna_list)
	print super_string
	with open('output/025_LONG.txt','w') as output_data:
		output_data.write(super_string)
