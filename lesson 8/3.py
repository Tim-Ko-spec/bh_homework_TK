# Написать функцию, которая вычисляет  факториал переданного в нее числа без рекурсии.


def factorial(n: int) -> int:
    """
    Вычисляет факториал числа n без рекурсии.
    :param n: целое число >= 0
    :return: факториал числа n
    """
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

if __name__ == "__main__":
    try:
        num = int(input("Введите число для вычисления факториала: "))
        print(f"Факториал числа {num} равен {factorial(num)}")
    except ValueError as e:
        print("Ошибка:", e)