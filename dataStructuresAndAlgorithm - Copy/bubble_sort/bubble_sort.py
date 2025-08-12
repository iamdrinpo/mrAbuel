items = input("Enter numbers, letters, or words: ").split()
order = input("(asc/desc): ").lower()

nums = []
words = []

for i in items:
    if i.isdigit():
        nums.append(int(i))
    else:
        words.append(i)

# for numbers
for i in range(len(nums)):
    for j in range(len(nums) - 1):
        if (order == "asc" and nums[j] > nums[j+1]) or (order == "desc" and nums[j] < nums[j+1]):
            nums[j], nums[j+1] = nums[j+1], nums[j]

# letters, words -- based on their len
for i in range(len(words)):
    for j in range(len(words) - 1):
        if (order == "asc" and len(words[j]) > len(words[j+1])) or (order == "desc" and len(words[j]) < len(words[j+1])):
            words[j], words[j+1] = words[j+1], words[j]

print("Sorted:", nums + words)
