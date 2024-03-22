"""
У нас есть класс TextProcessor, который содержит в себе методы для работы с текстом.

Задания:
    1. Создайте класс AdvancedTextProcessor, который будет наследником TextProcessor.
    2. Переопределите метод summarize у класса AdvancedTextProcessor таким образом, чтобы он возвращал еще и количество слов в тексте.
       Например: Total text length: 67, total number of words in the text: 10
    3. Создайте экземпляры каждого из двух классов и у каждого экземпляра вызовите все возможные методы.
"""
from faker import Faker

class TextProcessor:
    def __init__(self, text: str) -> None:
        self.text = text

    def to_upper(self) -> str:
        return self.text.upper()

    def summarize(self) -> str:
        return f'Total text length: {len(self.text)}'
    
class AdvancedTextProcessor(TextProcessor):
    def summarize(self) -> str:
        text_length=super().summarize()
        words_count=len(self.text.split())
        return f"{text_length} total number of words in the text: {words_count}"


if __name__ == '__main__':
    fake = Faker()
    processed_text = TextProcessor(text=fake.text())
    print(processed_text.to_upper())
    print(processed_text.summarize())

    advanced_text = AdvancedTextProcessor(text=fake.text())
    print(advanced_text.summarize())