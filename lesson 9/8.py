# Дан список содержащий в себе различные типы данных, отфильтровать таким
# образом, чтобы 
#  - остались только строки.
#  - остался только логический тип.


# исходный список с разными типами данных
data = [1, "hello", True, 3.14, "world", False, None, 42, "python"]

# Оставить только строки
only_strings = list(filter(lambda x: isinstance(x, str), data))

# Оставить только логический тип (bool)
only_bools = list(filter(lambda x: isinstance(x, bool), data))

print("Исходный список:", data)
print("Только строки:", only_strings)
print("Только логический тип:", only_bools)