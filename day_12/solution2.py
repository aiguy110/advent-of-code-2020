import sys

def load_directions(filename):
    directions = []
    with open(filename) as f:
        for line in f:
            op, arg = line[0], int(line.strip()[1:])
            if op == 'R':
                op = 'T'
                arg = -arg // 90
            elif op == 'L':
                op = 'T'
                arg = arg // 90

            directions.append( (op, arg) )
    
    return directions

def get_total_offset(directions):
    i, j = 0, 0
    wi, wj = -1, 10   

    headings = {
        'N': (-1, 0),
        'E': ( 0, 1),
        'S': ( 1, 0),
        'W': ( 0,-1)
    }

    turns = [
        lambda i, j: ( i, j),
        lambda i, j: (-j, i),
        lambda i, j: (-i,-j),
        lambda i, j: ( j,-i)
    ]

    for op, arg in directions:
        if op == 'T':
            wi, wj = turns[arg % 4](wi, wj)
        elif op == 'F':
            i += arg * wi
            j += arg * wj
        else:
            di, dj = headings[op]
            wi += di * arg
            wj += dj * arg
        
        print((i, j), (wi, wj))
            
    
    return (i, j)

directions = load_directions(sys.argv[1])
print( sum(map(abs, get_total_offset(directions))) )

