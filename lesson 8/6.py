# Напишите функцию yes_or_no, которая принимает список из целых чисел,
# а возвращает список из Yes или No для каждого элемента, 
# Yes - если число уже встречалось и No, если нет
# [1,2,3,1,4] => [no, no, no, yes, no]

# если в списке не все целые числа вернуть False.


def yes_or_no(numbers: list) -> list | bool:
    """
    Принимает список целых чисел.
    Возвращает список из 'yes' или 'no' для каждого элемента:
    - 'yes' если число уже встречалось ранее
    - 'no' если число встречается впервые
    Если в списке есть нецелые числа -> возвращает False
    """
    try:
        # Проверка, что все элементы — целые числа
        if not all(isinstance(n, int) for n in numbers):
            return False

        seen = set()
        result = []

        for n in numbers:
            if n in seen:
                result.append("yes")
            else:
                result.append("no")
                seen.add(n)

        return result

    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    try:
        
        user_input = input("Введите список чисел через пробел: ")
        numbers = [int(x) for x in user_input.split()]
        print("Результат:", yes_or_no(numbers))
    
    except ValueError:
        print("Ошибка: вводите только целые числа!")