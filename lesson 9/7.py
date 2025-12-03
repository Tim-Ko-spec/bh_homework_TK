# Дан список пользователей след. формата: 
# [{"name":"some_name", "login":"some_login", "password":"some_password" },
#  ...
# ]

# Отфильтровать используя функцию filter() список на предмет паролей 
# которые менее 5 символов.

# *Отфильтровать используя функцию filter() список на предмет валидных логинов. 
# Валидный логин должен содержать только латинские буквы, цифры и черту подчеркивания. 
# Каждому пользователю с плохим логином вывести текст 
# "Уважаемый user_name, ваш логин user_login не является корректным."


import re

users = [
    {"name": "Иван", "login": "ivan_123", "password": "12345"},
    {"name": "Петр", "login": "petr!", "password": "qwe"},
    {"name": "Ольга", "login": "olga", "password": "abcdef"},
    {"name": "Сергей", "login": "sergey_99", "password": "pass"},
]

# Фильтрация по паролям (менее 5 символов)
weak_passwords = list(filter(lambda u: len(u["password"]) < 5, users))

print("Пользователи с короткими паролями (<5 символов):")
for u in weak_passwords:
    print(f"{u['name']} -> пароль: {u['password']}")

# Фильтрация по валидным логинам
# Валидный логин: только латинские буквы, цифры и _
pattern = re.compile(r'^[A-Za-z0-9_]+$')

valid_logins = list(filter(lambda u: pattern.match(u["login"]), users))
invalid_logins = list(filter(lambda u: not pattern.match(u["login"]), users))

print("\nПользователи с валидными логинами:")
for u in valid_logins:
    print(f"{u['name']} -> логин: {u['login']}")

print("\nСообщения для пользователей с плохими логинами:")
for u in invalid_logins:
    print(f"Уважаемый {u['name']}, ваш логин {u['login']} не является корректным.")