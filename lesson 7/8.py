#Написать программу калькулятор которая предлагает 
#ввести пример для решения пока пользователь не введет команду "стоп"
#Программа должна решить пример и запросить следующий.
#При вводе команды "стоп" программа завершается.
#Поддерживаемые операции: + - * ** /
#Пример:
#    Введите пример или 'стоп' для завершения: 2 + 2
#    Ответ: 4
#    Введите пример или 'стоп' для завершения: 16 / 8
#    Ответ: 2
#    Введите пример или 'стоп' для завершения: 1651+
#    Неправильный формат. Пример: '2 + 4'


#eval() exec() нельзя


def calculate(expression: str):
    """Вычисляет выражение вида 'число оператор число'."""
    parts = expression.split()
    if len(parts) != 3:
        return None, "Неправильный формат. Пример: '2 + 4'"

    left, op, right = parts

    # Проверка чисел
    if not (left.replace('.', '', 1).isdigit() and right.replace('.', '', 1).isdigit()):
        return None, "Ошибка: нужно вводить числа."

    left = float(left)
    right = float(right)

    # Поддерживаемые операции
    if op == '+':
        return left + right, None
    elif op == '-':
        return left - right, None
    elif op == '*':
        return left * right, None
    elif op == '/':
        if right == 0:
            return None, "Ошибка: деление на ноль."
        return left / right, None
    elif op == '**':
        return left ** right, None
    else:
        return None, f"Оператор '{op}' не поддерживается."


def main():
    print("Простой калькулятор. Введите пример или 'стоп' для завершения.")
    while True:
        expr = input("Введите пример или 'стоп' для завершения: ").strip()
        if expr.lower() == "стоп":
            print("Работа завершена.")
            break

        result, error = calculate(expr)
        if error:
            print(error)
        else:
            # Если результат целое число, выводим без .0
            if result.is_integer():
                print(f"Ответ: {int(result)}")
            else:
                print(f"Ответ: {result}")


if __name__ == "__main__":
    main()