
input_string = input("Введите цифры через пробел: ")

numbers = list(map(int, input_string.split()))

total_sum = sum(numbers)
max_number = max(numbers)
average = total_sum / len(numbers)

print(f"Общая сумма: {total_sum}")
print(f"Максимальная цифра: {max_number}")
print(f"Среднее арифметическое: {average:.2f}")