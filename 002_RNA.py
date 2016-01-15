#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Transcribing DNA into RNA
Rosalind ID: RNA
Rosalind #: 002
URL: http://rosalind.info/problems/rna/
'''

'''First Solution'''

seq = open('rosalind_rna.txt','r')
seq = seq.read()

print(seq.replace('T','U'))

with open('002_RNA_output.txt', 'w') as output_data:
        output_data.write(print (seq.replace('T','U'))
