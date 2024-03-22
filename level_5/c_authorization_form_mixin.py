"""
У нас есть класс формы и метод для валидации в нем. Мы хотим создать форму для авторизации, где нам важно чтобы юзернэйм
существовал в базе данных

Задания:
    1. Напишите логику метода valid_form в классе AuthorizationFormMixin таким образом, чтобы там была проверка и из
       класса Form и проверка на то что юзернэйм есть в списке USERNAMES_IN_DB. Нужно использовать super() в этом методе
    2. Создайте класс AuthorizationForm, который будет наследником и от Form и от AuthorizationFormMixin
    3. Создайте экземпляр класса AuthorizationForm и вызовите у него метод valid_form. Должны отрабатывать обе проверки:
       и на длину пароля и на наличия юзернэйма в базе
"""
USERNAMES_IN_DB = ['Alice_2023', 'BobTheBuilder', 'CrazyCoder', 'DataDiva', 'EpicGamer', 'JavaJunkie']


class Form:
    def __init__(self, username: str, password: str) -> None:
        self.username = username
        self.password = password

    def valid_form(self) -> bool:
        return len(self.password) > 8


class AuthorizationFormMixin:
    def valid_form(self) -> bool:
        # Проверка наличия юзернэйма в базе данных
        if self.username not in USERNAMES_IN_DB:
            return False
        # Вызов метода valid_form из базового класса
        return super().valid_form()

class AuthorizationForm(AuthorizationFormMixin, Form):
    pass


if __name__ == '__main__':
    # Создание экземпляра AuthorizationForm
    form = AuthorizationForm('Alice_2023', 'password123')
    # Проверка валидности формы
    print(form.valid_form()) # Должно вернуть True

    # Создание экземпляра AuthorizationForm с неверным юзернэймом
    form_invalid_username = AuthorizationForm('NotInDB', 'password123')
    # Проверка валидности формы
    print(form_invalid_username.valid_form()) # Должно вернуть False

    # Создание экземпляра AuthorizationForm с коротким паролем
    form_short_password = AuthorizationForm('Alice_2023', 'short')
    # Проверка валидности формы
    print(form_short_password.valid_form()) # Должно вернуть False