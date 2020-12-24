import sys
import re

def load_rules_and_samples(filename):
    rules = []
    samples = []
    with open(filename) as f:
        # Load rules
        for line in f:
            if line.strip() == '':
                break
            
            terminal_match = re.match(r'\d+: \"([a-zA-Z])\"', line)
            if terminal_match:
                rules.append( terminal_match.group(1) )
                continue

            rules.append( [] )
            for super_string in re.finditer(r'[\d ]+', line[line.index(':')+1:]):
                rules[-1].append( tuple(map(int, super_string[0].strip().split(' '))) )

        # Load samples
        for line in f:
            samples.append( line.strip() )
    
    return rules, samples

def match_length(sample, rules, root_rule_ind=0):
    # Returns 0 if no match is possible. Else returns the number characters
    # from the beginning of sample were used in the match
    if len(sample) == 0:
        return 0
    
    if type(rules[root_rule_ind]) == str:
        if rules[root_rule_ind] == sample[0]:
            return 1
        else:
            return 0

    for super_string in rules[root_rule_ind]:
        i = 0
        for rule_ind in super_string:
            ml = match_length(sample[i:], rules, rule_ind)
            if ml == 0:
                break

            i += ml
        else:
            return i
    
    return 0

rules, samples = load_rules_and_samples(sys.argv[1])

match_count = 0
for sample in samples:
    ml = match_length(sample, rules)
    print('Match result (sample, match_length, match):', sample, ml, ml==len(sample))
    if ml == len(sample):
        match_count += 1

print(match_count)