# regex

# symbols:
# \d -> digit (0, 9)
# \w -> word (letters, numbers, _)
# + -> one or more

import re

text = "Order #541 cost $20 yesterday."

numbers = re.findall(r'\d+', text)

print(numbers)


