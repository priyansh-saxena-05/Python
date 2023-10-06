def countdown(n):
    while n > 0:
        yield n
        n -= 1

# Using the generator
for number in countdown(5):
    print(number)
