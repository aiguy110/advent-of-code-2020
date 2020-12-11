import sys

def load_adapters(filename):
    adapters = []
    with open(filename) as f:
        for line in f:
            adapters.append( int(line) )
    
    return sorted(adapters)

def is_valid_config(adapters, end_adapter):
    if len(adapters) == 0:
        return False
    if adapters[0] > 3:
        return False
    if end_adapter - adapters[-1] > 3:
        return False

    for i in range(1, len(adapters)):
        if adapters[i] - adapters[i-1] > 3:
            return False
    
    return True

def valid_configs(adapters, end_adapter, seen_configs=set()):
    if str(adapters) in seen_configs:
        return

    if is_valid_config(adapters, end_adapter):
        seen_configs.add( str(adapters) )
        yield adapters
    else:
        return
    
    for i in range(len(adapters)-1):
        yield from valid_configs( adapters[:i]+adapters[i+1:], end_adapter, seen_configs )

    if is_valid_config(adapters[:-1], end_adapter):
        yield adapters[:-1]

adapters = load_adapters(sys.argv[1])

num_configs = 0
for config in valid_configs(adapters, max(adapters)+3):
    num_configs += 1

print(num_configs)