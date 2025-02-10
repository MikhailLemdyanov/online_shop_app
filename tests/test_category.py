def test_category_init(category_phone, product_iphone, product_huawei):
    assert category_phone.name == "Смартфоны"
    assert category_phone.description == "Умные телефоны"
    assert category_phone.products == [product_iphone, product_huawei]

    assert category_phone.category_count == 1
    assert category_phone.product_count == 2
