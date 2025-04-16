
fruits = {
    "apple": 2.5,
    "banana": 1.8,
    "orange": 2.0,
    "mango": 3.5,
    "grape": 2.5
}

def question1():
    fruit_names = list(fruits.keys())
    print("List of fruit names:", fruit_names)
    
    unique_prices = set(fruits.values())
    print("Set of unique prices:", unique_prices)
    
    
    fruit_tuples = list(fruits.items())
    print("List of (fruit, price) tuples:", fruit_tuples)


def get_fruit_price():
    fruit_name = input("Enter a fruit name to get its price: ").lower()
    if fruit_name in fruits:
        print(f"The price of {fruit_name} is ${fruits[fruit_name]} per kg")
    else:
        print(f"{fruit_name} is not in the dictionary")

def add_fruit():
    new_fruit = input("Enter new fruit name: ").lower()
    new_price = float(input(f"Enter price per kg for {new_fruit}: "))
    fruits[new_fruit] = new_price
    print(f"Added {new_fruit} with price ${new_price}")

def update_fruit_price():
    update_fruit = input("Enter fruit name to update price: ").lower()
    if update_fruit in fruits:
        new_price = float(input(f"Enter new price for {update_fruit}: "))
        fruits[update_fruit] = new_price
        print(f"Updated price of {update_fruit} to ${new_price}")
    else:
        print(f"{update_fruit} not found in dictionary")

def print_all_fruits():
    print("\nAll fruits and their prices:")
    for fruit, price in fruits.items():
        print(f"{fruit}: ${price} per kg")


def question2():
    while True:
        print("\nFruit Price Manager Menu:")
        print("1. Get price of a fruit")
        print("2. Add a new fruit")
        print("3. Update price of a fruit")
        print("4. Print all fruits and prices")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            get_fruit_price()
        elif choice == "2":
            add_fruit()
        elif choice == "3":
            update_fruit_price()
        elif choice == "4":
            print_all_fruits()
        elif choice == "5":
            print("Exiting menu.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


print("Question 1 Results:")
question1()
print("\nQuestion 2 Results:")
question2()