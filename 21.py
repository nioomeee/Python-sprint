# date time
from datetime import datetime
# %d -> Day (14)
# %m -> Month(number) (02)
# %B -> Month (February)
# %Y -> Full year (2026)
# %A -> day of the week (Saturday)
# %H -> Hour(24 hour) (23)
# %M -> Minute (07)

# They give you a string, and you need to "read" it.

date_str = "14/02/2026"
dt = datetime.strptime(date_str, "%d/%m/%Y")

print(dt)

# They want the answer in a specific format like "Saturday, 14 February
print(dt.strftime("%A, %d %B"))

# 
