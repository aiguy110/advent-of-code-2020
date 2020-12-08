import sys
import re

def load_rules(filename):
    rules = []
    with open(filename) as f:
        for line in f:
            m = re.match(r'(.*?) bags contain (.*)\.$', line.strip())
            subject_str, requirements_str = m.groups([1,2])
            
            if requirements_str == 'no other bags':
                rules.append( (subject_str, []) )
                continue
            
            requirements = []
            for m in re.finditer(r'(\d+) (.*?) bag', requirements_str):
                num_bags, bag_type = m.groups([1,2])
                num_bags = int(num_bags)
                requirements.append( (num_bags, bag_type) )
            
            rules.append( (subject_str, requirements) )

    return rules 

def get_nested_bags_dict(rules):
    total_bags_inside = {}
    while len(total_bags_inside) < len(rules):
        for subject_bag, requirements in rules:
            if subject_bag in total_bags_inside:
                continue
            
            subject_bags_inside = 0
            for n, child_bag_type in requirements:
                if child_bag_type in total_bags_inside:
                    subject_bags_inside += n * ( total_bags_inside[child_bag_type] + 1 )
                else:
                    break
            else:
                total_bags_inside[subject_bag] = subject_bags_inside
    
    return total_bags_inside


rules = load_rules(sys.argv[1])
nested_bags_dict = get_nested_bags_dict(rules)
print( nested_bags_dict['shiny gold'] )