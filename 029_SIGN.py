#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Enumerating Oriented Gene Orderings
Rosalind ID: SIGN
Rosalind #: 029
URL: http://rosalind.info/problems/sign/
'''

from itertools import product, permutations

with open('data/rosalind_sign.txt') as input_data:
	n = int(input_data.read())

signed_ints = []
for i in xrange(1,n+1):
	signed_ints.append([-1*i,i])

product_list = map(list,list(product(*signed_ints)))

signed_perm_list = []
for ordered_perm in product_list:
	signed_perm_list += map(list,list(permutations(ordered_perm)))

with open('output/029_SIGN_output.txt','w') as output_data:
	output_data.write(str(len(signed_perm_list)))
	for signed_perm in signed_perm_list:
		output_data.write('\n'+' '.join(map(str,signed_perm)))