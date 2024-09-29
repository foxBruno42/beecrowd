nums = []
for x in range(100):
	nums.append(int(input()))
print(f"{max(nums)}")
print(f"{nums.index(max(nums))+1}")