
number = int(input("Введите число: "))

formatted_number = f"{number:,}".replace(",", " ")

print(f"Результат: {formatted_number}")