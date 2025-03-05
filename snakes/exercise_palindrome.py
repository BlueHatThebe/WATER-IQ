def is_palindrome_string(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

def is_palindrome_number(num):
    num_str = str(abs(num))  
    return num_str == num_str[::-1]

def main():
    user_string = input("Enter a string to check if it's a palindrome: ")
    
    if is_palindrome_string(user_string):
        print(f"'{user_string}' is a palindrome!")
    else:
        print(f"'{user_string}' is not a palindrome.")
    
    
    while True:
        try:
            user_number = int(input("Enter a number to check if it's a palindrome: "))
            break
        except ValueError:
            print("Please enter a valid integer!")
    
    
    if is_palindrome_number(user_number):
        print(f"{user_number} is a palindrome!")
    else:
        print(f"{user_number} is not a palindrome.")

if __name__ == "__main__":
    main()