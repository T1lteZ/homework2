import pytest
from src.product import Product
from src.category import Category


@pytest.fixture
def first_product():
    return Product(
        name="Samsung",
        description="256GB, Серый цвет, 200MP камера",
        price=180000.0,
        quantity=5,
    )


@pytest.fixture
def second_product():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def category_():
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, "
                    "но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
            Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
        ]
    )


@pytest.fixture
def category_2():
    return Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
                    "станет вашим другом и помощником",
        products=[
            Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
        ]
    )


@pytest.fixture
def str__(first_product, second_product):
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[first_product, second_product])


def test_category_init(category_, category_2):
    assert category_.name == "Смартфоны"
    assert category_.description == ("Смартфоны, как средство не только коммуникации, "
                                     "но и получения дополнительных функций для удобства жизни")
    assert len(category_.products) == 3

    assert category_.category_count == 2
    assert category_2.category_count == 2

    assert category_.product_count == 4
    assert category_2.product_count == 4


def test_category_str(str__):
    assert str(str__) == "Смартфоны, количество продуктов: 13 шт."


def test_category_middle_price(category_, category_2):
    assert category_.middle_price() == 140333.33333333334
    assert category_2.middle_price() == 123000


def test_category_middle_price_empty():
    cat = Category(
        name="Телевизоры",
        description="Современный телевизор, который позволяет наслаждаться просмотром, "
        "станет вашим другом и помощником",
        products=[],
    )
    assert cat.middle_price() == 0
