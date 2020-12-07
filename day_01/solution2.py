import sys

nums = []
with open(sys.argv[1]) as f:
    for line in f:
        nums.append(int(line))
N = len(nums)

for a in range(N):
    for b in range(a+1, N):
        for c in range(b+1, N):
            if nums[a] + nums[b]+ nums[c] == 2020:
                print(nums[a] * nums[b] * nums[c])
                exit()