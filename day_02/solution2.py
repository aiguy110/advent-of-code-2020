import sys
import re

input_pattern = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')
valid_count = 0
with open(sys.argv[1]) as f:
    for line in f:
        match = input_pattern.match(line)
        char1_ind, char2_ind, char, password = match.groups([1,2,3,4])
        char1_ind = int(char1_ind) - 1 
        char2_ind = int(char2_ind) - 1
        if (password[char1_ind] == char) != (password[char2_ind] == char):
            valid_count += 1

print(valid_count)