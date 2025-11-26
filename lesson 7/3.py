#Запросить любое число. Заменить каждую цифру этого числа буквой, 
#у которой номер в алфавите равен этой цифре. 
#Алфавит считаем от 0. a-0, b-1, c-3 и т.д.
#Например: 13520 -> bdfca.

def digit_to_letter(digit):
    """Преобразует цифру в букву английского алфавита, считая a = 0."""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    return alphabet[digit]

def main():
    while True:
        number = input("Введите любое число: ").strip()
        if number.isdigit():
            break
        else:
            print("Ошибка: введите только цифры.")

    result = ''.join(digit_to_letter(int(d)) for d in number)
    print(f"Преобразованная строка: {result}")

if __name__ == "__main__":
    main()