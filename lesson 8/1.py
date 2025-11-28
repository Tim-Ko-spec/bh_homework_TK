# Написать функцию  которая принимает фамилию имя и отчество одной стройкой, 
# а возвращает в виде краткого формата. 
# Функция должна содержать необязательный параметр в виде логического значения 
# и в зависимости от него возвращала ФИО в двух следующих форматах:
#  -  Николаев И.С. 
#  -  И.С.Николаев


def format_fio(full_name: str, reverse: bool = False) -> str:
    """
    Принимает ФИО одной строкой и возвращает краткий формат.
    :param full_name: строка вида 'Фамилия Имя Отчество'
    :param reverse: если False -> 'Фамилия И.О.', если True -> 'И.О.Фамилия'
    :return: строка в кратком формате
    """
    parts = full_name.strip().split()
    if len(parts) != 3:
        raise ValueError("Введите ФИО в формате: 'Фамилия Имя Отчество'")
    
    surname, name, patronymic = parts
    initials = f"{name[0]}.{patronymic[0]}."
    
    if reverse:
        return f"{initials}{surname}"
    else:
        return f"{surname} {initials}"

print(format_fio("Николаев Иван Сергеевич"))       
print(format_fio("Николаев Иван Сергеевич", True)) 