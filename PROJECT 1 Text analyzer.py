'''
author = Jan Papaj
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
text_selection = 0
def line_separator():
    print("-"*50)


def login():
    print("Hi there. Long time no see.")
    # 2. username and password, stripped of potential whitespaces and uppercase
    username = input("Type in your username: ").lower().strip(" ")
    password = input("And now your password: ").lower().strip(" ")
    # 3. membership test for name and password
    while username not in dict_hesla.keys():
        username = input("This username is not registered. Try inserting it again: ").lower().strip()
    while password != dict_hesla[username]:
        password = input("The password is not valid. Try inserting it again: ").lower().strip()
    print("Username:", username)
    print("Password:", password)


def text_select(text_selection):
    print("We have 3 texts to be analyzed.")
    text_selection = input("Select a number 1-3 to analyze a specific text: ")
    try:
        if str(text_selection.isalpha()) == True:
            text_selection = input("You have to key in a number between 1 and 3: ")
        elif not 1 <= int(text_selection) <= 3:
            text_selection = input("You have to key in a number between 1 and 3: ")
    except:
        text_selection = int(input("Key in a NUMBER between 1 and 3: "))
    print("Alright then, let's now crunch Text", text_selection, ".")


def split_Text(x):
    global split_text
    split_text = TEXTS[text_selection]
    split_text = split_text.replace(",.!?", " ")
    split_text = split_text.split()
    return split_text


def words_sum(split_text):
    result = len(list(split_text))
    print("There are", result, "words.")
    return result


def titlecase(split_text):
    result = 0
    for word in split_text:
        if word.istitle():
            result += 1
    print(f"There are {result} titlecase words in the text.")
    return result


def uppercase(split_text):
    result = 0
    for word in split_text:
        if word.isupper():
            result += 1
    print(f"There are {result} uppercase words in the text.")
    return result


def lowercase(split_text):
    result = 0
    for word in split_text:
        if word.islower():
            result += 1
    print(f"There are {result} lowercase words in the text.")
    return result


def sum_numeric(split_text):
    result = 0
    for word in split_text:
        if word.isnumeric():
            result += int(word)
    print(f"If we sum up all numbers there, we will get {float(result)}.")
    return float(result)


def text_analyzer(texts):
    line_separator()
    login()
    line_separator()
    text_select(text_selection)
    line_separator()
    split_Text(text_select)
    words_sum(split_text)
    titlecase(split_text)
    uppercase(split_text)
    lowercase(split_text)
    line_separator()
    sum_numeric(split_text)
    line_separator()


text_analyzer(TEXTS)









