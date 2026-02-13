# time delta
# new_date = old_date + timedelta(days=X)

from datetime import datetime, timedelta

today = datetime.now()
future = today + timedelta(days=100)
past = today - timedelta(weeks = 2)

print(future.date())
print(past.date())

# subtraction
# delta = date2 - date1

date1 = datetime(2026, 2, 14)
date2 = datetime(2026, 1, 1)

diff = date1 - date2
print(diff.days)
