from src.exceptions import ZeroQuantityError
from src.product import Product


class Category:
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        full_count = 0
        for product in self.__products:
            full_count += product.quantity
        return f"{self.name}, количество продуктов: {full_count} шт."

    @property
    def products_in_list(self):
        """Геттер, возвращающий приватный атрибут"""
        return self.__products

    def add_product(self, product):
        """Метод, добавляющий продукт в список и увеличивающий счетчик продуктов"""
        if isinstance(product, Product):
            try:
                if product.quantity == 0:
                    raise ZeroQuantityError("Нельзя добавить товар с нулевым количеством")
            except ZeroQuantityError as e:
                print(str(e))
            else:
                self.__products.append(product)
                Category.product_count += 1
                print("Товар добавлен успешно")
            finally:
                print("Обработка добавления товара завершена")
        else:
            raise TypeError

    @property
    def products(self):
        """Геттер, который выводит список товаров в виде строк"""
        prod_str = ""
        for product in self.__products:
            prod_str += f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
        return prod_str

    def middle_price(self):
        try:
            return round(sum([product.price for product in self.__products]) / len(self.__products), 1)
        except ZeroDivisionError:
            return 0
