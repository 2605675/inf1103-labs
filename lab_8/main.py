from file_handle import file_handle
from Inventory import Inventory
from menu import menu
from supplier import Supplier
from PhysicalProduct import PhysicalProduct
from DigitalProduct import DigitalProduct

if __name__ == "__main__":
    # handler = file_handle()
    # my_inventory = Inventory()
    # app = menu(handler, my_inventory)
    
    sup = Supplier("1", "testsup", "test@gmail.com")
    test = PhysicalProduct("1", "test", 2000, 20, 20, sup)
    test1 = DigitalProduct("2", "test2", 2000, 20, 20, sup)
    # print(test.display_information())
    # print(test1.display_information())
    # print(sup.display_information())
    my_inventory = Inventory()
    my_inventory.add_product(test)
    my_inventory.add_product(test1)
    print(my_inventory.display_products())
    my_inventory.remove_product("1")
    print(my_inventory.display_products())
    print(test.display_information())
    