# Дан словарь наблюдения за температурой 
# {"day1":18, "day2":22, "day3":7, "day4":11, "day5":14}. 
# Отсортировать словарь по температуре в порядке возрастания и обратно.


temps = {"day1": 18, "day2": 22, "day3": 7, "day4": 11, "day5": 14}

# сортировка по значениям (температуре) в порядке возрастания
sorted_asc = dict(sorted(temps.items(), key=lambda item: item[1]))

# сортировка по значениям (температуре) в порядке убывания
sorted_desc = dict(sorted(temps.items(), key=lambda item: item[1], reverse=True))

# вывод результатов
print("Исходный словарь:", temps)
print("По возрастанию:", sorted_asc)
print("По убыванию:", sorted_desc)