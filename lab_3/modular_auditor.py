inventory = 0
failed_entries = 0
user_input = ""

while True:
    user_input = input("Enter a stock quantity: ")
    if user_input == "quit":
        print("Total Units Processed: ", inventory)
        print("Number of Failed/Rejected Entries: ", failed_entries)
        break

    if user_input.isdigit():
        stock = int(user_input)
        inventory += stock
        if inventory > 500:
            print("Inventory exceed 500 units")
            break
        else:
            continue
    elif user_input.startswith("-") and user_input.replace("-", "", 1).isdigit():
        print("No negative number in user input")
        failed_entries += 1
        continue
    else:
        print("User input is not a integer")
        failed_entries += 1
        continue