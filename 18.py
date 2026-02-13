n = 29
isPrime = True
limit = int(n ** 0.5) + 1

for i in range(2, limit):
    if n%i == 0:
        isPrime = False
        break

print(isPrime)
