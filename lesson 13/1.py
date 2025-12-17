# Создать класс User с атрибутами:

# Свойства:
# 	- name - имя - содержит только буквы русского алфавита 
# 	- login - логин - может содержать  только латинские буквы цифры и черту подчеркивания быть не менее 6 символов
# 	- password - пароль - может содержать  только латинские буквы цифры. Обязательные условия: 
#                 содержит менее шести символов
#                 содержит строчную букву
#                 содержит заглавную букву
#                 содержит число
# 	- is_blocked - заблокирован
# 	- subscription_date - дата до какой действует подписка
# 	- subscription_mode - вид подписки (free, paid)


# Методы:
# 	- bloc - принимает логическое значение и помечает пользователя заблокированным 
# 	- check_subscr - может принимать аргумент в виде даты. Проверяет действует ли подписка на определенную дату. 
# 						Если дата не передана значит на дату проверки. 
# 						Возвращает  действует ли подписка, ее вид и сколько осталось дней.
# 	- change_pass - смена пароля и присваивание его в качестве действующего. 
# 						Пароль должен пройти валидацию. 
# 						Если пароль не был передан сгенерировать по правилам и вывести в консоль.
# 	- get_info - выводит информацию о пользователе если заблокирован то сообщает об этом.



# Создание объекта должно происходить  при передаче обязательных аргументов имя и логин и необязательного - пароль. 
# Логин и пароль должны быть проверен на валидность.
# Если пароль в конструктор не был передан он должен сгенерироваться на основании правил, и должен быть выведен на экран(консоль).
# При создании пользователя ему предоставляется пробная подписка сроком на 30 дней.
# При изменении даты подписки  вид подписки меняется на платный.
# Валидацию данных сделать через регулярные выражения


import re
import random
import string
from datetime import datetime, timedelta


class User:
    # ИНИЦИАЛИЗАЦИЯ
    def __init__(self, name: str, login: str, password: str | None = None):
        self.name = self.validate_name(name)
        self.login = self.validate_login(login)

        if password is None:
            password = self.generate_password()
            print(f"Сгенерирован пароль: {password}")

        self.password = self.validate_password(password)

        self.is_blocked = False
        self.subscription_date = datetime.now() + timedelta(days=30)
        self.subscription_mode = "free"

    # ВАЛИДАЦИЯ
    @staticmethod
    def validate_name(name: str):
        pattern = r"^[А-Яа-яЁё]+$"
        if not re.fullmatch(pattern, name):
            raise ValueError("Имя должно содержать только буквы русского алфавита")
        return name

    @staticmethod
    def validate_login(login: str):
        pattern = r"^[A-Za-z0-9_]{6,}$"
        if not re.fullmatch(pattern, login):
            raise ValueError("Логин должен содержать латинские буквы, цифры, '_' и быть не короче 6 символов")
        return login

    @staticmethod
    def validate_password(password: str):
        pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[A-Za-z0-9]{6,}$"
        if not re.fullmatch(pattern, password):
            raise ValueError(
                "Пароль должен содержать минимум 6 символов, строчную букву, заглавную букву и цифру"
            )
        return password

    # ГЕНЕРАЦИЯ ПАРОЛЯ
    @staticmethod
    def generate_password():
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits

        # гарантируем выполнение условий
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
        ]

        # добиваем до длины 8 случайными символами
        all_chars = lower + upper + digits
        password += random.choices(all_chars, k=5)

        random.shuffle(password)
        return "".join(password)

    # БЛОКИРОВКА 
    def bloc(self, value: bool):
        self.is_blocked = bool(value)

    # ПРОВЕРКА ПОДПИСКИ
    def check_subscr(self, date: datetime | None = None):
        if date is None:
            date = datetime.now()

        active = date <= self.subscription_date
        days_left = (self.subscription_date - date).days

        return active, self.subscription_mode, max(days_left, 0)

    # СМЕНА ПАРОЛЯ
    def change_pass(self, new_password: str | None = None):
        if new_password is None:
            new_password = self.generate_password()
            print(f"Сгенерирован новый пароль: {new_password}")

        self.password = self.validate_password(new_password)

    # ИНФОРМАЦИЯ
    def get_info(self):
        if self.is_blocked:
            return f"Пользователь {self.name} заблокирован."

        active, mode, days_left = self.check_subscr()

        return (
            f"Имя: {self.name}\n"
            f"Логин: {self.login}\n"
            f"Подписка: {mode}\n"
            f"Активна: {'да' if active else 'нет'}\n"
            f"Осталось дней: {days_left}"
        )

    # ИЗМЕНЕНИЕ ПОДПИСКИ 
    def set_subscription(self, new_date: datetime):
        self.subscription_date = new_date
        self.subscription_mode = "paid"

user = User("Максим", "Max_123")

print(user.get_info())

user.change_pass()
user.bloc(True)
print(user.get_info())

user.set_subscription(datetime.now() + timedelta(days=90))
print(user.check_subscr())
