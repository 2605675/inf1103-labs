from CanBeShipped import CanBeShipped
from DigitalProduct import DigitalProduct
from Inventory import Inventory
from Order import Order
from Orderline import Orderline
from PhysicalProduct import PhysicalProduct
from Product import Product
from supplier import Supplier


# ---------------------------------------------------------
# Setup
# ---------------------------------------------------------
supplier = Supplier("1", "test", "test@gmail.com")
physical = PhysicalProduct("P1", "test", 50, 5, 2, supplier)
digital = DigitalProduct("P2", "test", 20, 10, 10, supplier)

print("Objects created:")
print(physical.display_information())
print(digital.display_information())


# ---------------------------------------------------------
# Test Association
# ---------------------------------------------------------
print("\nProduct and Supplier")
print(physical.display_supplier())
print(digital.display_supplier())
print(supplier.display_information())

print("Supplier and physical are separate objects:", supplier is not physical)
print("Supplier and digital are separate objects:", supplier is not digital)
print("Physical and digital are separate objects:", physical is not digital)
print("Supplier id:", id(supplier))
print("Physical id:", id(physical))
print("Digital id:", id(digital))

del supplier

print("\nDeleted supplier")
print(physical.display_supplier())
print(digital.display_supplier())



# ---------------------------------------------------------
# Test Aggregation
# ---------------------------------------------------------
print("\nInventory -> Product")
inventory_a = Inventory()
inventory_b = Inventory()

inventory_a.add_product(physical)

# Remove from A and add the same object to B.
inventory_a.remove_product("P1")
print("\ncheck if product still exits")
print(physical.display_information())

inventory_b.add_product(physical)

print("\nShow that product can still be used in another inventory")
print(inventory_b.find_product("P1").display_information())
print("Product removed from inventory A:", inventory_a.find_product("P1") is None)
print("Inventory B has the same Product object:", inventory_b.find_product("P1") is physical)
print("Product id:", id(inventory_b.find_product("P1")))
print("Original physical id:", id(physical))


# ---------------------------------------------------------
# Test Composition
# ---------------------------------------------------------
print("\nOrder -> OrderLine")
order = Order("O1")
order.add_order_line(physical, 2)
order.add_order_line(digital, 1)

order.display_order_line()
print("Order total:", order.calculate_total())

order2 = Order("O2")
order2.add_order_line(physical, 2)

line1 = order.order_lines[0]
line2 = order2.order_lines[0]

# The same Product is used, but each Order creates a separate OrderLine.
print("The orders use different OrderLine objects:", line1 is not line2)
print("Both OrderLines refer to the same Product:", line1.product is line2.product)

# The Order manages its own order lines; removing one does not destroy the Product.
order.remove_order_line(0)
order.display_order_line()

print("Product still exists after line removal:")
print(physical.display_information())


# ---------------------------------------------------------
# Polymorphism
# ---------------------------------------------------------
print("\nPolymorphism")
for product in [physical, digital]:
    information = product.display_information()
    fulfilment = product.get_fulfilment_info()

    print("\ndisplay_information: ", information)
    print("get_fulfilment_info: ", fulfilment)
