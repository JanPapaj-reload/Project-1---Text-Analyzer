# star wedge
size = int(input("Choose a number between 6 and 20: "))

for num in range(size):
    while num < round(size/2):
        print(num * "*")
    else:
        i = 2
        print((num-i) * "*")
        i += 2
print()

