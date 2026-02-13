# You have a list of ID numbers with duplicates: ids = [101, 102, 101, 103, 102, 104].

# I want you to:

# Convert it to a Set to remove the duplicates.

# Print how many unique IDs there are. (Hint: use len()).

ids = [101, 102, 101, 103, 102, 104]

ids_set = set(ids)

print(f"Unique IDs: {ids_set}")

print(f"Number of uniue ids: {len(ids_set)}")