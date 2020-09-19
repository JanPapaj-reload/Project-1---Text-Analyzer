'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. ''',

'''At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.''',

'''The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''
]

dict_hesla = {
    "bob" : "123",
    "ann" : "pass123",
    "mike" : "password123",
    "liz" : "pass123",
}

# 1. Welcome to app
print("-" * 80)
print("Hi there. Long time no see.")

# 2. username and password, stripped of potential whitespaces and uppercase
username = input("Type in your username: ").lower().strip(" ")
password = input("And now your password: ").lower().strip(" ")

# 3. membership test for name and password
while username not in dict_hesla.keys():
    username = input("This username is not registered. Try inserting it again: ").lower().strip()
while password != dict_hesla[username]:
    password = input("The password is not valid either. Try inserting it again: ").lower().strip()
print("Username:", username)
print("Password:", password)

print("-" * 80)

# 4. text selection input
print("We have 3 texts to be analyzed.")
text_selection = int(input("Select a number 1-3 to choose a specific text: "))
print("Alright then, let's now crunch Text", text_selection,":")
print("-"*80)
# 5. text operations
# splitting the texts into iterable lists of strings, getting rid of commas and periods
split_text1_1 = TEXTS[0].replace(",", " ")
split_text1_2 = split_text1_1.replace(".", " ")
split_text1_3 = split_text1_2.split()

split_text2_1 = TEXTS[1].replace(",", " ")
split_text2_2 = split_text2_1.replace(".", " ")
split_text2_3 = split_text2_2.split()

split_text3_1 = TEXTS[2].replace(",", " ")
split_text3_2 = split_text3_1.replace(".", " ")
split_text3_3 = split_text3_2.split()

# variable for uppercase / lowercase membership test
uppercase = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
             "U", "V", "W", "X", "Y", "Z"]

# empty variables for word frequency bar representation
two_words = []
three_words = []
four_words = []
five_words = []
six_words = []
seven_words = []
eight_words = []
nine_words = []
ten_words = []
eleven_words = []
twelve_words = []
thirteen_words = []
fourteen_words = []
fourteen_plus_words = []

if text_selection == 1:
    # words total
    total_text1_3 = len(split_text1_3)
    print("In Text 1 there are", total_text1_3, "words,")
    # num of titlecased
    capital_text1_3 = []
    for item in split_text1_3:
        if item[0] in uppercase:
            capital_text1_3.append(item)
    print("of which", len(capital_text1_3),"are capitalized.")
    # num of uppercased
    uppercase_text1_3 = []
    for item in split_text1_3:
        if item.isupper() == True:
            uppercase_text1_3.append(item)
    print("There are also", len(uppercase_text1_3), "uppercase")
    # num of lowercased
    lowercase_text3_3 = []
    for item in split_text1_3:
        if item.islower() == True:
            lowercase_text3_3.append(item)
    print("and", len(lowercase_text3_3), "lowercase words.")
    # num of all-numeric
    numeric_text3_3 = []
    for item in split_text1_3:
        if item.isalnum():
            numeric_text3_3.append(item)
    print("Last but not least, there are", len(numeric_text3_3), "all-numeric strings.")
    print("-"*80)
    # graphic bar representation
    for item in split_text1_3:
        if len(item) == 2:
            two_words.append(item)
        elif len(item) == 3:
            three_words.append(item)
        elif len(item) == 4:
            four_words.append(item)
        elif len(item) == 5:
            five_words.append(item)
        elif len(item) == 6:
            six_words.append(item)
        elif len(item) == 7:
            seven_words.append(item)
        elif len(item) == 8:
            eight_words.append(item)
        elif len(item) == 9:
            nine_words.append(item)
        elif len(item) == 10:
            ten_words.append(item)
        elif len(item) == 11:
            eleven_words.append(item)
        elif len(item) == 12:
            twelve_words.append(item)
        elif len(item) == 13:
            thirteen_words.append(item)
        elif len(item) == 14:
            fourteen_words.append(item)
        else:
            fourteen_plus_words.append(item)
    print("2", len(two_words) * "*", len(two_words))
    print("3", len(three_words) * "*", len(three_words))
    print("4", len(four_words) * "*", len(four_words))
    print("5", len(five_words) * "*", len(five_words))
    print("6", len(six_words) * "*", len(six_words))
    print("7", len(seven_words) * "*", len(seven_words))
    print("8", len(eight_words) * "*", len(eight_words))
    print("9", len(nine_words) * "*", len(nine_words))
    print("10", len(ten_words) * "*", len(ten_words))
    print("11", len(eleven_words) * "*", len(eleven_words))
    print("12", len(twelve_words) * "*", len(twelve_words))
    print("13", len(thirteen_words) * "*", len(thirteen_words))
    print("14", len(fourteen_words) * "*", len(fourteen_words))
    print("14+", len(fourteen_plus_words) * "*", len(fourteen_plus_words))
    print("-"*80)
    # sum of all-numeric words
    sum_1 = 0
    for item in split_text1_3:
        if item.isdigit() is True:
            sum_1 += int(item)
    print("...and the sum of all numeric words here is", sum_1)

elif text_selection == 2:
    # words total
    total_text2_3 = len(split_text2_3)
    print("In Text 2 there are", total_text2_3, "words,")
    # num of titlecased
    capital_text2_3 = []
    for item in split_text2_3:
        if item[0] in uppercase:
            capital_text2_3.append(item)
    print("of which", len(capital_text2_3), "are capitalized.")
    # num of uppercased
    uppercase_text2_3 = []
    for item in split_text2_3:
        if item.isupper() == True:
            uppercase_text2_3.append(item)
    print("There are also", len(uppercase_text2_3), "uppercase")
    # num of lowercased
    lowercase_text2_3 = []
    for item in split_text2_3:
        if item.islower() == True:
            lowercase_text2_3.append(item)
    print("and", len(lowercase_text2_3), "lowercase words.")
    # num of all-numeric
    numeric_text2_3 = []
    for item in split_text2_3:
        if item.isalnum():
            numeric_text2_3.append(item)
    print("Last but not least, there are", len(numeric_text2_3), "all-numeric strings.")
    print("-" * 80)
    # graphic bar representation
    for item in split_text2_3:
        if len(item) == 2:
            two_words.append(item)
        elif len(item) == 3:
            three_words.append(item)
        elif len(item) == 4:
            four_words.append(item)
        elif len(item) == 5:
            five_words.append(item)
        elif len(item) == 6:
            six_words.append(item)
        elif len(item) == 7:
            seven_words.append(item)
        elif len(item) == 8:
            eight_words.append(item)
        elif len(item) == 9:
            nine_words.append(item)
        elif len(item) == 10:
            ten_words.append(item)
        elif len(item) == 11:
            eleven_words.append(item)
        elif len(item) == 12:
            twelve_words.append(item)
        elif len(item) == 13:
            thirteen_words.append(item)
        elif len(item) == 14:
            fourteen_words.append(item)
        else:
            fourteen_plus_words.append(item)
    print("2", len(two_words) * "*", len(two_words))
    print("3", len(three_words) * "*", len(three_words))
    print("4", len(four_words) * "*", len(four_words))
    print("5", len(five_words) * "*", len(five_words))
    print("6", len(six_words) * "*", len(six_words))
    print("7", len(seven_words) * "*", len(seven_words))
    print("8", len(eight_words) * "*", len(eight_words))
    print("9", len(nine_words) * "*", len(nine_words))
    print("10", len(ten_words) * "*", len(ten_words))
    print("11", len(eleven_words) * "*", len(eleven_words))
    print("12", len(twelve_words) * "*", len(twelve_words))
    print("13", len(thirteen_words) * "*", len(thirteen_words))
    print("14", len(fourteen_words) * "*", len(fourteen_words))
    print("14+", len(fourteen_plus_words) * "*", len(fourteen_plus_words))
    print("-" * 80)
    # sum of numeric words
    sum_1 = 0
    for item in split_text2_3:
        if item.isdigit() is True:
            sum_1 += int(item)
    print("...and the sum of all numeric words here is", sum_1)

else:
    # words total
    total_text3_3 = len(split_text3_3)
    print("In Text 3 there are", total_text3_3, "words,")
    # num of titlecased
    capital_text3_3 = []
    for item in split_text3_3:
        if item[0] in uppercase:
            capital_text3_3.append(item)
    print("of which", len(capital_text3_3), "are capitalized.")
    # num of uppercased
    uppercase_text3_3 = []
    for item in split_text3_3:
        if item.isupper() == True:
            uppercase_text3_3.append(item)
    print("There are also", len(uppercase_text3_3), "uppercase")
    # num of lowercased
    lowercase_text3_3 = []
    for item in split_text3_3:
        if item.islower() == True:
            lowercase_text3_3.append(item)
    print("and", len(lowercase_text3_3), "lowercase words.")
    # num of all-numeric
    numeric_text3_3 = []
    for item in split_text3_3:
        if item.isalnum():
            numeric_text3_3.append(item)
    print("Last but not least, there are", len(numeric_text3_3), "all-numeric strings.")
    print("-" * 80)
    # graphic bar representation
    for item in split_text3_3:
        if len(item) == 2:
            two_words.append(item)
        elif len(item) == 3:
            three_words.append(item)
        elif len(item) == 4:
            four_words.append(item)
        elif len(item) == 5:
            five_words.append(item)
        elif len(item) == 6:
            six_words.append(item)
        elif len(item) == 7:
            seven_words.append(item)
        elif len(item) == 8:
            eight_words.append(item)
        elif len(item) == 9:
            nine_words.append(item)
        elif len(item) == 10:
            ten_words.append(item)
        elif len(item) == 11:
            eleven_words.append(item)
        elif len(item) == 12:
            twelve_words.append(item)
        elif len(item) == 13:
            thirteen_words.append(item)
        elif len(item) == 14:
            fourteen_words.append(item)
        else:
            fourteen_plus_words.append(item)
    print("2", len(two_words) * "*", len(two_words))
    print("3", len(three_words) * "*", len(three_words))
    print("4", len(four_words) * "*", len(four_words))
    print("5", len(five_words) * "*", len(five_words))
    print("6", len(six_words) * "*", len(six_words))
    print("7", len(seven_words) * "*", len(seven_words))
    print("8", len(eight_words) * "*", len(eight_words))
    print("9", len(nine_words) * "*", len(nine_words))
    print("10", len(ten_words) * "*", len(ten_words))
    print("11", len(eleven_words) * "*", len(eleven_words))
    print("12", len(twelve_words) * "*", len(twelve_words))
    print("13", len(thirteen_words) * "*", len(thirteen_words))
    print("14", len(fourteen_words) * "*", len(fourteen_words))
    print("14+", len(fourteen_plus_words) * "*", len(fourteen_plus_words))
    print("-" * 80)
    # sum of numeric words
    sum_1 = 0
    for item in split_text3_3:
        if item.isdigit() is True:
            sum_1 += int(item)
    print("...and the sum of all numeric words here is", sum_1)
print("-"*80)


