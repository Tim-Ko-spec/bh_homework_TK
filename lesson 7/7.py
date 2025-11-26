#Запросить любое число не менее 10. 
#Вывести на экран сумму квадратов каждой цифры составляющей это число. 
#Например: дано 236 => 2*2 + 3*3 + 6*6 = 49 


def main():
    while True:
        raw = input("Введите число не менее 10: ").strip()
        if raw.isdigit():
            number = int(raw)
            if number >= 10:
                break
            else:
                print("Ошибка: число должно быть не меньше 10.")
        else:
            print("Ошибка: вводите только цифры.")

    digits = [int(d) for d in str(number)]
    squares = [d * d for d in digits]
    total = sum(squares)

    # Формируем строку вида "2*2 + 3*3 + 6*6"
    expression = " + ".join(f"{d}*{d}" for d in digits)

    print(f"{number} => {expression} = {total}")


if __name__ == "__main__":
    main()