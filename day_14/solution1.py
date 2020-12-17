import sys
import re

def load_program(filename):
    with open(filename) as f:
        instructions = []
        for line in f:
            if line[:4] == 'mask':
                instructions.append( ('mask', re.match(r'mask = ([01X]{36})', line).group(1)) )
            else: 
                addr, val = map( int, re.match(r'mem\[(\d+)\] = (\d+)', line).groups([1,2]) )
                instructions.append( (addr, val) )
    return instructions

def apply_mask(mask, num):
    num_bin = bin(num)[2:]
    num_bin = '0' * (len(mask) - len(num_bin)) + num_bin

    result = ''
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += num_bin[i]
        else:
            result += mask[i]
    
    return int(result, base=2)

def get_program_sum(instructions):
    mask = 'X'*36
    mem = {}
    
    for addr, val in instructions:
        if addr == 'mask':
            mask = val
        else:
            mem[addr] = apply_mask(mask, val)
    
    return sum( mem.values() )

program = load_program(sys.argv[1])
print( get_program_sum(program) )