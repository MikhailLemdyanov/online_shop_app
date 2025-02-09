import pytest

from src.product import Product
from src.category import Category

@pytest.fixture
def product_iphone():
    return Product("iPhone 15 Pro Max", "1Tb", 200000, 20)


@pytest.fixture
def product_huawei():
    return Product("Huawei 7S", "512Gb", 30000, 14)


@pytest.fixture
def category_phone(product_huawei, product_iphone):
    return Category("Смартфоны", "Умные телефоны", [product_iphone, product_huawei])

