#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: k-Mer Composition
Rosalind ID: KMER
Rosalind #: 036
URL: http://rosalind.info/problems/kmer/
'''

from itertools import product

dna = ReadFASTA('data/rosalind_kmer.txt')[0][1]

kmer_list = [''.join(kmer) for kmer in list(product(('ACGT', repeat=4)))]

kmer_count = [0]*(4**4)

for i in range(len(dna)-3):
	kmer_count[kmer_list.index(dna[i:i+4])] += 1
	
print ' '.join(map(str,kmer_count))
with open('output/036_KMER_output.txt','w') as output_data:
	output_data.write(' '.join(map(str,kmer_count)))
	
	