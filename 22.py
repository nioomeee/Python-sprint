# You have a date string: s = "2026-02-14".

# Parse it into a datetime object using strptime (Format is %Y-%m-%d).

# Print it in this format: "14-02-2026" (Day-Month-Year).
from datetime import datetime

s = "2026-02-14"
dt = datetime.strptime(s, "%Y-%m-%d")

print(dt)

print(dt.strftime("%d-%m-%Y"))
