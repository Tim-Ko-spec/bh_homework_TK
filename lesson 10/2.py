# Написать генератор factorial, который возвращает подряд значения факториала

# Например:

# factorial_gen = factorial()

# next(factorial_gen) -> 1
# next(factorial_gen) -> 2
# next(factorial_gen) -> 6
# next(factorial_gen) -> 24


def factorial():
    """
    Генератор факториалов.
    Возвращает последовательные значения: 1, 2, 6, 24, ...
    """
    n = 1
    fact = 1
    while True:
        fact *= n
        yield fact
        n += 1


factorial_gen = factorial()

print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))
print(next(factorial_gen))