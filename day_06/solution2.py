import sys

def unanimous_chars_from_group(group):
    unanimous_chars = []
    for char in group[0]:
        unanimous = True
        for answer_string in group:
            if char not in answer_string:
                unanimous = False
                break
        if unanimous:
            unanimous_chars.append( char )
    
    return unanimous_chars

def load_answers(file_name):
    answer_strings = []
    current_group = []
    with open(file_name) as f:
        for line in f:
            if line.strip() == '':
                answer_strings.append( ''.join(sorted(unanimous_chars_from_group(current_group))) )
                current_group = []
                continue
            current_group.append(line.strip())
        
        if len(current_group) != 0:
            answer_strings.append( ''.join(sorted(unanimous_chars_from_group(current_group))) )
        
    return answer_strings

reduced_answer_count = 0
for answer_string in load_answers(sys.argv[1]):
    reduced_answer_count += len(answer_string)

print(reduced_answer_count)