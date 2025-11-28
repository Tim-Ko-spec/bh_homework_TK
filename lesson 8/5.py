# Написать функцию count_char, которая принимает строковое значение,
# из которого создает и возвращает словарь, следующего вида:
# {'буква': 'количество-вхождений-в-строку'}
# Нельзя пользоваться collections.Counter!


def count_char(text: str) -> dict:
    """
    Принимает строку и возвращает словарь вида:
    {'буква': количество-вхождений-в-строку}
    """
    try:
        if not isinstance(text, str):
            raise ValueError("Аргумент должен быть строкой")

        result = {}
        for ch in text:
            if ch in result:
                result[ch] += 1
            else:
                result[ch] = 1

        return result

    except ValueError as e:
        return {"Ошибка": str(e)}
    except Exception as e:
        return {"Ошибка": f"Непредвиденная ошибка: {e}"}

if __name__ == "__main__":
    user_input = input("Введите строку: ")
    dictionary = count_char(user_input)
    print("Результат:", dictionary)
