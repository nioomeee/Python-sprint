# s1 = "race"
# s2 = "care"

# I want you to:

# Write an if statement that checks if they are anagrams using sorting.

# Print "Yes" or "No".
s1 = "race"
s2 = "care"
if sorted(s1) == sorted(s2):
    print("Yes")
else:
    print("No")