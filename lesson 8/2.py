# Написать функцию которая принимает 2 стороны прямоугольника 
# и возвращает либо площадь либо периметр в зависимости от дополнительного параметра.


# Функция для вычисления площади
def area(a: float, b: float) -> float:
    return a * b

# Функция для вычисления периметра
def perimeter(a: float, b: float) -> float:
    return 2 * (a + b)

# Главная функция, которая выбирает, что возвращать
def rectangle(a: float, b: float, mode: str = "area") -> float | str:
    """
    Вычисляет площадь или периметр прямоугольника.
    :param a: первая сторона
    :param b: вторая сторона
    :param mode: 'area' или 'perimeter'
    :return: результат вычисления или сообщение об ошибке
    """
    try:
        if mode == "area":
            return area(a, b)
        elif mode == "perimeter":
            return perimeter(a, b)
        else:
            raise ValueError("Неверный параметр mode")
    except ValueError as error:
        return f"Ошибка: {error}"

if __name__ == "__main__":
    try:
        side1 = float(input("Введите первую сторону прямоугольника: "))
        side2 = float(input("Введите вторую сторону прямоугольника: "))
        mode  = input("Что вычислить? (area / perimeter): ").strip().lower()

        result = rectangle(side1, side2, mode)
        print("Результат:", result)
    except ValueError:
        print("Ошибка: стороны должны быть числами!")