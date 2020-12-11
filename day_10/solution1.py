import sys

def load_adapters(filename):
    adapters = []
    with open(filename) as f:
        for line in f:
            adapters.append( int(line) )
    
    return sorted(adapters)

def get_diff_dict(adapters):
    diff_dict = {3:1, adapters[0]: 1}
    for a in range(1, len(adapters)):
        diff = adapters[a] - adapters[a-1]
        if diff in diff_dict:
            diff_dict[diff] += 1
        else:
            diff_dict[diff] = 1
    
    return diff_dict

diff_dict = get_diff_dict(load_adapters(sys.argv[1]))
print( diff_dict[1] * diff_dict[3] )