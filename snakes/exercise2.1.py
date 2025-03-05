numbers = range(1, 51)

def even_numbers():
    for num in numbers:
        if num %2 == 0:
            print(num)

even_numbers()