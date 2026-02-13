# You have the exam date: exam_date = datetime(2026, 2, 17).
# You have today's date (hardcode it): today = datetime(2026, 2, 13).

# I want you to:

# Calculate the difference (exam_date - today).

# Print the number of days left. (Hint: access .days).
from datetime import datetime, timedelta

exam_date = datetime(2026, 2, 17)
today = datetime(2026, 2, 13)

diff = exam_date - today
print(diff.days)
