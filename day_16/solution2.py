import sys
import re

def load_tickets(filename):
    with open(filename) as f:
        field_reqs = []
        my_ticket = None
        other_tickets = []

        def parse_ticket(ticket_line):
            return list( map(int, ticket_line.split(',')) )

        for line in f:
            if re.match(r'[a-z ]+: [0-9a-z\- ]+', line):
                field_name = line.split(': ')[0]
                reqs = []
                for m in re.finditer(r'(\d+)-(\d+)', line):
                    req_min, req_max = m.groups([1,2])
                    req_min = int(req_min)
                    req_max = int(req_max)
                    reqs.append( (req_min, req_max) )
                
                field_reqs.append( (field_name, reqs) )
            
            elif re.match(r'your ticket:', line):
                my_ticket = parse_ticket( f.readline() )
            
            elif re.match( r'nearby tickets:', line ):
                while True:
                    try:
                        other_tickets.append( parse_ticket(f.readline()) )
                    except:
                        break
        
        return {
            'field_reqs': field_reqs,
            'my_ticket': my_ticket,
            'other_tickets': other_tickets
        }

def invalid_values(ticket, field_reqs):
    bad_vals = []
    for ticket_field in ticket:
        field_is_bad = True
        for _, reqs in field_reqs:
            for req_min, req_max in reqs:
                if req_min <= ticket_field and req_max >= ticket_field:
                    field_is_bad = False
                    break
                if not field_is_bad:
                    break

        if field_is_bad:
            bad_vals.append( ticket_field )
        
    return bad_vals

def only_valid_tickets(tickets, field_reqs):
    valid_tickets = []
    for ticket in tickets:
        if len(invalid_values(ticket, field_reqs)) == 0:
            valid_tickets.append( ticket )
    
    return valid_tickets

def extract_column(tickets, col):
    vals = []
    for ticket in tickets:
        vals.append( ticket[col] )
    
    return vals

def column_meets_reqs(column, reqs):
    for val in column:
        meets_reqs = False
        for req_min, req_max in reqs:
            if val >= req_min and val <= req_max:
                meets_reqs = True
                break
        if not meets_reqs:
            return False
    
    return True

def deduce_fields(tickets, cols, field_reqs, possible_cols={}):
    # Returns a permutation of cols such that: 
    # colums_meets_reqs( extract_column(tickets, cols[i]), field_reqs[i]) == True for all i
    if len(cols) == 0:
        return cols
    
    if possible_cols == {}:
        for field_name, reqs in field_reqs:
            for c in range(len(tickets[0])):
                column = extract_column(tickets, c)
                if column_meets_reqs(column, reqs):
                    if field_name not in possible_cols:
                        possible_cols[field_name] = []
                    possible_cols[field_name].append( c )
    
    for i in range(len(cols)):
        if cols[i] in possible_cols[field_reqs[0][0]]:
            new_cols = cols[:i] + cols[i+1:]
            down_stream_result = deduce_fields(tickets, new_cols, field_reqs[1:], possible_cols)
            if down_stream_result != None:
                return [ cols[i] ] + down_stream_result

    return None




notes = load_tickets(sys.argv[1])
valid_tickets = only_valid_tickets(notes['other_tickets'], notes['field_reqs'])
print(f'Found {len(valid_tickets)} valid tickets')
deduced_fields = deduce_fields(valid_tickets, list(range(len(valid_tickets[0]))), notes['field_reqs'])

product = 1
for i in range(len(notes['field_reqs'])):
    if 'departure' in notes['field_reqs'][i][0]:
        product *= notes['my_ticket'][deduced_fields[i]]

print(product)