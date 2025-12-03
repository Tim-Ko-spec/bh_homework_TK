# Написать рекурсивную функцию, которая вычисляет  
# факториал переданного в нее числа.


def factorial(n: int) -> int:
    """
    Рекурсивная функция для вычисления факториала числа n.
    Факториал определяется как:
    n! = n * (n-1) * (n-2) * ... * 1
    """
    if n < 0:
        raise ValueError("Факториал определён только для неотрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
print(factorial(0))
print(factorial(7))