#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Rabbits and Recurrence Relations
Rosalind ID: FIB
Rosalind #: 004
URL: http://rosalind.info/problems/fib/
'''

'''First Option'''

def fib_rabbits(n,k):
    rabbits = [0,1]
    for i in xrange(n-1):
        rabbits[i % 2] = rabbits[(i-1) % 2] + k*rabbits[i % 2]
    return rabbits[n % 2]

def main():
    with open('rosalind_fib.txt') as input_data:
        n,k = map(int,input_data.read().strip().split())
    
    rabbits=str(fib_rabbits(n,k))
    
    print rabbits
    with open('FIB.txt','w') as output_data:
        output_data.write(rabbits)
if __name__ == '__main__':
    main()
    
'''Second Option'''

def fib(n,factor):
    if n< 2:
        return n
    return factor*fib(n-2,factor) + fib(n-1,factor)
print fib(34,5)
