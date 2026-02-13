# sort() vs sorted()

# list.sort() sorts in place and forever
# sorted(list) created new sorted list (leaves old one alone)

nums = [5, 1, 9, 3]

new_list = sorted(nums)

print(f"New list: {new_list}, \n Old list: {nums}")


nums.sort()
print(f"Sorting og list: {nums}")

# descending
nums.sort(reverse=True)
print(f"Sorted list in descending: {nums}")

# key:value pairs or (name, score) tuples => python sorts by key by default

# key = lambda item: item[index]

players = [("Donald", 95), ("Mickey", 82), ("Goofy", 98)]

# Sort by SCORE (Index 1), Descending (Highest First)
players.sort(key = lambda x: x[1], reverse = True)

print(players)
