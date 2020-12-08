import sys
import re

def load_passport_data(file_name):
    passports = []
    with open(file_name) as f:
        current_passport = {}
        for line in f:
            if line.strip() == '':
                passports.append( current_passport )
                current_passport = {}
                continue

            for kv_pair in line.strip().split():
                k, v = kv_pair.split(':')
                current_passport[k] = v
            
        if current_passport != {}:
            passports.append( current_passport )

    return passports

def is_valid(passport):
    required_fields = [
        ( 'byr', r'^\d{4}$', lambda x: (int(x) >= 1920) and (int(x) <= 2002) ),
        ( 'pid', r'^\d{9}$', lambda x: True ),
        ( 'eyr', r'^\d{4}$', lambda x: (int(x) >= 2020) and (int(x) <= 2030) ),
        ( 'hcl', r'^#[0-9a-f]{6}$', lambda x: True ),
        ( 'ecl', r'^(amb|blu|brn|gry|grn|hzl|oth)$', lambda x: True ),  
        ( 'iyr', r'^\d{4}$', lambda x: (int(x) >= 2010) and (int(x) <= 2020) ),
        ( 'hgt', r'^\d+(cm|in)$', lambda x: (int(x[:-2]) >= 150) and (int(x[:-2]) <= 193) if 'cm' in x else (int(x[:-2]) >= 59) and (int(x[:-2]) <= 76) )
    ]
    for req_field, field_regex, validation_fn in required_fields:
        if req_field not in passport:
            return False
        
        if not re.match(field_regex, passport[req_field]):
            return False
        
        if not validation_fn( passport[req_field] ):
            return False
    
    return True

passports = load_passport_data(sys.argv[1])
valid_count = 0
for passport in passports:
    if is_valid(passport):
        valid_count += 1

print(valid_count)