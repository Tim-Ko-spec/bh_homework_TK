#Даны 4 переменные - a1, a2, a3, a4.
#1 - вывести True если все они дробные числа
#2 - вывести True если одна из них строка
#3 - вывести True если  одна пара переменных является целочисленным типом. 
#    Пары могут образовать только следующие переменные - a1-a3, a2-a4, a3-a4"

a1 = 1.5
a2 = "hello"
a3 = 3
a4 = 4

# 1. Все ли переменные дробные (float)
all_float = all(isinstance(x, float) for x in (a1, a2, a3, a4))
print("Все дробные:", all_float)

# 2. Есть ли хотя бы одна строка
has_string = any(isinstance(x, str) for x in (a1, a2, a3, a4))
print("Есть строка:", has_string)

# 3. Проверка пар на целочисленный тип
pair_int = (
    (isinstance(a1, int) and isinstance(a3, int)) or
    (isinstance(a2, int) and isinstance(a4, int)) or
    (isinstance(a3, int) and isinstance(a4, int))
)
print("Есть целочисленная пара:", pair_int)