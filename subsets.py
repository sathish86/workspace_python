"""
9.4 Write a method to return all subsets of a set

Base Case: n = 0.
There is just one subset of the empty set: {}.
Case:r\ 1.
There are two subsets of the set {aj: {}, {aj.
Case:n = 2.
There are four subsets of the set {a^ a2}: {}, {aj, {a2}, {aaJ a2}.

"""

class Item:
    """Lightweight composite to store priority queue items."""

    def init (self, k, v):
        self. key = k
        self. value = v

    def lt (self, other):
        return self. key < other. key # compare items based on their keys
