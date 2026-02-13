# counter from collections

from collections import Counter

votes = ["Mickey", "Donald", "Goofy", "Mickey", "Goofy", "Mickey", "Donald", "Goofy", "Mickey"]

counts = Counter(votes)

print(counts)