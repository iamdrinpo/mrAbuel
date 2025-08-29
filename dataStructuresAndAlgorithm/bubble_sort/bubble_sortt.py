# import random 

# items = input("Enter numbers, letters, or words: ").split()
# order = input("(asc/desc): ").lower()

# nums = [int(i) for i in items if i.isdigit()]
# words = [i for i in items if not i.isdigit()]

# nums.sort(reverse=(order == "desc"))
# words.sort(key=len, reverse=(order == "desc"))

# print("Sorted:", nums + words)


words = ['apple, banana, cherry']
found = False

for word in words:
    if 'apple' in word:
        found = True
        break
print(f"{word} matched.")