#1. Запросить у пользователей имя и отзыв о магазине. 
#Программа должна запрашивать данные пока не введено слово "stop". 
#Все данные сложить в словарь.
#    -распечатать количество отзывов
#    -распечатать отдельно имена пользователей
#    -распечатать отдельно отзывы


def main():
    reviews = {}  # словарь: имя -> отзыв

    print("Введите имя и отзыв о магазине. Для завершения введите 'stop'.")

    while True:
        name = input("Имя пользователя: ").strip()
        if name.lower() == "stop":
            break

        review = input("Отзыв: ").strip()
        if review.lower() == "stop":
            break

        reviews[name] = review

    # --- Вывод результатов ---
    print("\nИтоги:")
    print(f"Количество отзывов: {len(reviews)}")

    print("\nИмена пользователей:")
    for name in reviews.keys():
        print(name)

    print("\nОтзывы:")
    for review in reviews.values():
        print(review)


if __name__ == "__main__":
    main()