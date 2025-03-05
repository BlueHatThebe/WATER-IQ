number = int(input("Please enter a number: "))

def get_operators():
    if number == 0:
        print("The number entered is zero and is not allowed!")
    elif number % 2 == 0 and number > 0:
        print("The number is even and positive")
    elif number % 2 == 0 and number < 0:
        print("The number is even and negative")
    elif number % 2 != 0 and number > 0:
        print("The number is odd and positive")
    elif number % 2 != 0 and number < 0:
        print("The number is odd and negative")

get_operators()