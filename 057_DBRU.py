#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Constructing a De Bruijn Graph
Rosalind ID: DBRU
Rosalind #: 057
URL: http://rosalind.info/problems/dbru/
'''

from string import maketrans

def ReverseComplementDNA(dna):
	'''Returns the reverse complement of a given DNA strand.'''
	transtab = maketrans('ATCG', 'TAGC')
	return dna.translate(transtab)[::-1]

with open('data/rosalind_dbru.txt') as input_data:
	k_mers = [line.strip() for line in input_data.readlines()]

# Get the edge elements.
DBG_edge_elmts = set()
for kmer in k_mers:
	DBG_edge_elmts.add(kmer)
	DBG_edge_elmts.add(ReverseComplementDNA(kmer))

# Create the edges.
k = len(k_mers[0])
edge = lambda elmt: '('+elmt[0:k-1]+', '+elmt[1:k]+')'
DBG_edges = [edge(elmt) for elmt in DBG_edge_elmts]

# Write and save the adjacency list.
print '\n'.join(DBG_edges)
with open('output/057_DBRU_output.txt','w') as output_file:
	output_file.write('\n'.join(DBG_edges))
	
# Second solution.

def adjacency(dna_list):
	dna_set = set(dna_list + [ReverseComplementDNA(dna) for dna in dna_list])
	return [(dna[:-1], dna[1:]) for dna in dna_set]
	
with open('data/rosalind_dbru.txt') as input_data:
	k_mers = input_data.read().strip().split('\n')

print '\n'.join("({kmer1}, {kmer2})".format(kmer1=x, kmer2=y) for (x,y) in adjacency(k_mers))