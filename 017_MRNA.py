#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Inferring mRNA from Protein
Rosalind ID: MRNA
Rosalind #: 017
URL: http://rosalind.info/problems/mrna/
'''

#First Solution

# Protein Dictionary
def ProteinDictRNA():
	with open('Dictionaries/codon_table_rna.txt') as input_data:
		rna_to_protein = [line.strip().split() for line in input_data.readlines()]
	rna_dict = {}
	for translation in rna_to_protein:
		rna_dict[translation[0]] = translation[1]
	return rna_dict
	
with open('data/rosalind_mrna.txt') as input_data:
	protein = input_data.read().strip()
rna_dict = ProteinDictRNA()
rna_num = rna_dict.values().count('Stop')

for p in protein:
	rna_num = rna_num * rna_dict.values().count(p) % 1000000

print rna_num

#Second Solution
from Bio.Data import CodonTable as ct

ftab = ct.standard_rna_table
rtab = {}
for codon in ftab.forward_table:
    aa = ftab.forward_table[codon]
    if aa in rtab:
        rtab[aa] += 1
    else:
        rtab[aa] = 1
prot = open('data/rosalind_mrna.txt','r').readline().strip()

x = 1
for aa in prot: x *= rtab[aa]
print (x*3)%1000000
