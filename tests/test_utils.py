import pytest
from src.product import Product
from src.category import Category
from src.utils import Smartphone, LawnGrass


@pytest.fixture
def lawngrass1():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")


@pytest.fixture
def lawngrass2():
    return LawnGrass("Газонная трава 2", "Выносливая трава", 450.0, 15, "США", "5 дней", "Темно-зеленый")


@pytest.fixture
def smartphone1():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def smartphone2():
    return Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, 98.2, "15", 512, "Gray space")


def test_lawn_grass(lawngrass1, lawngrass2):

    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"

    assert lawngrass2.name == "Газонная трава 2"
    assert lawngrass2.description == "Выносливая трава"
    assert lawngrass2.price == 450.0
    assert lawngrass2.quantity == 15
    assert lawngrass2.country == "США"
    assert lawngrass2.germination_period == "5 дней"
    assert lawngrass2.color == "Темно-зеленый"


def test_add_lawn_grass(lawngrass1, lawngrass2):

    assert lawngrass1 + lawngrass2 == 16750.0


def test_add_lawn_grass_error(lawngrass1):

    with pytest.raises(TypeError):
        lawngrass1 + 1


def test_smartphone(smartphone1, smartphone2):
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.memory == 256
    assert smartphone1.color == "Серый"

    assert smartphone2.name == "Iphone 15"
    assert smartphone2.description == "512GB, Gray space"
    assert smartphone2.price == 210000.0
    assert smartphone2.quantity == 8
    assert smartphone2.efficiency == 98.2
    assert smartphone2.model == "15"
    assert smartphone2.memory == 512
    assert smartphone2.color == "Gray space"


def test_add_smartphone(smartphone1, smartphone2):

    assert smartphone1 + smartphone2 == 2580000.0


def test_add_smartphone_error(smartphone1):

    with pytest.raises(TypeError):
        smartphone1 + 1
