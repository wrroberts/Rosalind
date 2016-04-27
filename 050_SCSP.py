#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Interleaving Two Motifs
Rosalind ID: SCSP
Rosalind #: 050
URL: http://rosalind.info/problems/scsp/
'''

from numpy import zeros

def longest_common_subsequence(dna1, dna2):
	M = zeros((len(dna1)+1,len(dna2)+1))
	for i in xrange(len(dna1)):
		for j in xrange(len(dna2)):
			if dna1[i] == dna2[j]:
				M[i+1][j+1] = M[i][j]+1
			else:
				M[i+1][j+1] = max(M[i+1][j],M[i][j+1])
	
	longest_sseq = ''
	i,j = len(dna1), len(dna2)
	while i*j != 0:
		if M[i][j] == M[i-1][j]:
			i -= 1
		elif M[i][j] == M[i][j-1]:
			j -= 1
		else:
			longest_sseq = dna1[i-1] + longest_sseq
			i -= 1
			j -= 1
	
	return longest_sseq
	
with open('data/rosalind_scsp.txt') as input_data:
	dna1, dna2 = [line.strip() for line in input_data.readlines()]
	
lcsq = longest_common_subsequence(dna1, dna2)

superseq = ['']*(len(lcsq)+1)
dna1_index = dna2_index = 0

for i in xrange(len(lcsq)+1):
	if i == len(lcsq):
		superseq[len(lcsq)] = dna1[dna1_index:]+dna2[dna2_index:]
		superseq = ''.join(superseq)
	
	else:
		while dna1[dna1_index] != lcsq[i] and dna1_index < len(dna1):
			superseq[i] += dna1[dna1_index]
			dna1_index += 1
		while dna2[dna2_index] != lcsq[i] and dna2_index < len(dna2):
			superseq[i] += dna2[dna2_index]
			dna2_index += 1
		superseq[i] += lcsq[i]
		dna1_index += 1
		dna2_index += 1
		
print superseq
with open('output/050_SCSP_output.txt','w') as output_file:
	output_file.write(superseq)
