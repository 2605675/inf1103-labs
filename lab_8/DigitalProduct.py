from Product import Product
from supplier import Supplier


class DigitalProduct(Product):
    def __init__(
        self,
        product_id: str,
        name: str,
        price: float,
        stock: int,
        download_size: float,
        supplier: Supplier,
    ) -> None:
        super().__init__(product_id, name, price, stock, supplier)
        self.__download_size: float = download_size

    def display_information(self) -> str:
        return (
            f"ID: {self.product_id} | Name: {self.name} | "
            f"Price: ${self.price:.2f} | Stock: {self.stock} | "
            f"Download size: {self.__download_size}\n"
            f"{self.display_supplier()}"
        )

    def get_fulfilment_info(self) -> str:
        return "Product is delivered digitally"

    def to_dict(self) -> dict:
        data = super().to_dict()
        data["download_size"] = self.__download_size
        return {"Digital": data}
