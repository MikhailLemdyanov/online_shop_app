import json

from settings import JSON_PATH
from src.category import Category
from src.product import Product


def read_json(file_path: str) -> dict:
    '''Функция, которая считывает json-файл'''

    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data

def data_processing(data: dict) -> list:
    '''Функция, которая принимает словарь с данными, создает объекты класса и возвращает их список'''
    categories = []
    for cat in data:
        products = []
        for product in cat ["products"]:
            products.append(Product(**product))
        cat["products"] = products
        categories.append(Category(**cat))

    return categories

if __name__ == '__main__':
    raw_data = read_json(JSON_PATH)
    categories_data = data_processing(raw_data)
    print(categories_data)