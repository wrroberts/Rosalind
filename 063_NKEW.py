#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Newick Format with Edge Weights
Rosalind ID: NKEW
Rosalind #: 063
URL: http://rosalind.info/problems/nkew/
'''

class Node(object):
    '''Node class for Newick Trees.'''
    def __init__(self, number, parent, name=None):
        '''Node initialization.'''
        self.number = number
        self.parent = parent
        self.children = []
        self.name = [name, 'Node_' + str(self.number)][name is None]

    def __repr__(self):
        '''Defines how Node instances are printed.'''
        return ['Node_' + str(self.number) + '('+str(self.name)+')', str(self.name)+'()'][self.name == 'Node_'+str(self.number)]

    def add_child(self, child):
        '''Add a child to the node.'''
        self.children.append(child)

class WeightedNewick(object):
    '''Creates a Newick Tree from the given data.'''
    def __init__(self, data):
        '''Initialize the Newick Tree.'''
        self.nodes = []
        self.node_index = 0
        self.edges = []
        self.node_weight = {}
        self.construct_tree(data)
        self.name_index = {node.name: node.number for node in self.nodes}

    def construct_tree(self, data):
        '''Constructs the Newick Tree.'''
        data = data.replace(',', ' ').replace('(','( ').replace(')',' )').strip(';').split()
        current_parent = Node(-1, None)
        for item in data:
            if item[0] == '(':
                current_parent = Node(len(self.nodes), current_parent.number)
                self.nodes.append(current_parent)
                if len(self.nodes) > 1:
                    self.nodes[current_parent.parent].add_child(current_parent.number)
                    self.edges.append((current_parent.parent, current_parent.number))

            elif item[0] == ')':
                if len(item) > 1:
                    self.node_weight[current_parent.number] = int(item[item.find(':') + 1:])
                    if len(item) > 2:
                        current_parent.name = item[1:item.find(':')]
                current_parent = self.nodes[current_parent.parent]

            else:
                self.nodes[current_parent.number].add_child(len(self.nodes))
                self.edges.append((current_parent.number, len(self.nodes)))
                self.node_weight[len(self.nodes)] = int(item[item.find(':') + 1:])
                self.nodes.append(Node(len(self.nodes), current_parent.number, item[:item.find(':')]))

    def edge_names(self):
        '''Return a list of edges referencing node names.'''
        return [(self.nodes[edge[0]].name, self.nodes[edge[1]].name) for edge in self.edges]

    def distance(self, name1, name2):
        '''Returns the distance between name1 and name2.'''
        if name1 == name2:
            return 0

        # Create the branches from the two desired nodes to the root.
        branch1 = [self.name_index[name1]]
        branch2 = [self.name_index[name2]]
        while self.nodes[branch1[-1]].parent != -1:
            branch1.append(self.nodes[branch1[-1]].parent)
        while self.nodes[branch2[-1]].parent != -1:
            branch2.append(self.nodes[branch2[-1]].parent)

        return sum([self.node_weight[node] for node in set(branch1) ^ set(branch2)])

    def get_descendants(self, node_name):
        descendants = []
        for child in self.nodes[self.name_index[node_name]].children:
            descendants.append(self.nodes[child].name)
            descendants += self.get_descendants(self.nodes[child].name)

        return descendants
        
with open('data/rosalind_nkew.txt') as input_data:
	trees = [line.split('\n') for line in input_data.read().strip().split('\n\n')]
	
distances = [str(WeightedNewick(tree[0]).distance(*tree[1].split())) for tree in trees]

print ' '.join(distances)
with open('output/063_NKEW_output.txt','w') as output_data:
	output_data.write(' '.join(distances))