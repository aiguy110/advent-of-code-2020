import sys
import re

input_pattern = re.compile(r'(\d+)-(\d+) ([a-z]): ([a-z]+)')
valid_count = 0
with open(sys.argv[1]) as f:
    for line in f:
        match = input_pattern.match(line)
        min_chars, max_chars, char, password = match.groups([1,2,3,4])
        min_chars = int(min_chars)
        max_chars = int(max_chars)
        char_count = password.count(char)
        if char_count >= min_chars and char_count <= max_chars:
            valid_count += 1

print(valid_count)