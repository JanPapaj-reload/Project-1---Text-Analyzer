
if text_selection == 1:
    # words total
    total_text1 = len(split_text1)
    print("In Text 1 there are", total_text1, "words,")
    # num of titlecased
    capital_text1 = []
    for item in split_text1:
        if item[0] in uppercase:
            capital_text1.append(item)
    print("of which", len(capital_text1), "are capitalized.")
    # num of uppercased
    uppercase_text1 = []
    for item in split_text1:
        if item.isupper() == True:
            uppercase_text1.append(item)
    print("There are also", len(uppercase_text1), "uppercase")
    # num of lowercased
    lowercase_text1 = []
    for item in split_text1:
        if item.islower() == True:
            lowercase_text1.append(item)
    print("and", len(lowercase_text1), "lowercase words.")
    # num of all-numeric
    numeric_text1 = []
    for item in split_text1:
        if item.isalnum():
            numeric_text1.append(item)
    print("Last but not least, there are", len(numeric_text1), "all-numeric strings.")
    line_separator()
    # graphic bar representation
    for item in split_text1:
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
    line_separator()
    # sum of all-numeric words
    sum_1 = 0
    for item in split_text1:
        if item.isdigit() is True:
            sum_1 += int(item)
    print("...and the sum of all numeric words here is", sum_1)

elif text_selection == 2:
    # words total
    total_text2 = len(split_text2)
    print("In Text 2 there are", total_text2, "words,")
    # num of titlecased
    capital_text2 = []
    for item in split_text2:
        if item[0] in uppercase:
            capital_text2.append(item)
    print("of which", len(capital_text2), "are capitalized.")
    # num of uppercased
    uppercase_text2 = []
    for item in split_text2:
        if item.isupper() == True:
            uppercase_text2.append(item)
    print("There are also", len(uppercase_text2), "uppercase")
    # num of lowercased
    lowercase_text2 = []
    for item in split_text2:
        if item.islower() == True:
            lowercase_text2.append(item)
    print("and", len(lowercase_text2), "lowercase words.")
    # num of all-numeric
    numeric_text2 = []
    for item in split_text2:
        if item.isalnum():
            numeric_text2.append(item)
    print("Last but not least, there are", len(numeric_text2), "all-numeric strings.")
    line_separator()
    # graphic bar representation
    for item in split_text2:
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
    line_separator()
    # sum of numeric words
    sum_1 = 0
    for item in split_text2:
        if item.isdigit() is True:
            sum_1 += int(item)
    print("...and the sum of all numeric words here is", sum_1)

else:
    # words total
    total_text3 = len(split_text3)
    print("In Text 3 there are", total_text3, "words,")
    # num of titlecased
    capital_text3 = []
    for item in split_text3:
        if item[0] in uppercase:
            capital_text3.append(item)
    print("of which", len(capital_text3), "are capitalized.")
    # num of uppercased
    uppercase_text3 = []
    for item in split_text3:
        if item.isupper() == True:
            uppercase_text3.append(item)
    print("There are also", len(uppercase_text3), "uppercase")
    # num of lowercased
    lowercase_text3 = []
    for item in split_text3:
        if item.islower() == True:
            lowercase_text3.append(item)
    print("and", len(lowercase_text3), "lowercase words.")
    # num of all-numeric
    numeric_text1 = []
    for item in split_text3:
        if item.isalnum():
            numeric_text1.append(item)
    print("Last but not least, there are", len(numeric_text1), "all-numeric strings.")
    line_separator()
    # graphic bar representation
    for item in split_text3:
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
    line_separator()
    # sum of numeric words
    sum_1 = 0
    for item in split_text3:
        if item.isdigit() is True:
            sum_1 += int(item)
    print("...and the sum of all numeric words here is", sum_1)
line_separator()





# star wedge
input = int(input("Choose a number between 6 and 20: "))

if 5 < input < 21:
    for num in range(input):
        while num < round(input/2):
            print(num * "*")
        else:
            i = 2
            print((num-i) * "*")
            i += 2

