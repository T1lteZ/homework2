import pytest
from src.product import Product


@pytest.fixture
def product_():
    return Product("Iphone 15", "512GB, Gray space", 210000.0, 8)


def test_product_init(product_):
    assert product_.name == "Iphone 15"
    assert product_.description == "512GB, Gray space"
    assert product_.price == 210000.0
    assert product_.quantity == 8
