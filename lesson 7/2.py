#Запросить фразу состоящую минимум из трех слов. 
#Сформировать фразу из этих слов в которой каждая буква слова, 
#продублирована то количество раз, которое соответствует номеру позиции 
#данной буквы в слове этой буквы. 
#Например: Привет как дела => Прриииввввееееетттттт кааккк деелллаааа


def transform_word(word):
    """Преобразует слово: каждая буква повторяется по позиции в слове."""
    result = ""
    for i, char in enumerate(word, start=1):
        result += char * i
    return result

def main():
    while True:
        phrase = input("Введите фразу минимум из трёх слов: ").strip()
        words = phrase.split()
        if len(words) < 3:
            print("Ошибка: нужно минимум три слова.")
        else:
            break

    transformed_words = [transform_word(word) for word in words]
    transformed_phrase = ' '.join(transformed_words)
    print("Преобразованная фраза:")
    print(transformed_phrase)

if __name__ == "__main__":
    main()