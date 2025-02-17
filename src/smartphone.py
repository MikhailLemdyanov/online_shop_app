from src.product import Product


class Smartphone(Product):
    'Класс, описывающий категорию товаров Смартфон. Наследник класса Product'
    def __init__(self, name, description, price, quantity, effeciency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.effeciency == effeciency
        self.model == model
        self.memory == memory
        self.color == color
