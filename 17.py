# palindrome check
# You have a word: word = "madam".

# I want you to:

# Write an if statement checking if word is equal to its reverse.

# Print "Palindrome!" if it is.

word = "madam"

if word == word[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")