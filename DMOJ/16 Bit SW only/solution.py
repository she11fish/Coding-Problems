N = int(input())
nums = []
for i in range(N):
    nums.append(input().split(" "))

for i in range(N):
    if (int(nums[i][0]) * int(nums[i][1]) == int(nums[i][2])):
        print("POSSIBLE DOUBLE SIGMA")
        continue
    print("16 BIT S/W ONLY")
    