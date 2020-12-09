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

seq = load_sequence(sys.argv[1])
preamble_length = int(sys.argv[2])
print( first_anomaly(seq, preamble_length) )
