#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Introduction to Set Operations
Rosalind ID: SETO
Rosalind #: 051
URL: http://rosalind.info/problems/seto/
'''

with open('data/rosalind_seto.txt') as input_data:
	S,A,B = input_data.readlines()
	
	S = set( [i for i in xrange(1,int(S.strip())+1)])
	A = set(map(int, A.strip().rstrip('}').lstrip('{').replace(' ','').split(',')))
	B = set(map(int, B.strip().rstrip('}').lstrip('{').replace(' ','').split(',')))
	
with open('output/051_SETO_output.txt','w') as output_data:
	# A union B
	output_data.write('{'+', '.join(map(str,list(A|B)))+'}'+'\n')
	#A intersect B
	output_data.write('{'+', '.join(map(str,list(A&B)))+'}'+'\n')
	# A - B
	output_data.write('{'+', '.join(map(str,list(A-B)))+'}'+'\n')
	# B - A
	output_data.write('{'+', '.join(map(str,list(B-A)))+'}'+'\n')
	# A complement
	output_data.write('{'+', '.join(map(str,list(S-A)))+'}'+'\n')
	# B complement
	output_data.write('{'+', '.join(map(str,list(S-B)))+'}')
