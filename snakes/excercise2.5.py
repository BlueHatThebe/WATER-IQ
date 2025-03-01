def get_day_of_week():
    days = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    
    try:
        user_input = int(input("Enter a number (1-7): "))
        
        if 1 <= user_input <= 7:
            print(f"The day is {days[user_input]}")
        else:
            print("Invalid input! Please enter a number between 1 and 7.")
    except ValueError:
        print("Invalid input! Please enter a number.")

get_day_of_week()