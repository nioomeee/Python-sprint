# You have a number: num = 49.

# I want you to:

# Calculate the limit (square root of num).
# Hint: int(num ** 0.5) + 1

# Write a loop from 2 to that limit.

# If num is divisible by i (num % i == 0), print "Not Prime" and break.

# (Bonus: If the loop finishes without breaking, it's Prime—but let's just focus on finding the factor for now).

num = 53

limit = int(num ** 0.5) + 1

for i in range(2, limit):
    if num % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")