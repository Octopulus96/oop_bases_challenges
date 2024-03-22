"""
У нас есть класс кредитного банковского аккаунта со свойствами: полное имя владельца и баланс.

Задания:
    1. Нужно вынести методы, которые не относится непосредственно к кредитам в отдельны класс BankAccount.
    2. CreditAccount нужно отнаследовать от BankAccount.
    3. Создать экземпляр класс BankAccount и вызвать у него каждый из возможных методов.
    4. Создать экземпляр класс CreditAccount и вызвать у него каждый из возможных методов.
"""

from faker import Faker 

class BankAccount:
    def __init__(self, owner_full_name: str, balance: float) -> None:
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, amount: float) -> None:
        self.balance += amount

    def decrease_balance(self, amount: float) -> None:
        self.balance -= amount


class CreditAccount(BankAccount):

    def is_eligible_for_credit(self) -> float:
        return self.balance > 1000


if __name__ == '__main__':
    fake = Faker()
    bank_customer = BankAccount(fake.name(), fake.random_int())
    bank_customer.increase_balance(fake.random_int())
    bank_customer.decrease_balance(fake.random_int())

    middle_manager = CreditAccount(fake.name(), fake.random_int())
    middle_manager.decrease_balance(fake.random_int())


