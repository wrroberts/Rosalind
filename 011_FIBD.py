#!/usr/bin/env python

'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Mortal Fibonacci Rabbits
Problem ID: FIBD
Problem #: 011
URL: http://rosalind.info/problems/fibd/
'''

with open('rosalind_fibd.txt','r') as input_data:
	n,m = map(int,input_data.read().split())

Rabbits = [1]+[0]*(m-1)

for year in range(1,n):
	Bunnies = 0
	for j in range(1,m):
		Bunnies += Rabbits[(year-j-1)%m]
	Rabbits[(year)%m] = Bunnies

Total_Rabbits = sum(Rabbits)

with open('011_FIBD_output.txt','w') as output_data:
	print Total_Rabbits
	output_data.write(str(Total_Rabbits))
