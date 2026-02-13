# You have a list of students and their marks:
# results = [("Amy", 88), ("Ben", 92), ("Cat", 75), ("Dan", 92)]

# Sort them by marks (Index 1) in Descending order (Highest to Lowest).

# Print the name of the winner (the first person in the sorted list).

results = [("Amy", 88), ("Ben", 92), ("Cat", 75), ("Dan", 92)]

results.sort(key = lambda x: x[1], reverse = True)
print(results)

print(f"Highest marks scored by: {results[0]}")