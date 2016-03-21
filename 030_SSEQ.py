#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding a Spliced Motif
Rosalind ID: SSEQ
Rosalind #: 030
URL: http://rosalind.info/problems/sseq/
'''

dna, sub_seq = [fasta[1] for fasta in ReadFASTA('data/rosalind_sseq.txt')]

sseq_indicies, i = [], 0
for nucleotide in sub_seq:
	while dna[i] != nucleotide:
		i += 1
	sseq_indicies.append(str(i+1))
	i += 1

print ' '.join(sseq_indicies)
with open('output/030_SSEQ.txt','w') as output_data:
	output_data.write(' '.join(sseq_indicies))