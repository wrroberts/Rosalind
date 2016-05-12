#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Edit Distance Alignment
Rosalind ID: EDTA
Rosalind #: 058
URL: http://rosalind.info/problems/edta/
'''

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

def edit_alignment(v,w):
	'''Returns the edit score and edit alignment of strings v and w.'''
	from numpy import zeros
	
	S = zeros((len(v)+1, len(w)+1), dtype=int)
	backtrack = zeros((len(v)+1, len(w)+1), dtype=int)
	
	for i in xrange(1, len(v)+1):
		S[i][0] = i
	for j in xrange(1, len(w)+1):
		S[0][j] = j
	
	for i in xrange(1, len(v)+1):
		for j in xrange(1, len(w)+1):
			scores = [S[i-1][j-1] + (v[i-1] != w[j-1]), S[i-1][j]+1, S[i][j-1]+1]
			S[i][j] = min(scores)
			backtrack[i][j] = scores.index(S[i][j])
			
	insert_indel = lambda word, i: word[:i] + '-' + word[i:]
	
	v_aligned, w_aligned = v,w
	
	i,j = len(v), len(w)
	min_score = S[i][j]
	
	while i*j != 0:
		if backtrack[i][j] == 1:
			i -= 1
			w_aligned = insert_indel(w_aligned, j)
		elif backtrack[i][j] == 2:
			j -= 1
			v_aligned = insert_indel(v_aligned, i)
		else:
			i -= 1
			j -= 1
			
	for repeat in xrange(i):
		w_aligned = insert_indel(w_aligned, 0)
	for repeat in xrange(j):
		v_aligned = insert_indel(v_aligned, 0)
		
	return str(min_score), v_aligned, w_aligned
	
if __name__ == '__main__':

	s,t = [fasta[1] for fasta in ReadFASTA('data/rosalind_edta.txt')]
	
	edited = edit_aligned(s,t)
	
	print '\n'.join(edited)
	with open('output/058_EDIT_output.txt','w') as output_data:
		output_data.write('\n'.join(edited))