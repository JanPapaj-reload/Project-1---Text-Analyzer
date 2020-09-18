input = input("Enter the time: ").strip()
split_input = input.split(":")

if int(split_input[0]) in range(12,24):
    converted_time = int(split_input[0]) - 12
    print("Converted time:", converted_time, ":", split_input[1], "PM")
else:
    print("Converted time:", int(split_input[0]), ":", int(split_input[1]), "AM")











