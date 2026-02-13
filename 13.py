# You have a messy log string: log = "User_101: Error, User_505: Success, User_303: Fail"

# I want you to:

# Extract all the User IDs (the numbers).

# Print the list of IDs.

# Hint: Use re.findall() with the pattern for "one or more digits".

import re

log = "User_101: Error, User_505: Success, User_303: Fail"

ids = re.findall(r'\d+', log)

print(ids)