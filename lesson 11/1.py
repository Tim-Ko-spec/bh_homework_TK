# Создать класс Phone, у которого будут следующие атрибуты:

# Определить атрибуты:

# - brand - бренд
# - model - модель
# - issue_year - год выпуска

# Определить методы:

# - инициализатор __init__
# - receive_call, который принимает имя звонящего и выводит на экран: 
#         <Бренд-Модель> - Звонит {name}
# - get_info, который будет возвращать кортеж (brand, model, issue_year)
# - метод __str__, который выводит на экран информацию об устройстве:
# Бренд: {}
# Модель: {}
# Год выпуска: {}


class Phone:
    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        print(f"<{self.brand}-{self.model}> - Звонит {name}")

    def get_info(self):
        return self.brand, self.model, self.issue_year

    def __str__(self):
        return (
            f"Бренд: {self.brand}\n"
            f"Модель: {self.model}\n"
            f"Год выпуска: {self.issue_year}"
        )


phone1 = Phone("Samsung", "Galaxy S21", 2021)
phone2 = Phone("Apple", "iPhone 14", 2022)

print(phone1)
phone1.receive_call("Иван")

print(phone2.get_info())