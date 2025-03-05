def isLongerThan(input_string):
    if len(input_string) > 5:
        return True
    else:
        print("It does not contain 5 characters")
        return False

user_input = input("Enter a string: ")

result = isLongerThan(user_input)

if result:
    print("The string has more than 5 characters")