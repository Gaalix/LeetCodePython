nums = [-17, -8, -5, 0, 1, 2, 3, 4, 5, 6, 7, 8]
posNums = 0
negNums = 0

for i in range(len(nums)):
    if nums[i] < 0:
        negNums += 1
    if nums[i] > 0:
        posNums += 1

max = max(posNums, negNums)

print(max)