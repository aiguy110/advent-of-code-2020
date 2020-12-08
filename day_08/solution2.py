import sys

def load_instructions(filename):
    instructions = []
    with open(filename) as f:
        for line in f:
            op, arg = line.split()
            arg = int(arg)
            instructions.append( (op, arg) )
    
    return instructions

def get_accumulator_and_termination_mode(instructions):
    pc = 0
    pc_hist = []
    accumulator = 0
    while True:
        if pc in pc_hist:
            return (accumulator, 'repeated')
        elif pc == len(instructions):
            return (accumulator, 'finished')
        pc_hist.append( pc )

        op, arg = instructions[pc]
        if op == 'nop':
            pc += 1
        elif op == 'acc':
            accumulator += arg
            pc += 1
        elif op == 'jmp':
            pc += arg

base_instructions = load_instructions(sys.argv[1])
for i in range(len(base_instructions)):
    if base_instructions[i][0] in ['nop', 'jmp']:
        mutatated_instructions = base_instructions[:]
        mutatated_instructions[i] = ('nop' if base_instructions[i][0] == 'jmp' else 'jmp', base_instructions[i][1])
        acc, mode = get_accumulator_and_termination_mode( mutatated_instructions )
        if mode == 'finished':
            print(acc)