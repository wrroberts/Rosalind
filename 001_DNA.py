#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting DNA Nucleotides
Rosalind ID: DNA
Rosalind #: 001
URL: http://rosalind.info/problems/dna/
'''

'''First Solution'''

dnafile = 'rosalind_dna.txt'
file = open(dnafile,'r').readlines()
temp = ''.join(file)

totalA = temp.count('A')
totalC = temp.count('C')
totalG = temp.count('G')
totalG = temp.count('T')

print str(totalA),
print str(totalC),
print str(totalG),
print str(totalT)

'''Second Solution'''

seq = open('rosalind_dna.txt','r')
seq = seq.read()

countA = 0
countC = 0
countG = 0
countT = 0

for n in seq:
    if n =='A':
        countA += 1
    if n == 'C':
        countC += 1
    if n == 'G':
        countG += 1
    if n == 'T':
        countT += 1

print str(countA),
print str(countC),
print str(countG),
print str(countT)

'''Third Solution'''

from collections import Counter

seq = open('rosalind_dna.txt','r')
seq = seq.read()
c = Counter(seq)
print c['A'], c['C'], c['G'], c['T']
