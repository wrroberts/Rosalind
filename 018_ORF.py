#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Open Reading Frames
Rosalind ID: ORF
Rosalind #: 018
URL: http://rosalind.info/problems/orf/
'''

ReadFAST
ReverseComplementDNA
ProteinDictDNA

#ReadFASTA
import urllib
import contextlib

def ReadFASTA(data_location):
	if type(data_location) == list:
		fasta_list = []
		for location in data_location:
			fasta_list += ReadFASTA(location)
		return fasta_list
	if data_location[-4:] == '.txt':
		with open(data_location) as f:
			return ParseFASTA(f)
	elif data_location[0:4] == 'http':
		with contextlib.closing(urllib.urlopen(data_location)) as f:
			return ParseFASTA(f)

def ParseFASTA(f):
	fasta_list = []
	for line in f:
		if line[0] == '>':
			try:
				fasta_list.append(current_dna)
			except UnboundLocalError:
				pass
			current_dna = [line.lstrip('>').rstrip('\n'),'']
		else:
			current_dna[1] += line.rstrip('\n')
	fasta_list.append(current_dna)
	return fasta_list

#ReverseComplementDNA
from string import maketrans

def ReverseComplementDNA(dna):
	transtab = maketrans('ATCG','TAGC')
	return dna.translate(transtab)[::-1]

#ProteinDictDNA
def ProteinDictDNA():
	with open('Dictionaries/codon_table_dna.txt') as input_data:
		dna_to_protein = [line.strip().split() for line in input_data.readlines()]
	dna_dict = {}
	for translation in dna_to_protein:
		dna_dict[translation[0]] = translation[1]
	return dna_dict

#Open Reading Frames
dna_list = [ReadFASTA('data/rosalind_orf-1.txt')[0][1]]
dna_list.append(ReverseComplementDNA(dna_list[0]))
dna_dict = ProteinDictDNA()

protein_orf = set()
for dna in dna_list:
	for i in range(len(dna)-2):
		if dna[i:i+3] == 'ATG':
			j = i
			current_protein = ''
			while j+3 < len(dna)-1:
				if dna_dict[dna[j:j+3]] == 'Stop':
					protein_orf.add(current_protein)
					break
				else:
					current_protein += dna_dict[dna[j:j+3]]
				j += 3

protein_orf = map(str,protein_orf)

print '\n'.join(protein_orf)
with open('output/018_ORF_output.txt','w') as output_data:
	output_data.write('\n'.join(protein_orf))
	