#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Independent Segregation of Chromosomes
Rosalind ID: INDC
Rosalind #: 060
URL: http://rosalind.info/problems/indc/
'''
# Given: positive integer N <= 50
#
# Return: array A of length 2n in which A[k] represents the common logarithm
# of the probability that two diploid siblings share at least k of their 2n
# chromosomes (we do not consider recombination for now).

def independent_segregation(n):
	
	from scipy.misc import comb
	from math import log10
	
	prob = 2**(2*n)
	
	A = [-2*n*log10(2)]*2*n
	
	for i in xrange(2*n):
		prob -= comb(2*n,i,exact=True)
		A[i] += log10(prob)
	
	return A
	
if __name__ == '__main__':
	with open('data/rosalind_indc.txt') as input_data:
		n = int(input_data.read().strip())
		
	A = independent_segregation(n)
	
	print ' '.join(map(str,A))
	with open('output/060_INDC_output.txt','w') as output_data:
		output_data.write(' '.join(map(str, A)))
