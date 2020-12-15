import sys

def load_bus_notes(filename):
    with open(filename) as f:
        f.readline()
        schedule = f.readline().split(',')
        busses = []
        for i in range(len(schedule)):
            if schedule[i] != 'x':
                busses.append( (i, int(schedule[i])) )
        
    return busses

def check_solution(t, busses):
    for order, bus_id in busses:
        if (bus_id - t % bus_id) % bus_id != order % bus_id:
            return False
    
    return True

def gcd(a, b):
    if min(a,b) == 0:
        return max(a,b)
    else:
        return gcd(min(a, b), max(a, b) % min(a, b))

def lcm(a, b):
    return a * b // gcd(a,b)

def lcm_seq(seq):
    x = 1
    for n in seq:
        x = lcm(x, n)
    
    return x

busses = load_bus_notes(sys.argv[1])
busses.sort(key=lambda x: x[1])

step_size = busses[0][1]
n = 2
t = -busses[0][0]
while True:
    if check_solution(t, busses):
        break
    
    if check_solution(t, busses[:n]):
        step_size = lcm_seq( map(lambda x: x[1], busses[:n]) )
        n += 1
    
    t += step_size

print(t) 

