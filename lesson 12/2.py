# Создать класс BookCard, в классе должны быть:

# - private атрибут author - автор (тип str)
# - private атрибут title - название книги (тип str)
# - private атрибут year - год издания (тип int)
# - магический метод __init__, который принимает author, title, year
# - магические методы сравнения для сортировки книг по году издания
# - сеттеры и геттеры к атрибутам author, title, year. В сеттерах сделать проверку
#   на тип данных, если тип данных не подходит, то бросить ValueError. Декущего ля года
#   издания дополнительно проверить на валидность (> 0, <= тгода).

# Аксессоры реализоваться через property.


from functools import total_ordering
import datetime


@total_ordering
class BookCard:
    def __init__(self, author: str, title: str, year: int):
        self.author = author
        self.title = title
        self.year = year

    # author
    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise ValueError("author должен быть строкой")
        self.__author = value

    # title
    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise ValueError("title должен быть строкой")
        self.__title = value

    # year
    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if not isinstance(value, int):
            raise ValueError("year должен быть целым числом")

        current_year = datetime.datetime.now().year
        if not (0 < value <= current_year):
            raise ValueError(f"year должен быть в диапазоне 1..{current_year}")

        self.__year = value

    # сравнение по году 
    def __eq__(self, other):
        return self.year == other.year

    def __lt__(self, other):
        return self.year < other.year

    # строковое представление 
    def __str__(self):
        return f"{self.author} — «{self.title}», {self.year}"

books = [
    BookCard("Толстой", "Война и мир", 1869),
    BookCard("Достоевский", "Идиот", 1868),
    BookCard("Булгаков", "Мастер и Маргарита", 1967),
]

print("Сортировка по году:")
for b in sorted(books):
    print(b)

print("\nСамая новая книга:")
print(max(books))
