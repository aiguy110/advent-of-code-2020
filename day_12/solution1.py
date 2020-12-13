import sys

def load_directions(filename):
    directions = []
    with open(filename) as f:
        for line in f:
            op, arg = line[0], int(line.strip()[1:])
            if op == 'R':
                op = 'T'
                arg = arg // 90
            elif op == 'L':
                op = 'T'
                arg = -arg // 90

            directions.append( (op, arg) )
    
    return directions

def get_total_offset(directions):
    i, j = 0, 0
    headings = [
        ('N', (-1, 0)),
        ('E', ( 0, 1)),
        ('S', ( 1, 0)),
        ('W', ( 0,-1))
    ]
    current_heading = 1

    def move(direction, dist):
        nonlocal i, j
        di, dj = direction
        i += dist*di
        j += dist*dj    

    for op, arg in directions:
        if op == 'T':
            current_heading = (current_heading + arg) % 4
        elif op == 'F':
            direction = headings[current_heading][1]
            move(direction, arg)
        else:
            for heading in headings:
                if heading[0] == op:
                    move(heading[1], arg)
                    break
    
    return (i, j)

directions = load_directions(sys.argv[1])
print( sum(get_total_offset(directions)) )

