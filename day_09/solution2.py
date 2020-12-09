import sys

def load_sequence(filename):
    seq = []
    with open(filename) as f:
        for line in f:
            seq.append( int(line.strip()) )
    
    return seq

def is_sum_of_pair(n, seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] + seq[j] == n:
                return True
    
    return False


def first_anomaly(seq, preable_length):
    for i in range(preable_length, len(seq)):
        if not is_sum_of_pair(seq[i], seq[i-preable_length:i]):
            return seq[i]
    
    return None

def find_block_summing_to(n, seq):
    s, e = 0, 1
    while e < len(seq):
        S = sum(seq[s:e+1])
        if S < n:
            e += 1
        elif S > n:
            s += 1
        elif s == e:
            e += 1
        else:
            return seq[s:e+1]


seq = load_sequence(sys.argv[1])
preamble_length = int(sys.argv[2])
anom = first_anomaly(seq, preamble_length)
target_block = find_block_summing_to(anom, seq)
print( min(target_block) + max(target_block) )
