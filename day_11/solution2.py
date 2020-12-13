import sys

def load_seating_state(filename):
    rows = []
    with open(filename) as f:
        for line in f:
            rows.append( line.strip() )
    
    return rows

def get_cell(i, j, state):
    if i < 0 or j < 0 or i >= len(state) or j >= len(state[0]):
        return '-'
    else:
        return state[i][j]

def set_cell(i, j, state, x):
    state[i] = state[i][:j] + x + state[i][j+1:]

def line_of_sight(i, j, di, dj, state):
    I, J = i, j
    while True:
        I += di
        J += dj
        viz_cell = get_cell(I, J, state)
        if viz_cell != '.':
            return viz_cell

def get_next_state(current_state):
    next_state = []
    for row in current_state:
        next_state.append( row )

    for i in range(len(next_state)):
        for j in range(len(next_state[0])):
            this_cell = get_cell(i, j, current_state) 
            if this_cell == '.':
                continue
            
            adj_occupied = 0
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    if di == 0 and dj == 0:
                        continue
                    if line_of_sight(i, j, di, dj, current_state) == '#':
                        adj_occupied += 1
            
            if this_cell == 'L' and adj_occupied == 0:
                set_cell(i, j, next_state, '#')
            elif this_cell == '#' and adj_occupied >= 5:
                set_cell(i, j, next_state, 'L')
    
    return next_state

current_state = load_seating_state(sys.argv[1])
seen_states = set([ ''.join(current_state) ])
while True:
    current_state = get_next_state(current_state)
    if ''.join(current_state) in seen_states:
        break
    else:
        seen_states.add( ''.join(current_state) )

total_occupied = 0
for row in current_state:
    total_occupied += row.count('#')
    print(row)

print('Steady state seats occupied:', total_occupied)