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

    get_valid_input()

def process_delivery(current_total, new_value):
    current_total += new_value
    return current_total

def calculate_tax(amount):
    tax = amount * 0.10
    return tax

def generate_report(inventory, failed_entries):
    print("Total Units Processed: ", inventory)
    print("Number of Failed/Rejected Entries: ", failed_entries)  
    return

while True:
    valid_input = get_valid_input()

    if valid_input == "quit":
        generate_report(inventory, failed_entries) 
        break

    inventory = process_delivery(inventory, valid_input)
    tax = calculate_tax(inventory)

    if inventory > 500:
        print("Inventory exceed 500 units")
        break