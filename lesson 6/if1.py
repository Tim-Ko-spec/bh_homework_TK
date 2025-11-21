#Запросить у пользователя год рождения и в соответствии с его возрастом 
#охарактеризовать пользователя - 
#ребенок, подросток, юноша, в расцвете сил, пожилой, старик.

from datetime import datetime

# Запрос года рождения
birth_year = int(input("Введите ваш год рождения: "))

# Определяем текущий год
current_year = datetime.now().year

# Вычисляем возраст
age = current_year - birth_year

# Определяем категорию по возрасту
if age < 12:
    category = "ребенок"
elif age < 18:
    category = "подросток"
elif age < 25:
    category = "юноша"
elif age < 45:
    category = "в расцвете сил"
elif age < 65:
    category = "пожилой"
else:
    category = "старик"

# Вывод результата
print(f"Ваш возраст: {age}. Вы — {category}.")