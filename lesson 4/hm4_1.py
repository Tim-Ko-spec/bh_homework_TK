phrase = input("Введите фразу: ")

char_count = len(phrase)
print(f"Количество символов: {char_count}")

words = phrase.split()
word_count = len(words)
print(f"Количество слов: {word_count}")

vowels = "аеёиоуыэюяaeiou"  
vowel_count = sum(phrase.lower().count(vowel) for vowel in vowels)
print(f"Количество гласных: {vowel_count}")