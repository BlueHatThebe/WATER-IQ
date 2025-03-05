numbers_list = [2, 4, 6, 720, 8, 10, 41, 12, 14, 16, 360, 18, 20, 980]

largest_number = numbers_list[0]


for number in numbers_list:
    if number > largest_number:
        largest_number = number

print("The largest number in the list is:", largest_number)