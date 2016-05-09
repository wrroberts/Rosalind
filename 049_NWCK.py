#!/usr/bin/env python
'''
A solution to a ROSALIND bioinformatics problem.

Problem Title: Distances in Trees
Rosalind ID: NWCK
Rosalind #: 049
URL: http://rosalind.info/problems/nwck/
'''

def parse_newick(text):
    import operator
    from parcon import Alpha, Digit, ZeroOrMore, Optional, Forward, OneOrMore, Longest, flatten, InfixExpr, CharIn

    labels = {}

    class ZNode(object):
        def __init__(self, label=None, length=None):
            self.label = label
            self.length = length
            self.children = []
            self.parent = None

        def add_child(self, node):
            node.parent = self
            self.children.append(node)

        def ancestors(self):
            pairs = [(self, 0)]
            node = self
            while node.parent:
                pairs.append((node.parent, pairs[-1][1] + 1))
                node = node.parent
            return pairs

        def __str__(self):
            return "{}[{}]:{}".format(
                self.label,
                ''.join(map(str, self.children)),
                self.length
            )

        def __repr__(self):
            s = "<%s" % (self.label or "?",)
            if self.children:
                s += " " + ", ".join(map(repr, self.children))
            s += ">"
            return s

    def make_leaf(ast):
        # print "leaf ast", ast
        label = ast
        node = ZNode(label=label)
        if label:
            labels[label] = node
        return node

    def make_internal(ast):
        # print "internal ast", ast
        if isinstance(ast[0], ZNode):
            node = ZNode()
            children = ast
        else:
            label = ast[-1]
            node = ZNode(label=label)
            if label:
                labels[label] = node
            children = ast[-2]
        for n in children:
            node.add_child(n)
        return node

    def test(args):
        # print "matched:", args
        return args

    Name = ZeroOrMore(Alpha() | CharIn("_"))[''.join]
    Leaf = Name
    Node = Forward()
    Internal = ("(" + InfixExpr(Node[lambda x: [x]], [(",", operator.add)]) + ")") + Optional(Name)
    Node << (Internal[make_internal] | Leaf[make_leaf])
    Tree = Node + ";"

    return Tree.parse_string(text), labels
    
def parse(text):

    lines = filter(None, text.split("\n"))
    pairs = [lines[i:i+2] for i in range(0, len(lines)-1, 2)]
    return [(parse_newick(p[0]), p[1].split()) for p in pairs]


def problem(tree, ks):
    tree, labels = tree
    kx = labels[ks[0]]
    ky = labels[ks[1]]
    kx_depths = dict(kx.ancestors())
    ky_depths = dict(ky.ancestors())
    common = set([x[0] for x in kx.ancestors()]) & set([y[0] for y in ky.ancestors()])
    best = sorted(common, key=lambda k: kx_depths[k] + ky_depths[k])[0]
    return kx_depths[best] + ky_depths[best]


def format(results):
    print ' '.join(map(str, results))


if __name__ == '__main__':
    import doctest
    from os.path import dirname

    doctest.testmod()

    dataset = open("data/rosalind_nwck.txt").read()
    dataset = parse(dataset)
    format(problem(t, k) for t, k in dataset)