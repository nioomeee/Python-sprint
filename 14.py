# counter from collections

from collections import Counter

votes = ["Mickey", "Donald", "Goofy", "Mickey", "Goofy", "Mickey", "Donald", "Goofy", "Mickey"]

counts = Counter(votes)

print(counts)

# top 2 winners

print(counts.most_common(2))
