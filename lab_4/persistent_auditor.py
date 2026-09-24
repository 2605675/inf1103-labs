total = 0
failed_entries = 0
order_id = 0


def get_valid_input(failed_entries=0):
    input_product = input("Enter Product Name: ")

    if input_product == "quit":
        return input_product, 0, failed_entries
    elif len(input_product) == 0:
        return get_valid_input(failed_entries)

    input_quantity = input("Enter a stock quantity: ")

    if input_quantity == "quit":
        return input_product, input_quantity, failed_entries

    if input_quantity.isdigit():
        input_quantity = int(input_quantity)
        return input_product, input_quantity, failed_entries

    elif (
        input_quantity.startswith("-") and input_quantity.replace("-", "", 1).isdigit()
    ):
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


def load_inventory():
    try:
        with open("./lab_4/inventory.txt", mode="r") as file:
            total = int(file.readline().strip())
            inventory = [line.strip() for line in file]
            if inventory:
                order_id = int(inventory[-1].split(",", 1)[0])
            else:
                order_id = 0
    except FileNotFoundError:
        total = 0
        inventory = []
        order_id = 0

    return total, inventory, order_id


total, inventory, order_id = load_inventory()

print("Current Orders:\n")
for line in inventory:
    print(line)
print("")

while True:
    valid_product, valid_quantity, fails = get_valid_input()
    failed_entries += fails

    if valid_product == "quit" or valid_quantity == "quit":
        generate_report(total, failed_entries)
        break

    total = process_delivery(total, valid_quantity)
    if total > 500:
        print("Inventory exceed 500 units")
        break

    order_id += 1
    new_order = f"{order_id}, {valid_product}, {valid_quantity}"
    inventory.append(new_order)
    tax = calculate_tax(total)
    print("New Order Added:\n" + new_order + "\n\nOrder successfully saved to orders.txt")