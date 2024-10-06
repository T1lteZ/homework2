from src.product import Product


class Category:
    """Создание класса Категорий продукции"""
    name: str
    description: str
    products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        """Инициализация класса """
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)

    @property
    def products(self):
        return self.__products

    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def product_list(self):
        product_str = ""
        for product in self.products:
            product_str += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
        return product_str

    def __str__(self):
        all_quantity = 0
        for j in self.__products:
            all_quantity += j.quantity
        return f"{self.name}, количество продуктов: {all_quantity} шт."
