'''
author =  Jan Papaj
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

import sys
split_text = []
text_selection = 0
approved = False

def line_separator():
    print("-"*50)


def login():
    login_attempt = 0
    print("Hello. Welcome to the app.")
    while login_attempt < 2:
        username = input("Please, type in your username: ").lower().strip(" ")
        password = input("And now your password: ").strip(" ")
        if username in dict_hesla.keys() and password == dict_hesla[username]:
            print("Welcome,", username,". Your login has been successful.")
            break
        login_attempt += 1
    else:
        print("Login credentials incorrect. Please, contact Helpdesk.")
        sys.exit()



# def text_select():
#     print("We have 3 texts to be analyzed.")
#     text_selection = input("Select a number 1-3 to choose a specific text: ")
#     try:
#         if str(text_selection.isalpha()) == True:
#             text_selection = input("You have to key in a number between 1 and 3: ")
#         elif not 1 <= int(text_selection) <= 3:
#             text_selection = input("You have to key in a number between 1 and 3: ")
#     except:
#         text_selection = input("Key in a NUMBER between 1 and 3: ")
#     print("Alright then, let's now crunch Text", text_selection, ".")


# def splitt_text(text_selection):
#     split_text = TEXTS[(text_selection - 1)]
#     split_text = split_text.replace(",.!?", " ")
#     split_text = split_text.split()
#     return split_text


def words_sum(split_text):
    result = len(split_text)
    print("There are", result, "words in that particular text")


def titlecase(split_text):
    result = 0
    for word in split_text:
        if word.istitle():
            result += 1
    print("There are", result, "titlecase words")


def uppercase(split_text):
    result = 0
    for word in split_text:
        if word.isupper():
            result += 1
    print("There are", result, "uppercase words")


def lowercase(split_text):
    result = 0
    for word in split_text:
        if word.islower():
            result += 1
    print("There are", result, "lowercase words")


def all_numeric(split_text):
    result = 0
    for numeric in split_text:
        if numeric.isnumeric():
            result += 1
    print("There are", result, "numeric words")

# tady jsem si nekonecne dlouho na webu pohledal mozna reseni. pokus/omyl :(
# snad me to teda aspon neco naucilo
def frequency(split_text):
    len_freq = {}
    for x in split_text:
        if len(x) in len_freq:
            len_freq[len(x)] += 1
        else:
            len_freq.setdefault(len(x), 1)
    grouped = list(len_freq.keys())
    grouped.sort()
    for y in grouped:
        print( y, "|", '*' * len_freq[y], len_freq[y])


def sum_numeric(split_text):
    result = 0
    for numeric in split_text:
        if numeric.isnumeric():
            result += int(numeric)
    print("If we sum up all numbers, we will get", float(result))


def text_analyzer(texts):
    line_separator()
    while login():
        return
    line_separator()
    # text_selection()    <- puvodne jsem chtel volat jako funkci,
    # v ramci celeho programku text_analyzer, ale motal jsem se v tom
    print("We have 3 texts to be analyzed")
    text_selection = int(input("Choose a number between 1-3: "))
    # pokousel jsem se osetrit alpha znaky na vstupu pomoci try/except, ale utopil jsem se.
    # zatim tedy tak, ac to blbuvzdorny neni. vim o tom
    while not 1 <= text_selection <= 3:
        text_selection = int(input(("It must be a NUMBER between 1 and 3! ")))
    else:
        print("Alright, let's crunch text", text_selection)
    line_separator()

    # splitt_text(text_selection)  <-  takto jsem funkci volal a interpreter to nevzal, viz lines 63-80

    split_text = texts[text_selection-1]
    split_text = split_text.replace(",.!?", " ")
    split_text = split_text.split()

    words_sum(split_text)
    titlecase(split_text)
    uppercase(split_text)
    lowercase(split_text)
    all_numeric(split_text)
    line_separator()
    frequency(split_text)
    line_separator()
    sum_numeric(split_text)
    line_separator()

# line 176 mi neustale vyhazuje jako chybovou. proc???
text_analyzer(TEXTS)
