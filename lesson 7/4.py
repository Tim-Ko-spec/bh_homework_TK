#Запросить высоту елочки - число от 3 до 20. 
#Напечатать на экране елочку где ее высота равна числу строк. 
#Пример елочки из 4 строк:
#   *
#  ***
# *****
#*******

#* - елочка со снегом


def read_height():
    """Запрашивает высоту ёлочки от 3 до 20 с проверкой."""
    while True:
        raw = input("Введите высоту ёлочки (от 3 до 20): ").strip()
        try:
            height = int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue

        if 3 <= height <= 20:
            return height
        else:
            print("Ошибка: допустимы значения от 3 до 20.")

def print_tree(height):
    """Печатает ёлочку высотой height строк."""
    for i in range(1, height + 1):
        stars = '*' * (2 * i - 1)
        print(stars.center(2 * height - 1))

def main():
    height = read_height()
    print("\nВот ваша ёлочка со снегом:\n")
    print_tree(height)

if __name__ == "__main__":
    main()