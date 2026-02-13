# Create a dictionary called scores with two people: "Donald": 95 and "Mickey": 90.

# Print Donald's score.

# Bonus: Add a new person, "Goofy", with a score of 98. (Hint: dict[key] = value).

scores = {
    "Donald" : 95,
    "Mickey" : 90
}

print(scores.get("Donald"))

scores["Goofy"] = 98

print(scores.get("Goofy"))