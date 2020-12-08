import sys

def load_answers(file_name):
    answer_strings = []
    current_group_set = set()
    with open(file_name) as f:
        for line in f:
            if line.strip() == '':
                answer_strings.append( ''.join(sorted(list(current_group_set))) )
                current_group_set = set()
            for char in line.strip():
                current_group_set.add(char)
        if len(current_group_set) != 0:
            answer_strings.append( ''.join(sorted(list(current_group_set))) )
    
    return answer_strings

reduced_answer_count = 0
for answer_string in load_answers(sys.argv[1]):
    reduced_answer_count += len(answer_string)

print(reduced_answer_count)