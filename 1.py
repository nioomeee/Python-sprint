# You have a list of strings: names = ["niomi", "malika", "vinay"].
# Create a new list called cap_names that only includes names longer than 5 letters, and make them all UPPERCASE.

names = ["Donald", "Mickey", "Goofy"]

cap_names = [name.upper() for name in names if len(name) > 5]

print(cap_names)