#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Complementing a Strand of DNA
Rosalind ID: REVC
ROSALIND #: 003
URL: http://rosalind.info/problems/revc/
'''

'''First Solution'''

seq = open('rosalind_rna.txt','r')
seq = seq.read()

from Bio.Seq import Seq
seq1 = Seq(seq)
print seq1.reverse_complement()

'''Second Solution'''

st = open('rosalind_rna.txt','r')
st = seq.read()

st = st.replace('A','t').replace('T','a').replace('C','g').replace('G','c').upper()[::-1]
print st

with open('003_REVC_output.txt', 'w') as output_data:
        output_data.write(st)
