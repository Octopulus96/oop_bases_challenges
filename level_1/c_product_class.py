"""
У любого продукта есть такие свойства: название, описание, цена, вес

Задания:
    1. Создайте класс продукта.
    2. Создайте экземпляр этого продукта и наполинте своими данными.
    3. Распечатайте о нем иформацию в таком виде: Информация о продукте: название, описание, цена, вес
"""

#Использовал немного другие параметры для продукта, но котекст тот же

from typing import Dict, Any
class Product:
    def __init__(self, name: str, description: str, price: float, size: int, color: str) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.size = size
        self.color = color

    def show_product_information(self) -> str:
        return ("Информация о продукте:\n{name}\n\n{description}{price}$\n{size}\n{color}".format(
            name = self.name,
            description = self.description,
            price = self.price,
            size = self.size,
            color = self.color
        ))

if __name__ == '__main__':
    shorts_product_information: Dict[str, Any] = {
        "product_details_name": "Dickies Skateboarding Regular Fit Cargo Shorts, 11",
        "description": """
    Dickies Skateboarding Cargo Shorts were built knowing your need for durable skate gear.
    The stretch ripstop fabrication allows for added movement in a durable construction that won’t rip or tear over time.
    An inseam gusset provides reinforced construction to avoid blow-outs while giving you a wider range of motion.
    The dual cargo pockets have been sewn down at the flap to keep your contents safe and secure while skating.
    Plus, a stay stitch at the rear pockets helps avoid bunching when you are active.
    Complete with Dickies Skateboarding interior red detailing and black herringbone pocket bags for comfort,
    these shorts also feature a strong metal button front closure that won’t give out when you bail.
    \n""",
    "price": 49.99,
    "waist": 32,
    "color": "Black (BKX)"}

    shorts = Product(**shorts_product_information)
    print(shorts.show_product_information())