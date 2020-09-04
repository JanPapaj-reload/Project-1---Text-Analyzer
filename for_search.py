text = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.'''

# je potreba!! znovu vytvorit promennou "text", ktera mezitim volanim funkce "split" zanikla!
text = list(text.split(" "))

target = input("Which word should I look for?").strip(",./- ")

# iterovani skrz "text" pomoci funkce "enumerate", ktera vytvari tuply index-prvek a proto se pro hledani indexu prvku v klekci hodi skvele
for index, word in enumerate(text):
    if word.strip(".,") == target:
        print(f"The index of your word is: {index + 1}")

# ask user for sequence of integers, use 'q' to quit from asking user for next number
total = 0
while True:
    reply = input("Insert a number (or 'q' to quit):  ").lower().strip()
    if reply != "q":
        total += int(reply)
        continue
    else:
        print("Total:", total)
        break

# get maximum, minimum and average of the integers in a list without a build in functions
list = [1,3,5,8,9,45,21,0,3]
max = 1
min = 1
total = 0
for num in list:
    if num > max:
        max = num
        continue
print("Max:", max)

for num in list:
    if num < min:
        min = num
print("Min:", min)

for num in list:
    total += num
average = round(total / len(list), 2)
print("Average:", average)

# create immutable copy a list and clear original data


# BONUS: can you also print the indexes of maximum and minimum?
list = [1,3,5,8,9,45,21,0,3]
max = 1
min = 1
for i, num in enumerate(list):
    if num > max:
        max = num
        index = i
        continue
print("The index of max value:", index)
for i, num in enumerate(list):
    if num < min:
        min = num
        index = i
        continue
print("The index of min value:", index)
