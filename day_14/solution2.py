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

def apply_mask(mask, addr):
    addr_bin = bin(addr)[2:]
    addr_bin = '0' * (len(mask) - len(addr_bin)) + addr_bin

    result = ''
    for i in range(len(mask)):
        if mask[i] == 'X':
            result += 'X'
        elif mask[i] == '0':
            result += addr_bin[i]
        else:
            result += '1'
    
    for n in range(2**result.count('X')):
        n_bin = bin(n)[2:]
        n_bin = '0' * (result.count('X') - len(n_bin)) + n_bin
        specific_result = result
        for i in range(len(n_bin)):
            x = specific_result.index('X')
            specific_result = specific_result[:x] + n_bin[i] + specific_result[x+1:]
        
        yield specific_result
            

def get_program_sum(instructions):
    mask = 'X'*36
    mem = {}
    
    for addr, val in instructions:
        if addr == 'mask':
            mask = val
        else:
            for specific_addr in apply_mask(mask, addr):
                mem[specific_addr] = val
    
    return sum( mem.values() )

program = load_program(sys.argv[1])
print( get_program_sum(program) )