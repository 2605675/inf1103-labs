from Product import Product
from CanBeShipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)
        self.__weight = weight
        self.__cost = self.calculate_shipping_cost()

    def display_information(self):
        return f" {super().display_information()} | Weight: {self.__weight} | Cost: {self.__cost}"

    def get_fufilment_info(self):
        print("Product requires physical shipping")
        return

    def calculate_shipping_cost(self):
        cost = self.__weight * 2
        return cost

    def to_dict(self):
        return {
            "Physical": {
                "product_id": super().get_product_id(),
                "name": super().get_name(),
                "price": super().get_price(),
                "stock": super().get_stock(),
                "weight": self.__weight,
                "cost": self.__cost,
            }
        }