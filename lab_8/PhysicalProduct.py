from Product import Product
from CanBeShipped import CanBeShipped
from supplier import Supplier


class PhysicalProduct(Product, CanBeShipped):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        weight: float,
        supplier: Supplier,
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__weight: float = weight
        self.__cost: float = self.calculate_shipping_cost()

    def display_information(self) -> str:
        return (
            f"ID: {self.product_id} | Name: {self.name} | "
            f"Price: ${self.price:.2f} | Stock: {self.stock} | "
            f"Weight: {self.__weight} | Cost: {self.__cost}\n"
            f"{self.display_supplier()}"
        )

    def get_fulfilment_info(self) -> str:
        return "Product requires physical shipping"

    def calculate_shipping_cost(self) -> float:
        return self.__weight * 2

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["weight"] = self.__weight
        data["cost"] = self.__cost
        return {"Physical": data}
