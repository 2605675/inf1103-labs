inventory = 0
failed_entries = 0
user_input = ""

def get_valid_input():
    user_input = input("Enter a stock quantity: ")
    if user_input == "quit":
        return user_input


    if user_input.isdigit():
        user_input = int(user_input)
        return user_input


    elif user_input.startswith("-") and user_input.replace("-", "", 1).isdigit():
        print("No negative number in user input")
        failed_entries += 1
        get_valid_input()

    else:
        print("User input is not a integer")
        failed_entries += 1
        get_valid_input()

    return

while True:
    valid_input = get_valid_input()
    
    # if valid_input == "quit":
    #     print("Total Units Processed: ", inventory)
    #     print("Number of Failed/Rejected Entries: ", failed_entries)

    # inventory += stock
    # if inventory > 500:
    #     print("Inventory exceed 500 units")