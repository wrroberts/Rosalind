#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Finding a Shared Spliced Motif
Rosalind ID: LCSQ
Rosalind #: 038
URL: http://rosalind.info/problems/lcsq/
'''

from numpy import zeros

def longest_common_subsequence(dna1, dna2):
	M = zeros((len(dna1)+1,len(dna2)+1))
	for i in xrange(len(dna1)):
		for j in xrange(len(dna2)):
			if dna1[i] == dna2[j]:
				M[i+1][j+1] = M[i][j]+1
			else:
				M[i+1][j+1] = max(M[i+1][j],M[i][j+1])
	
	longest_sseq = ''
	i,j = len(dna1), len(dna2)
	while i*j != 0:
		if M[i][j] == M[i-1][j]:
			i -= 1
		elif M[i][j] == M[i][j-1]:
			j -= 1
		else:
			longest_sseq = dna1[i-1] + longest_sseq
			i -= 1
			j -= 1
	
	return longest_sseq
	
import urllib
import contextlib

def ReadFASTA(data_location):
        '''Determines the data type of the FASTA format data and passes the appropriate information to be parsed.'''
        
        # If given a list, return fasta information from all items in the list.
        if type(data_location) == list:
                fasta_list =[]
                for location in data_location:
                        fasta_list+=ReadFASTA(location)
                return fasta_list


        # Check for a text file, return fasta info from the text file.
        if data_location[-4:] == '.txt':
                with open(data_location) as f:
                        return ParseFASTA(f)
        
        # Check for a website, return fasta info from the website.
        elif data_location[0:4] == 'http':
                with contextlib.closing(urllib.urlopen(data_location)) as f:
                        return ParseFASTA(f)


def ParseFASTA(f):
        '''Extracts the Sequence Name and Nucleotide/Peptide Sequence from the a FASTA format file or website.'''
        fasta_list=[]
        for line in f:

                # If the line starts with '>' we've hit a new DNA strand, so append the old one and create the new one.
                if line[0] == '>':
                        
                        # Using try/except because intially there will be no current DNA strand to append.
                        try:
                                fasta_list.append(current_dna)
                        except UnboundLocalError:
                                pass

                        current_dna = [line.lstrip('>').rstrip('\n'),'']

                # Otherwise, append the current DNA line to the current DNA
                else:
                        current_dna[1] += line.rstrip('\n')
        
        # Append the final DNA strand after reading all the lines.
        fasta_list.append(current_dna)

        return fasta_list
	
if __name__ == '__main__':
	dna1, dna2 = [fasta[1] for fasta in ReadFASTA('data/rosalind_lcsq.txt')]
	
	lcsq = longest_common_subsequence(dna1, dna2)
	
	print lcsq
	with open('output/038_LCSQ_output.txt','w') as output_file:
		output_file.write(lcsq)