# -*- coding: utf-8 -*-
''' This module solves a sudoku, This is actually written by Peter Norvig
    Code and Explanation can be found here : norvig.com/sudoku.html'''

def cross(A, B):
	return [a+b for a in A for b in B]

digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits
squares = cross(rows, cols)
unitlist = ([cross(rows, c) for c in cols] + [cross(r, cols) for r in rows] + [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')])
units = dict((s, [u for u in unitlist if s in u]) for s in squares)
# print(units)
# print(unitlist)

# peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

peers =dict()
for s in squares:
	peers[s] = set(sum(units[s],[]))-set([s])

print(peers)
