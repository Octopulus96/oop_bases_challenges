"""
У нас есть класс банковского аккаунта со свойствами: полное имя владельца и баланс, но не реализован
метод, который увеличивает баланс.

Задания:
    1. Допишите логику в метод increase_balance, который должен увеличивать баланс банковского счета на значение income.
    2. Создайте экземпляр класса банковского счета и распечатайте баланс.
    3. Увеличьте баланс счета у экземпляра класса с помощью метода increase_balance и снова распечатайте текущий баланс.
"""


class BankAccount:
    def __init__(self, owner_full_name: str, balance: float):
        self.owner_full_name = owner_full_name
        self.balance = balance

    def increase_balance(self, income: float) -> float: 
        bank_statement = self.balance * income
        return bank_statement

if __name__ == '__main__':
    account = BankAccount("Makarov Valentine", 102.00)
    print(account.balance)
    print(account.increase_balance(50))
