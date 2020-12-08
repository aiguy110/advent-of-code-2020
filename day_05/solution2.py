import sys

def decode_seat(seat_str):
    n = 0
    for i in range(len(seat_str)):
        n *= 2
        n += 1 if seat_str[i] in ['B', 'R'] else 0
    
    return (n // 8, n % 8, n)

seat_ids = []
for line in open(sys.argv[1]):
    _, _, seat_id = decode_seat( line.strip() )
    seat_ids.append( seat_id )

seat_ids.sort()
for i in range(1, len(seat_ids)):
    if seat_ids[i] - seat_ids[i-1] > 1:
        print(seat_ids[i]-1)
        