import sys

nums = []
with open(sys.argv[1]) as f:
    for line in f:
        nums.append(int(line))

compliments = set()
for n in nums:
    if n in compliments:
        print( n * (2020-n) )
        exit()
    compliments.add( 2020-n )