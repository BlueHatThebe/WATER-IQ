def sort_characters(input_string, limit=10):
    characters = [char.strip() for char in input_string.split(',')]
    
    sorted_characters = sorted(characters)
    
    limited_characters = sorted_characters[:limit]
    
    return limited_characters

user_input = input("Enter characters separated by commas: ")

result = sort_characters(user_input)

print("Sorted characters (limited to 10):")
print(result)