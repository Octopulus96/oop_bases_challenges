"""
У нас есть класс Product, который содержит в себе информацию о продукте.
Еще у нас есть класс AlcoholProduct, но метод is_available для него не подходит, так как
алкоголь нельзя продавать с 5 утра до 11 вечера

Задания:
    1. Переопределите метод is_available в классе AlcoholProduct с использованием super()
    2. is_available у AlcoholProduct должен возвращать False если сейчас часы между 5 утра и 11 вечера.
       Для определения текущего часа можно использовать datetime.now().hour
    3. Создайте экземпляр класса AlcoholProduct и проверьте, можно ли сейчас продавать алкоголь.
"""
from datetime import datetime, time

class Product:
    def __init__(self, title: str, price: float, stock_quantity: int) -> None:
        self.title = title
        self.price = price
        self.stock_quantity = stock_quantity

    def get_discounted_price(self, discount_percentage: float) -> int | float:
        return self.price * (1 - discount_percentage / 100)

    def is_available(self) -> bool:
        return self.stock_quantity > 0
    
class AlcoholProduct(Product):
    def is_available(self) -> bool:
        if (time(23, 0, 0) <= datetime.now().time() < time(5, 0, 0)) is False:
            return False
        else:
            return super().is_available()


if __name__ == '__main__':
    alcohol_product = AlcoholProduct("vine", 83, 21)
    print(alcohol_product.is_available())

