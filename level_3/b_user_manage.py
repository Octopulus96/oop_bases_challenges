"""
У нас есть класс UserManager, который содержит в себе спискок юзернэймов пользователей и может расширять этот список.

Задания:
    1. Создайте класс AdminManager, который будет наследником UserManager.
       У него должен быть свой уникальный метод ban_username, который по переданному в него юзернэйму будет удалять
       юзернэйм из списка. Если такого юзернэйма в списке нет - должно печататься сообщение: "Такого пользователя не существует."
    2. Создайте класс SuperAdminManager, который будет наследником AdminManager.
       У него должен быть свой уникальный метод ban_all_users, который будет удалять все юзернэймы из списка.
    3. Создайте экземпляры каждого из трех классов и у каждого экземпляра вызовите все возможные методы.
"""

from faker import Faker
class UserManager:
    def __init__(self) -> None:
        self.usernames: list[str] = []

    def add_user(self, username: str) -> None:
        self.usernames.append(username)

    def get_users(self) -> list[str]:
        return self.usernames
    
class AdminManager(UserManager):

    def ban_username(self, username: str) -> None | str: 
        if username in self.usernames:
            self.usernames.remove(username)
        else:   
            return f"Такого пользователя не существует."
        
class SuperAdminManager(AdminManager):

    def ban_all_users(self) -> None:
       self.usernames.clear()

if __name__ == '__main__':
    fake = Faker()
    # Создаём экземпляры каждого класса
    user_manager = UserManager()
    admin_manager = AdminManager()
    super_admin_manager = SuperAdminManager()

    # Добавляем юзернэймы
    user_manager.add_user(fake.name())
    user_manager.add_user(fake.name())
    admin_manager.add_user(fake.name())
    admin_manager.add_user(fake.name())
    super_admin_manager.add_user(fake.name())
    super_admin_manager.add_user(fake.name())

    # Вызываем методы
    admin_manager.ban_username(fake.name())
    admin_manager.ban_username(fake.name())
    super_admin_manager.ban_all_users()
