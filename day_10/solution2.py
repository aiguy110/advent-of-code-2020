import sys

def load_adapters(filename):
    adapters = []
    with open(filename) as f:
        for line in f:
            adapters.append( int(line) )
    
    return sorted(adapters)

def is_valid_config(adapters, end_adapter, start_adapter=0):
    if len(adapters) == 0:
        if end_adapter - start_adapter > 3:
            return False
        else:
            return True
    if adapters[0] - start_adapter > 3:
        return False
    if end_adapter - adapters[-1] > 3:
        return False

    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i-1] > 3:
            return False
    
    return True

def valid_configs(adapters, end_adapter, start_adapter=0, seen_configs=set()):
    if str(adapters) in seen_configs:
        return

    if is_valid_config(adapters, end_adapter, start_adapter):
        seen_configs.add( str(adapters) )
        yield adapters
    else:
        return
    
    for i in range(len(adapters)-1):
        yield from valid_configs( adapters[:i]+adapters[i+1:], end_adapter, start_adapter, seen_configs )

    if is_valid_config(adapters[:-1], end_adapter, start_adapter):
        yield adapters[:-1]

def get_islands(adapters):
    island_start_ind = 0
    if adapters[0] == 3:
        island_start_ind = 0
    
    islands = []
    for i in range(len(adapters)-1):
        if adapters[i+1] - adapters[i] == 3:
            islands.append( (island_start_ind, i+1) )
            island_start_ind = i+1
    
    islands.append( (island_start_ind, len(adapters)) )
    
    return islands

adapters = load_adapters(sys.argv[1])
island_config_counts = []
for island in get_islands(adapters):
    island_slice = adapters[island[0]: island[1]]
    start_adapter = 0 if island[0] == 0 else adapters[island[0]-1]
    end_adapter = adapters[island[1]] if island[1] < len(adapters) else max(adapters) + 3
    config_count = 0
    for config in valid_configs(island_slice, end_adapter, start_adapter):
        config_count += 1
    
    island_config_counts.append( config_count )

prod = 1
for n in island_config_counts:
    prod *= n

print(prod)