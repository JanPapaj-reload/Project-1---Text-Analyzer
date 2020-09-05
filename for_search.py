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
    else:
        print("The word has not been found.")
        break

# ask user for sequence of integers, use 'q' to quit from asking user for next number
total = 0
reply_list = []
while True:
    reply = input("Insert a number (or 'q' to quit):  ").lower().strip()
    if reply != "q":
        total += int(reply)
        reply_list.append(reply)
    else:
        print("Total:", total)
        break

# get maximum, minimum and average of the integers in a list without a build in functions
max = 0
min = 0
for num in list(map(int, reply_list)):
    if num > max:
        max = num
    elif num < min:
        min = num

print("Max:", max)
print("Min:", min)
average = round(total / len(reply_list), 2)
print("Average:", average)

# create immutable copy a list and clear original data
immutable = tuple(map(int, reply_list))
print(immutable)
reply_list.clear()

# BONUS: can you also print the indexes of maximum and minimum?
max = 0
min = 0
index_max = 0
index_min = 0
for i, num in enumerate(immutable):
    if num > max:
        max = num
        index_max = i
    elif num < min:
        min = num
        index_min = i
print("The index of max value:", index_max)
print("The index of min value:", index_min)
