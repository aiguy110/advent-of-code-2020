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
            if re.match(r'[a-z]+: [0-9a-z\- ]+', line):
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

print( load_tickets(sys.argv[1]) )

