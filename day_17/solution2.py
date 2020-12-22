import sys

def load_cells(filename):
    active_cells = set()
    with open(filename) as f:
        i = 0
        for line in f:
            for j in range(len(line)):
                if line[j] == '#':
                    active_cells.add( (i, j, 0, 0) )
            i += 1
    
    return active_cells

def get_adjacent_cells(cell):
    i, j, k, l = cell
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            for dk in [-1, 0, 1]:
                for dl in [-1, 0, 1]:
                    if di == 0 and dj == 0 and dk == 0 and dl == 0:
                        continue
                
                    yield (i+di, j+dj, k+dk, l+dl)

def get_neighbor_count(cell, active_cells):
    count = 0
    for adj_cell in get_adjacent_cells(cell):
        if adj_cell in active_cells:
            count += 1
    
    return count

def get_next_active_cells(current_active_cells):
    cells_to_check = set()
    for cell in current_active_cells:
        cells_to_check.add(cell)
        for adj_cell in get_adjacent_cells(cell):
            cells_to_check.add( adj_cell )
    
    next_active_cells = set()
    for cell in cells_to_check:
        neighbor_count = get_neighbor_count(cell, current_active_cells)
        if neighbor_count == 3:
            next_active_cells.add( cell )
        elif cell in current_active_cells and neighbor_count == 2:
            next_active_cells.add( cell )
    
    return next_active_cells


current_active_cells = load_cells(sys.argv[1])

N = 6
for i in range(N):
    current_active_cells = get_next_active_cells( current_active_cells )

print(len(current_active_cells))


