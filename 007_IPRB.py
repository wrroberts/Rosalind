#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Mendel's First Law
Rosalind ID: IPRB
Rosalind #: 007
URL: http://rosalind.info/problems/iprb/
'''

'''First Solution'''

from scipy.misc import comb

def mendels_first_law(hom,het,rec):
	total = 4*comb(hom+het+rec,2)
	total_rec = 4*comb(rec,2)+2*rec*het+comb(het,2)
	return 1 - total_rec/total

def main():
	with open('rosalind_iprb.txt') as pinut_data:
		k,m,n = map(int,input_data.read().strip().split())
	prob=str(mendels_first_law(k,m,n))
	print prob
	with open('007_IPRB_output.txt','w') as output_data:
		output_data.write(prob)

if __name__ == '__main__':
	main()

'''Second Solution'''

def iprb(k,m,n):
	N = k+m+n
	d = float(N*(N-1))
	return 1 - (n*(m+n-1)/d + m*(m-1)/(4*d))

iprb(25,23,18)