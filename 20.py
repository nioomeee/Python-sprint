# I want you to print the first 10 Fibonacci numbers.

# Initialize a = 0 and b = 1.

# Print a.

# Loop 9 more times.

# Inside the loop:

# Print b.

# Update a and b using the one-line swap: a, b = b, a + b

a, b = 0, 1

print(a)

for i in range(1, 10):
    print(b)
    a, b = b, a+b

