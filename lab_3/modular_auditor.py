inventory = 0
failed_entries = 0
user_input = ""

def get_valid_input(failed_entries = 0):
    user_input = input("Enter a stock quantity: ")
    
    if user_input == "quit":
        return user_input, failed_entries

    if user_input.isdigit():
        user_input = int(user_input)
        return user_input, failed_entries

    elif user_input.startswith("-") and user_input.replace("-", "", 1).isdigit():
        print("No negative number in user input")
        failed_entries += 1
        return get_valid_input(failed_entries)

    else:
        print("User input is not a integer")
        failed_entries += 1
        return get_valid_input(failed_entries)


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
    valid_input, fails = get_valid_input()
    failed_entries += fails

    if valid_input == "quit":
        generate_report(inventory, failed_entries) 
        break

    inventory = process_delivery(inventory, valid_input)
    tax = calculate_tax(inventory)

    if inventory > 500:
        print("Inventory exceed 500 units")
        break