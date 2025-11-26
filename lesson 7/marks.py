#Запросить у учителя оценки ученика по одной до тех пор пока он не введет 0. 
#Выдать средний бал ученика.

def read_grade():
    """Читает одну оценку от пользователя и валидирует её."""
    while True:
        raw = input("Введите оценку (1–10) или 0 для завершения: ").strip()
        try:
            grade = int(raw)
        except ValueError:
            print("Ошибка: введите целое число.")
            continue

        if grade == 0:
            return 0
        if 1 <= grade <= 10:
            return grade
        else:
            print("Ошибка: допустимы оценки от 1 до 10, или 0 для завершения.")

def main():
    print("Ввод оценок ученика. Чтобы закончить, введите 0.")
    total = 0
    count = 0

    while True:
        grade = read_grade()
        if grade == 0:
            break
        total += grade
        count += 1

    if count == 0:
        print("Оценки не были введены. Средний балл вычислить невозможно.")
    else:
        average = total / count
        print(f"Средний балл ученика: {average:.2f} (на основе {count} оценок)")

if __name__ == "__main__":
    main()