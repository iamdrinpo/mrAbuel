items = input("Enter numbers, letters, or words: ").split()
order = input("(asc/desc): ").lower()

nums = [int(i) for i in items if i.isdigit()]
words = [i for i in items if not i.isdigit()]

# Sort numbers normally
nums.sort(reverse=(order == "desc"))

# Sort words by length
words.sort(key=len, reverse=(order == "desc"))

print("Sorted:", nums + words)