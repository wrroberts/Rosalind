#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Consensus and Profile
Rosalind ID: SUBS
Rosalind #: 009
URL: http://rosalind.info/problems/subs/
'''

'''ReadFasta'''

import urllib
import contextlib

def ReadFasta(data_location):
    if type(data_location) == list:
        fasta_list =[]
        for location in data_location:
            fasta_list += ReadFasta(location)
        return fasta_list
    if data_location[-4:] == '.txt':
        with open(data_location) as f:
            return ParseFasta(f)
    elif data_location[0:4] == 'http':
        with contextlib.closing(urllib.urlopen(data_location)) as f:
            return ParseFasta(f)
        
def ParseFasta(f):
    fasta_list=[]
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

'''First Option'''

from numpy import zeros

dna_list = ReadFasta('rosalind_cons.txt')

M = zeros((4,len(dna_list[0][1])),dtype=int)
snp_dict = {'A':0,'C':1,'G':2,'T':3}
for dna in dna_list:
	for index,snp in enumerate(dna[1]):
		M[snp_dict[snp]][index] += 1
		
consensus = ''
to_snp = {0:'A',1:'C',2:'G',3:'T'}
for i in range(0,len(dna_list[0][1])):
    maxval = [-1,-1]
    for j in range(0,4):
        if maxval[1] < M[j][i]:
            maxval = [j,M[j][i]]
    consensus += to_snp[maxval[0]]

consensus = [consensus, 'A:','C:','G:','T:']
for index,col in enumerate(M):
    for val in col:
        consensus[index+1] += ' '+str(val)
        
print '\n'.join(consensus)
with open('010_CONS.txt','w') as output_data:
    output_data.write('\n'.join(consensus))
