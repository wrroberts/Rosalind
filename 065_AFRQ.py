#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Counting Disease Carriers
Rosalind ID: AFRQ
Rosalind #: 065
URL: http://rosalind.info/problems/afrq/
'''

# Let x = proportion of homozygous recessive, y = proportion heterozygous.
# We want the proportion of population carrying at least 1 recessive allele, so the answer is x + y.
#
# Assume allele frequency is stable.
# Given the proportion of recessive individuals, we need to setup an equation for the proportion of recessive individuals.
# The only way to get the recessive trait is mating between recessives and/or heterozygotes.
#
# Use the total law of probability.
# Proportion recessive = P(Recessive|2 Rec Mate)P(2 Rec Mate) + P(Recessive|1 Rec 1 Het Mate)P(1 Rec 1 Het Mate) + P(Recessive|2 Het Mate)P(2 Het Mate)
# In terms of variable: x = (1)*(x^2) + (0.5)(2*x*y) + (0.25)*(y^2)
#						x = x^2 + xy + 0.25y^2
#
# Use quadratic formula to solve for y:
#			y = -2x +/- 2*sqrt(x) ==> y = 2*sqrt(x) - 2x since y must be positive.
#
# Substitute into the solution formula: x + y = x + (2*sqrt(x)-2x) = 2*sqrt(x) - x
#
# Therefore, the solution is 2*sqrt(x) - x

from math import sqrt

with open('data/rosalind_afrq.txt') as input_data:
	A = map(float, input_data.read().strip().split())

B = [2*sqrt(i)-i for i in A]

print ' '.join(map(str, B))
with open('output/065_AFRQ_output.txt','w') as output_data:
	output_data.write(' '.join(map(str,B))
