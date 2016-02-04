#!/usr/env/python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Partial Permutations
Rosalind ID: PPER
Rosalind #: 027
URL: http://rosalind.info/problems/pper/
'''

#First Solution
with open('data/rosalind_pper.txt') as f:
	n,k = map(int,f.read().split())

partial_perm = 1
for i in range(n-k+1,n+1):
	partial_perm = (partial_perm*i)%1000000
print partial_perm

#Second Solution
data = open('data/rosalind_pper.txt','r').readlines()[0].split(' ')
n,num = int(data[0]),1
for k in range(int(data[1])):
	num = num*(n-k)
print num%1000000

