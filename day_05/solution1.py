import sys

def decode_seat(seat_str):
    n = 0
    for i in range(len(seat_str)):
        n *= 2
        n += 1 if seat_str[i] in ['B', 'R'] else 0
    
    return (n // 8, n % 8, n)

highest_seat_id = -1
for line in open(sys.argv[1]):
    _, _, seat_id = decode_seat( line.strip() )
    if highest_seat_id < seat_id:
        highest_seat_id = seat_id

print(highest_seat_id)
