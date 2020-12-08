import sys

def load_instructions(filename):
    instructions = []
    with open(filename) as f:
        for line in f:
            op, arg = line.split()
            arg = int(arg)
            instructions.append( (op, arg) )
    
    return instructions

def get_accumulator_at_repeat(instructions):
    pc = 0
    pc_hist = []
    accumulator = 0
    while True:
        if pc in pc_hist:
            break
        pc_hist.append( pc )

        op, arg = instructions[pc]
        if op == 'nop':
            pc += 1
        elif op == 'acc':
            accumulator += arg
            pc += 1
        elif op == 'jmp':
            pc += arg
    
    return accumulator

instructions = load_instructions(sys.argv[1])
print( get_accumulator_at_repeat(instructions) )