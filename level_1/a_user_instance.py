"""
Задания:
    1. Создайте экземпляр класса юзера, наполнив любыми данными.
    2. Распечатайте информацию о нем в таком виде: Информация о пользователе: имя, юзернэйм, возраст, телефон.
"""


class User:
    def __init__(self, name: str, username: str, age: int, phone: str):
        self.name = name
        self.username = username
        self.age = age
        self.phone = phone


if __name__ == '__main__':
    account = User("Valentine", "Octopulus96", 27, "+44 (323) 257-8854")
    a = account
    print(f"Информация о пользователе: {a.name}, {a.username}, {a.age}, {a.phone}.")
