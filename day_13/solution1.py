import sys

def load_bus_notes(filename):
    with open(filename) as f:
        earliest_departure = int(f.readline())
        bus_ids_line = f.readline().strip()
        bus_ids = []
        for s in bus_ids_line.split(','):
            if s != 'x':
                bus_ids.append(int(s))
    
    return earliest_departure, bus_ids


earliest_departure, bus_ids = load_bus_notes(sys.argv[1])
best_id = None
best_wait = None
for bus_id in bus_ids:
    wait = bus_id - earliest_departure % bus_id
    if best_id == None or wait < best_wait:
        best_id = bus_id
        best_wait = wait

print(best_id * best_wait)