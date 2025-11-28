# Написать функцию, которая возвращает любое число в виде денежной величины 
# с разделителями групп разрядов в качестве пробела и валютой в конце. 
# Денежная величина всегда должна содержать количество копеек в виде дух 
# знаков после точки, даже если исходное число целое. 
# *Нельзя использовать форматную строку.
# Например: 1234567 -> "1 234 567.00 руб."

# с помощью try перехватить возможные ошибки.


def money_format(value) -> str:
    """
    Преобразует число в денежный формат с пробелами и двумя знаками после точки.
    :param value: число (int или float)
    :return: строка вида '1 234 567.00 руб.'
    """
    try:
        # Преобразуем в float
        num = float(value)

        # Отделяем целую и дробную часть
        integer_part = int(num)
        fractional_part = round((num - integer_part) * 100)

        # Если дробная часть = 100 (например, 12.999 округлилось), корректируем
        if fractional_part == 100:
            integer_part += 1
            fractional_part = 0

        # Преобразуем целую часть в строку с разделителями пробелами
        digits = list(str(integer_part))
        result_int = ""
        count = 0
        for d in reversed(digits):
            if count and count % 3 == 0:
                result_int = " " + result_int
            result_int = d + result_int
            count += 1

        # Дробная часть всегда два знака
        frac_str = str(fractional_part).rjust(2, "0")

        return result_int + "." + frac_str + " руб."

    except ValueError:
        return "Ошибка: введено не число"
    except Exception as e:
        return f"Ошибка: {e}"

if __name__ == "__main__":
    user_input = input("Введите число: ")
    print(money_format(user_input))