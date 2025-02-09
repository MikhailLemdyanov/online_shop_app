from src.product import Product

class Category:
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.category_count +=1
        Category.product_count += len(products)

    def line(self):
        full_count = 0
        for product in self.products:
            full_count += product.quantity
        return f'{self.name}, количество продуктов: {full_count} шт.'

    def add_product(self, product: Product):
        '''Метод, увеличивающий счетчик количества продуктов'''
        self.products.append(product)
        Category.product_count += 1