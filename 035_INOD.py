#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Phylogenetic Ancestors
Rosalind ID: INOD
Rosalind #: 035
URL: http://rosalind.info/problems/inod/
'''

# Let m = number of internal nodes, n = number of leaves, E = number of edges
# The sum of the degrees of all vertices is twice the number of edges.
# 2E = 3m + n
#
# From Rosalind Problem 032, the total number of edges is one less than the number of nodes.
# E = m + n - 1
# Scaling to match the above statement: 2E = 2m + 2n - 2
#
# Set the two expressions equal to each other, and solve for m in terms of n.
# 3m + n = 2m + 2n - 2 ==> m = n - 2

with open('data/rosalind_inod.txt') as input_data, open('output/035_INOD_output.txt','w') as output_data:
	n = int(input_data.read().strip())
	print n-2
	output_data.write(str(n-2))