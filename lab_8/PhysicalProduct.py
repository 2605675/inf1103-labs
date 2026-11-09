from Product import Product
from CanBeShipped import CanBeShipped


class PhysicalProduct(Product, CanBeShipped):
    def __init__(self, product_id, name, price, stock, weight, supplier):
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight = weight
        self.__cost = self.calculate_shipping_cost()

    def display_information(self):
        info, supplier = super().display_information()
        print(f"{info} | Weight: {self.__weight} | Cost: {self.__cost}" f"\n{supplier}")

    def get_fufilment_info(self):
        return "Product requires physical shipping"

    def calculate_shipping_cost(self):
        cost = self.__weight * 2
        return cost

    def to_dict(self):
        data = super().to_dict()
        data["weight"] = self.__weight
        data["cost"] = self.__cost
    
        return {"Physical": data}
