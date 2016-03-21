#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Completing a Tree
Rosalind ID: TREE
Rosalind #: 032
URL: http://rosalind.info/problems/tree/
'''

with open('data/rosalind_tree.txt') as input_data:
    edges = input_data.read().strip().split('\n')
    n = int(edges.pop(0))
    edges = [map(int,edge.split()) for edge in edges]
    
connected_nodes = [{i} for i in range(1,n+1)]

for edge in edges:
    temp_nodes = set()
    del_nodes = []
    for nodes in connected_nodes:
        if (edge[0] in nodes) and (edge[1] in nodes):
            break
        elif (edge[0] in nodes) or (edge[1] in nodes):
            temp_nodes.update(nodes)
            del_nodes.append(nodes)
            if len(del_nodes) == 2:
                break
    if len(del_nodes) != 0:
        temp_nodes.add(edge[0])
        temp_nodes.add(edge[1])
        for nodes in del_nodes:
            connected_nodes.remove(nodes)
        connected_nodes.append(temp_nodes)
        
print len(connected_nodes)-1
with open('output/032_TREE_output.txt','w') as output_data:
    output_data.write(str(len(connected_nodes)-1))