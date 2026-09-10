inventory = 0
user_input = ""

while True:
    user_input = input("Enter a stock quantity: ")

    if user_input == "quit":
        break

    if user_input.isdigit():
        stock = int(user_input)
    else:
        print("User input is not a integer")
        