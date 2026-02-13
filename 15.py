# You have a list of letters representing answers to a multiple-choice question:
# answers = ["A", "B", "A", "C", "A", "B", "A", "C", "C", "D"]

# I want you to:

# Use Counter to count them.

# Print the single most common answer (The winner!).
# Hint: most_common(1) returns a list with one tuple inside, like [('A', 4)]. You want the 'A'.

from collections import Counter

answers = ["A", "B", "A", "C", "A", "B", "A", "C", "C", "D"]

counts = Counter(answers)

print(counts)

first = (counts.most_common(1))

print(f"Most common answer in the list: {first[0][0]}")
