# Написать декоратор который позволит не останавливать программу 
# в случае если любая декорируемая функция выбрасывает ошибку, 
# а выводить имя функции в которой произошла ошибка и информацию об ошибке в. 
# Имя функции можно узнать использовав свойство __name__ ( print(func.__name__))

# * сделать настраиваемы параметр который определяет печать в консоль или в файл
# и если в файл передать название фала


def safe_run(output="console"):
    """
    Декоратор, который перехватывает ошибки в функции.
    output="console" — выводить ошибки в консоль
    output="file:filename.txt" — выводить ошибки в файл
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                message = f"Ошибка в функции '{func.__name__}': {e}"

                # вывод в консоль
                if output == "console":
                    print(message)

                # вывод в файл
                elif output.startswith("file:"):
                    filename = output.split(":", 1)[1]
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + "\n")

                # продолжаем выполнение программы
        return wrapper
    return decorator


# ✅ Примеры использования

@safe_run(output="console")
def div(a, b):
    return a / b


@safe_run(output="file:errors.log")
def bad_func():
    x = int("hello")  # ошибка


print("Результат деления:", div(10, 2))
print("Попытка деления на ноль:")
div(5, 0)

print("Вызов функции с ошибкой:")
bad_func()

print("Программа продолжает работать!")