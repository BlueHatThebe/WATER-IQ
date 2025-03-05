def print_numbers_skip_multiples():
    multiples_of_seven = []
    
    print("Numbers from 1 to 50 (skipping multiples of 7):")
    for num in range(1, 51):
        try:
            if num % 7 == 0:
                raise ValueError("Multiple of 7")
            print(num, end=" ")
        except ValueError:
            multiples_of_seven.append(num)
    
    print("\n")
    
    print("Multiples of 7 that were skipped:")
    for multiple in multiples_of_seven:
        print(multiple, end=" ")
    print()

print_numbers_skip_multiples()