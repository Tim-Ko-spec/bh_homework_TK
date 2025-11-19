#Дан список
#['samsung', 'lg', 'xerox', 'bosch']
#Удалить элемент с именем 'xerox'
#Добавить элемент на 2 место 'indesit'

brands = ['samsung', 'lg', 'xerox', 'bosch']

# Удаляем элемент 'xerox'
if 'xerox' in brands:
    brands.remove('xerox')

# Добавляем 'indesit' на 2-е место (индекс 1)
brands.insert(1, 'indesit')

print("Обновлённый список брендов:", brands)