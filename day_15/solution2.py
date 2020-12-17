import sys

def load_nums(filename):
    with open(filename) as f:
        nums = []
        for s in f.readline().split(','):
            nums.append( int(s) )
    
    return nums

def get_next_num(last_num, history, n):
    if last_num in history:
        return n - history[last_num]
    else:
        return 0

start_nums = load_nums(sys.argv[1])
N = 30000000
progress = 0
n = 1
history = {}
last_num = start_nums[0]

while n < N:
    if n < len(start_nums):
        history[last_num] = n
        last_num = start_nums[n]
    else:
        next_num = get_next_num(last_num, history, n)
        history[last_num] = n
        last_num = next_num
    
    n += 1

    if round(n / N * 1000) != progress:
        progress = round(n / N * 1000)
        print(str(progress / 10)+'% ', end='\r')

print()
print(last_num)