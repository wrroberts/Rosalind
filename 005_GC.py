#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Computing GC Content
Rosalind ID: GC
Rosalind #: 005
URL: http://rosalind.info/problems/gc/
'''

'''First Option'''

inputFile = open('rosalind_gc.txt','r')
max_label = ""
max_gc = 0

c_count = 0
g_count = 0
temp_label = ""
temp_gc = 0.0
temp_len = 0

for line in inputFile:
    if line.startswith('>'):
        if temp_len !=0:
            temp_gc = (c_count + g_count) / temp_len * 100
            if temp_gc > max_gc:
                max_label = temp_label
                max_gc = temp_gc
            c_count = 0
            g_count = 0
            temp_len = 0
        temp_label = line[1:14]
    else:
        c_count += line.count('C')
        g_count += line.count('G')
        temp_len += len(str.strip(line))

temp_gc = (c_count + g_count) / temp_len * 100
if temp_gc > max_gc:
    max_label = temp_label
    max_gc = temp_gc
    
print max_label
print max_gc

''' Second Option'''

from Bio import SeqIO
from Bio.SeqUtils import GC
GCcont = 0
GCname = ""
file = open("rosalind_gc.txt", "r")
for record in SeqIO.parse(file, "fasta"):
    if GCcont < GC(record.seq):
        GCcont = GC(record.seq)
        GCname = record.id

print GCname
print round(GCcont,2), "%"

'''Third Option'''

for seq_record in SeqIO.parse('rosalind_gc.txt','fasta'):
    A = seq_record.seq.count('A')
    T = seq_record.seq.count('T')
    C = seq_record.seq.count('C')
    G = seq_record.seq.count('G')
    gc_content = (((G+C) / (A+T+G+C))*100)
    print(seq_record.id, gc_content)
    
'''Fourth Attempt'''

def gc_content(dna):
        return 100 * (dna.count("C") + dna.count("G")) / float(len(dna))

def get_best_content(dna_list):
        best = (0, "")
        for name in dna_list:
                current_gc = gc_content(dna_list[name])
                if current_gc > best[0]:
                        best = (current_gc, name)
        return best

def read_input():
        lines = [line[:-1] for line in open("rosalind_gc.txt")]
        dna = {}
        for line in lines:
                if line[0] == ">":
                        current_name = line[1:]
                        dna[current_name] = ""
                else:
                        dna[current_name] += line
        return dna

dna_list = read_input()
best = get_best_content(dna_list)
print best[1]
print best[0]
