from abc import ABC, abstractmethod
from src.product import Product
from src.category import Category


class Mixin:
    def __init__(self):
        print(f"Product('{self.name}', '{self.description}', {self.price}, {self.quantity})")
        super().__init__()


class BaseProduct(ABC):
    @classmethod
    @abstractmethod
    def new_product(cls, *args, **kwargs):
        pass


class Smartphone(Product, Mixin):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
