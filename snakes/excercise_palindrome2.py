def is_palindrome(input_value):
    input_str = str(input_value)
    cleaned_str = input_str.replace(" ", "").lower()
    return cleaned_str == cleaned_str[::-1]

def main():
    user_input = input("Enter a string or an integer: ")
    

    if is_palindrome(user_input):
        print(f"'{user_input}' is a palindrome!")
    else:
        print(f"'{user_input}' is not a palindrome.")

if __name__ == "__main__":
    main()