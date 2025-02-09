class Product:
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


    def line(self):
        '''Выводит строку в заданном формате'''
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def summary_price(self, other):
        '''Складывает стоимость товаров определенной категории на складе'''
        return (self.quantity * self.price) + (other.quantity * other.price)