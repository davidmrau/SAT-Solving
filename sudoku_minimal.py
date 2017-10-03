#This script was writted on the basis of:
#
# https://github.com/cjdrake/pyeda/blob/master/pyeda/logic/sudoku.py

from boolexpr import *
import sys
file_name = sys.argv[1]
ctx = Context()
DIGITS = "123456789"
X = ctx.get_vars("x", 9, 9, 9)
cell_d = and_s(*[
            and_s(*[
                or_s(*[ X[r,c,v] for v in range(9) ])
                for c in range(9)
                ])
            for r in range(9)
            ])
cell_u = and_s(*[
            and_s(*[
                and_s(*[
                    or_s(*[ or_s(*[ neq_s(*[X[r,c,vi]]), neq_s(*[X[r,c,vj]]) ])  for vj in range(vi+1,9) ])
                    for vi in range(9-1)
                    ])
                for c in range(9)
                ])
            for r in range(9)
            ])
row_d = and_s(*[
            and_s(*[
                or_s(*[ X[r,c,v] for c in range(9) ])
                for v in range(9)
                ])
            for r in range(9)
            ])


row_u = and_s(*[
            and_s(*[
                and_s(*[
                    and_s(*[ or_s(*[ neq_s(*[X[r,ci,v]]), neq_s(*[X[r,cj,v]]) ])  for cj in range(ci+1,9) ])
                    for ci in range(9-1)
                    ])
                for v in range(9)
                ])
            for r in range(9)
            ])

col_d = and_s(*[
            and_s(*[
                or_s(*[ X[r,c,v] for r in range(9) ])
                for v in range(9)
                ])
            for c in range(9)
            ])


col_u = and_s(*[
            and_s(*[
                and_s(*[
                    and_s(*[ or_s(*[ neq_s(*[X[rj,c,v]]), neq_s(*[X[ri,c,v]]) ])  for rj in range(ri+1,9) ])
                    for ri in range(9-1)
                    ])
                for v in range(9)
                ])
            for c in range(9)
            ])

block_d = and_s(*[
            and_s(*[
                and_s(*[
                    or_s(*[
                        or_s(*[X[3*r_offs+r,3*c_offs+c,v] for c in range(3)])
                        for r in range(3)
                        ])
                        for v in range(9)
                    ])
                for c_offs in range(3)
                ])
            for r_offs in range(3)
            ])

block_u = and_s(*[
            and_s(*[
                and_s(*[
                    and_s(*[
                        and_s(*[ or_s(*[ neq_s(*[X[(3*r_offs)+(r%3),(3*c_offs)+(r%3),v]]), neq_s(*[X[(3*r_offs)+(r%3),(3*c_offs)+(c%3),v]])]) for c in range(r+1,9)])
                        for r in range(9-1)
                        ])
                        for v in range(9)
                    ])
                for c_offs in range(3)
                ])
            for r_offs in range(3)
            ])
S = and_s(cell_d,row_u, col_u, block_u)
def parse_grid(grid):
        chars = [c for c in grid if c in DIGITS or c in "0."]
        assert len(chars) == 9 ** 2
        return and_s(*[ X[i//9,i%9,int(c)-1]
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
        f = and_s(S, parse_grid(line))
        print(f)
