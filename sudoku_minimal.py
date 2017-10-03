#This script was writted on the basis of:
#
# https://github.com/cjdrake/pyeda/blob/master/pyeda/logic/sudoku.py

from boolexpr import *
import sys
file_name = sys.argv[1]
ctx = Context()
DIGITS = "123456789"
X = ctx.get_vars("x", 9, 9, 9)
cell_d = and_(*[
            and_(*[
                or_(*[ X[r,c,v] for v in range(9) ])
                for c in range(9)
                ])
            for r in range(9)
            ])
cell_u = and_(*[
            and_(*[
                and_(*[
                    or_(*[ or_(*[ not_(*[X[r,c,vi]]), not_(*[X[r,c,vj]]) ]) for vj in range(vi+1,9) ])
                    for vi in range(9-1)
                    ])
                for c in range(9)
                ])
            for r in range(9)
            ])
row_d = and_(*[
            and_(*[
                or_(*[ X[r,c,v] for c in range(9) ])
                for v in range(9)
                ])
            for r in range(9)
            ])
row_u = and_(*[
            and_(*[
                and_(*[
                    and_(*[ or_(*[ not_(*[X[r,ci,v]]), not_(*[X[r,cj,v]]) ])  for cj in range(ci+1,9) ])
                    for ci in range(9-1)
                    ])
                for v in range(9)
                ])
            for r in range(9)
            ])
col_d = and_(*[
            and_(*[
                or_(*[ X[r,c,v] for r in range(9) ])
                for v in range(9)
                ])
            for c in range(9)
            ])
col_u = and_(*[
            and_(*[
                and_(*[
                    and_(*[ or_(*[ not_(*[X[rj,c,v]]), not_(*[X[ri,c,v]]) ])  for rj in range(ri+1,9) ])
                    for ri in range(9-1)
                    ])
                for v in range(9)
                ])
            for c in range(9)
            ])
block_d = and_(*[
            and_(*[
                and_(*[
                    or_(*[
                        or_(*[X[3*r_offs+r,3*c_offs+c,v] for c in range(3)])
                        for r in range(3)
                        ])
                        for v in range(9)
                    ])
                for c_offs in range(3)
                ])
            for r_offs in range(3)
            ])
block_u = and_(*[
            and_(*[
                and_(*[
                        onehot(*[ X[3*r_offs+r,3*c_offs+c,v] for r in range(3) for c in range(3) ])
                        for v in range(9)
                    ])
                for c_offs in range(3)
                ])
            for r_offs in range(3)
            ])
S = and_(cell_d,row_u, col_u, block_u)
def parse_grid(grid):
        chars = [c for c in grid if c in DIGITS or c in "0."]
        assert len(chars) == 9 ** 2
        return and_(*[ X[i//9,i%9,int(c)-1]
                        for i, c in enumerate(chars) if c in DIGITS ])
def get_val(point, r, c):
    for v in range(9):
        if point[X[r,c,v]]:
            return DIGITS[v]
    return "X"
def display(point):
    chars = list()
    for r in range(9):
        for c in range(9):
            chars.append(get_val(point, r, c))
        if r != 8:
            chars.append("\n")
with open(file_name, 'r') as f:
    lines = f.readlines()
    for line in lines:
        f = and_(S, parse_grid(line))
        solns = list(f.iter_sat())
    	#Verify there is exactly one solution
        #print(len(solns))
        #assert len(solns) == 1
        #display(solns[0])
        print(f)
