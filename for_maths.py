numbers = [1, 2, 3, 4, 5, 6, 10]

# sum all power of numbers in list
sum1 = 0
for number in numbers:
    sum1 += 2 ** number
print('Sum of all powers of numbers in list is '+ str(sum1))

# sum all power of numbers in list
sum2 = 0
for number in numbers:
    sum2 += number ** 2
print('Sum all power of numbers in list' + str(sum2))

# how many numbers are divisible by 2
evens = []
for number in numbers:
    if number % 2 == 0:
        evens.append(number)
print(len(evens))

# Matesovo reseni
result = 0
for num in numbers:
    result += bool(num % 2 == 0)

print(result)
