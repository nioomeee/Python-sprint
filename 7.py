# You have a sentence: title = "Python is cool".

# Split it into words.

# Join them back together with dashes - to make a URL slug.

# Print the final string in lowercase. (Bonus points if you chain .lower() at the end!).

# Target Output: python-is-cool

s = "Python is cool"

s_list = s.split()

print(s_list)

new_s = "-".join(s_list)
print(new_s.lower())