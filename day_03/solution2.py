import functools
import sys

tree_grid = []
with open(sys.argv[1]) as f:
    for row in f:
        tree_grid.append( row.strip() )

rows = len(tree_grid)
cols = len(tree_grid[0])

def is_tree(i, j):
    return tree_grid[i % rows][j % cols] == '#'

def num_trees_encountered_with_step(step):
    num_trees = 0 
    i, j = 0, 0
    di, dj = step
    while i < rows:
        if is_tree(i, j):
            num_trees += 1
        i += di
        j += dj
    
    return num_trees

def mult(l):
    return functools.reduce(lambda x, y: x*y, l)

steps = [
    (1, 1),
    (1, 3),
    (1, 5),
    (1, 7),
    (2, 1)
]


print( mult(map(num_trees_encountered_with_step, steps)) )