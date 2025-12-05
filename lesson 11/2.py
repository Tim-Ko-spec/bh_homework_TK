# Создать класс Student.


# Определить атрибуты:
#     - surname - фамилия
#     - name - имя
#     - group - номер группы
#     - grads - список оценок

# Определить методы:
#     - инициализатор __init__
#     - Методы __eq__, __ne__, __lt__, __gt__, __le__, __ge__, которые будут сравнивать
#     студентов по среднему баллу
#     - метод add_grade - добавляет в список оценок одну или несколько оценок от 1 до 10
#     - метод average_grade -считает и возвращает среднюю оценку ученика

# Создать список из 5 студентов класса и вывести его отсортированным по возрастанию
# и убыванию.

# Вывести студентов, у которых средний балл больше 8


class Student:
    def __init__(self, surname, name, group, grads=None):
        self.surname = surname
        self.name = name
        self.group = group
        self.grads = grads if grads is not None else []

    # ---------- сравнение по среднему баллу ----------
    def average_grade(self):
        return sum(self.grads) / len(self.grads) if self.grads else 0

    def __eq__(self, other):
        return self.average_grade() == other.average_grade()

    def __ne__(self, other):
        return self.average_grade() != other.average_grade()

    def __lt__(self, other):
        return self.average_grade() < other.average_grade()

    def __gt__(self, other):
        return self.average_grade() > other.average_grade()

    def __le__(self, other):
        return self.average_grade() <= other.average_grade()

    def __ge__(self, other):
        return self.average_grade() >= other.average_grade()

    # ---------- добавление оценок ----------
    def add_grade(self, *grades):
        for g in grades:
            if 1 <= g <= 10:
                self.grads.append(g)
            else:
                print(f"Оценка {g} игнорируется — должна быть от 1 до 10")

    # ---------- строковое представление ----------
    def __str__(self):
        return f"{self.surname} {self.name}, группа {self.group}, ср. балл: {self.average_grade():.2f}"


# Создаём список студентов
students = [
    Student("Иванов", "Пётр", "9А", [9, 8, 10]),
    Student("Сидоров", "Антон", "9А", [6, 7, 5]),
    Student("Кузнецова", "Мария", "9А", [10, 9, 9]),
    Student("Орлов", "Илья", "9А", [8, 8, 7]),
    Student("Громова", "Алина", "9А", [9, 10, 10]),
]

# Добавим оценки (пример)
students[1].add_grade(10, 9)

# Сортировка по возрастанию
print("Сортировка по возрастанию среднего балла:")
for s in sorted(students):
    print(s)

# Сортировка по убыванию
print("\nСортировка по убыванию среднего балла:")
for s in sorted(students, reverse=True):
    print(s)

# Студенты со средним баллом > 8
print("\nСтуденты со средним баллом > 8:")
for s in students:
    if s.average_grade() > 8:
        print(s)
