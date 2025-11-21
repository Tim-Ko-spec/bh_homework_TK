#Запросить фразу 
#    - вывести на экран количество уникальных символов
#    - вывести на экран количество уникальных слов
#    -* вывести символ который встречался чаще всего

from collections import Counter

phrase = input("Введите фразу: ")

# Количество уникальных символов
unique_chars = set(phrase)
print("Количество уникальных символов:", len(unique_chars))

# Количество уникальных слов
words = phrase.split()
unique_words = set(words)
print("Количество уникальных слов:", len(unique_words))

# Символ, который встречался чаще всего
counter = Counter(phrase)
most_common_char, freq = counter.most_common(1)[0]
print(f"Самый частый символ: '{most_common_char}', встречается {freq} раз(а)")