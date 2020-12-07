import sys

tree_grid = []
with open(sys.argv[1]) as f:
    for row in f:
        tree_grid.append( row.strip() )

rows = len(tree_grid)
cols = len(tree_grid[0])

def is_tree(i, j):
    return tree_grid[i % rows][j % cols] == '#'

trees_encountered = 0
j = 0
cols_per_row = 3
for i in range(rows):
    if is_tree(i, j):
        trees_encountered += 1
    j += cols_per_row

print(trees_encountered)
