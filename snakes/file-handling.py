import datetime

def validate_date(date_str):
    """Validate date format (YYYY-MM-DD)."""
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_entry():
    """Add a new diary entry to diary.txt."""
    while True:
        date = input("Enter the date (YYYY-MM-DD): ")
        if validate_date(date):
            break
        print("Invalid date format. Please use YYYY-MM-DD (e.g., 2025-04-16).")
    
    title = input("Enter the title: ")
    body = input("Enter the diary entry: ")
    
    entry = f"============== {date} ===============\nTitle: {title}\n{body}\n-----------------------------------------\n"
    
    with open("diary.txt", "a") as file:
        file.write(entry)

def view_entries():
    """Display all diary entries from diary.txt."""
    with open("diary.txt", "r") as file:
        content = file.read()
        print(content)

def search_entries():
    """Search diary entries for a keyword."""
    keyword = input("Enter a keyword to search: ").lower()
    
    with open("diary.txt", "r") as file:
        content = file.read()
        entries = content.split("-----------------------------------------\n")
        
        for entry in entries:
            if entry.strip() and keyword in entry.lower():
                print(entry.strip())
                print("-" * 20)

add_entry()
view_entries()
search_entries()