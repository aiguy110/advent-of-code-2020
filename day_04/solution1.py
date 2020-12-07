import sys

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
            
    return passports

def is_valid(passport):
    required_fields = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'hgt']
    for req_field in required_fields:
        if req_field not in passport:
            return False
    
    return True

passports = load_passport_data(sys.argv[1])
valid_count = 0
for passport in passports:
    if is_valid(passport):
        valid_count += 1

print(valid_count)