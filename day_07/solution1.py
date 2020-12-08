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

def get_possible_parent_bags(bag_type, rules):
    parent_bags = []
    edge_bags = [bag_type]
    while len(edge_bags) > 0:
        starting_edge_bag_count = len(edge_bags)
        for b in range(starting_edge_bag_count):
            for rule_subject, requirements in rules:
                if edge_bags[b] in map(lambda r: r[1], requirements) and rule_subject not in parent_bags:
                    parent_bags.append(rule_subject)
                    edge_bags.append(rule_subject)
        
        for b in range(starting_edge_bag_count-1, -1, -1):
            del edge_bags[b]

    return parent_bags

rules = load_rules(sys.argv[1])
print( len(get_possible_parent_bags('shiny gold', rules)) )