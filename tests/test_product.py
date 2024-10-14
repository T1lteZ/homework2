import pytest
from src.product import Product


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
def sum_1(first_product, second_product):
    return 2580000.0


@pytest.fixture
def product_():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


@pytest.fixture
def product_s():
    return Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )


def test_product_init(product_):
    assert product_.name == "Iphone 15"
    assert product_.description == "512GB, Gray space"
    assert product_.price == 210000.0
    assert product_.quantity == 8


def test_samsung(product_s):
    assert product_s.name == "Samsung Galaxy S23 Ultra"
    assert product_s.description == "256GB, Серый цвет, 200MP камера"
    assert product_s.price == 180000.0
    assert product_s.quantity == 5


def test_product_str(first_product, second_product):
    assert str(first_product) == "Samsung, 180000.0 руб. Остаток: 5 шт."
    assert str(second_product) == "Iphone 15, 210000.0 руб. Остаток: 8 шт."


def test_product_add(first_product, second_product, sum_1):
    assert sum_1 == 2580000.0
