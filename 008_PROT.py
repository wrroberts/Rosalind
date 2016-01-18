#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Translating RNA into Protein
Rosalind ID: PROT
Rosalind #: 008
URL: http://rosalind.info/problems/prot/
'''

'''First Solution'''

from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

with open('rosalind_prot.txt','r') as input:
	mrna = input.read()

messenger_rna = Seq(mrna,IUPAC.unambiguous_rna)

print messenger_rna.translate()
