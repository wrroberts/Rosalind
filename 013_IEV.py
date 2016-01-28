#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Calculating Expected Offspring.
Problem ID: IEV
Problem #: 013
URL: http://rosalind.info/problems/iev/
'''

#Probability of offspring with dominant phenotype
# AA - AA -> 100%
# AA - Aa -> 100%
# AA - aa -> 100%
# Aa - Aa -> 75%
# Aa - aa -> 50%
# aa - aa -> 0%

with open('rosalind_iev.txt','r') as input_data:
	s = input_data.read().split()
	
p_list = [1, 1, 1, 0.75, 0.5, 0]
EV_list = []

for index, num_parents in enumerate(s):
	EV_list.append(2*int(num_parents)*p_list[index])
	
print sum(EV_list)
