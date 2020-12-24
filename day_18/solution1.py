import sys

def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        if s[i] in '()+*':
            tokens.append( s[i] )
        elif s[i] in '0123456789':
            j = i
            while j < len(s) and s[j] in '0123456789':
                j += 1
            tokens.append( int(s[i:j]) )
            i = j-1
        
        i += 1
    
    return tokens

def find_matching_paren(tokens, i):
    depth = 0
    while True:
        if tokens[i] == '(':
            depth += 1
        elif tokens[i] == ')':
            depth -= 1

        if depth == 0:
            return i

        i += 1

def evaluate(tokens):
    while '(' in tokens:
        i = tokens.index('(')
        j = find_matching_paren(tokens, i)
        tokens = tokens[:i] + [evaluate(tokens[i+1:j])] + tokens[j+1:]
    
    while len(tokens) > 1:
        if tokens[1] == '+':
            tokens = [tokens[0] + tokens[2]] + tokens[3:]
        elif tokens[1] == '*':
            tokens = [tokens[0] * tokens[2]] + tokens[3:]
    
    return tokens[0]

with open(sys.argv[1]) as f:
    total = 0
    for line in f:
        tokens = tokenize(line)
        total += evaluate(tokens)
        print(line.strip(),'=', evaluate(tokens))

print('Total:', total)
