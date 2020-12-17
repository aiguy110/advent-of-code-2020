import sys

def load_nums(filename):
    with open(filename) as f:
        nums = []
        for s in f.readline().split(','):
            nums.append( int(s) )
    
    return nums

def get_next_num(nums):
    if nums.count(nums[-1]) == 1:
        return 0
    else:
        return nums[:-1][::-1].index(nums[-1]) + 1

nums = load_nums(sys.argv[1])
while len(nums) < 2020:
    nums.append( get_next_num(nums) )

print(nums[-1])