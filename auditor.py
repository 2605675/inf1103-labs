inventory = 0
user_input = ""

while True:
    user_input = input("Enter a stock quantity: ")
    print(user_input[1:])
    if user_input == "quit":
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
        continue
    else:
        print("User input is not a integer")
        continue