# Елка


import os
import random
import time

# параметры
ROWS = 30
COLS = 60
SNOW_TYPES = ["*", ".", "+", "Ж"]
WIND_CHANGE_EVERY = 10  # каждые N кадров меняется ветер


# создаём пустое поле
def empty_field():
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]


# генерируем новую снежинку сверху
def generate_snowflakes(field, count=3):
    for _ in range(count):
        col = random.randint(0, COLS - 1)

        # не ставим снежинку рядом с другой
        if col > 0 and field[0][col - 1] != " ":
            continue
        if col < COLS - 1 and field[0][col + 1] != " ":
            continue

        field[0][col] = random.choice(SNOW_TYPES)


# двигаем снежинки вниз
def update_snow(field, wind):
    new_field = empty_field()

    for r in range(ROWS):
        for c in range(COLS):
            if field[r][c] in SNOW_TYPES:
                snow = field[r][c]

                # скорость падения зависит от размера
                speed = 2 if snow in ["*", "Ж"] else 1

                new_r = min(ROWS - 1, r + speed)
                new_c = min(COLS - 1, max(0, c + wind))

                # если место занято — оставляем на старом
                if new_field[new_r][new_c] != " ":
                    new_r = r
                    new_c = c

                new_field[new_r][new_c] = snow

    return new_field


# рисуем ёлку поверх поля
def draw_tree(field):
    center = COLS // 2
    height = 15

    for i in range(height):
        stars = "*" * (2 * i + 1)
        start = center - i
        for j, ch in enumerate(stars):
            field[i + 5][start + j] = ch


# вывод кадра
def print_field(field):
    print("\n".join("".join(row) for row in field))


# основной цикл
frame = 0
wind = 0

field = empty_field()

while True:
    os.system("cls")

    # иногда меняется ветер
    if frame % WIND_CHANGE_EVERY == 0:
        wind = random.choice([-1, 0, 1])

    # генерируем новые снежинки сверху
    generate_snowflakes(field, count=3)

    # двигаем старые снежинки
    field = update_snow(field, wind)

    # рисуем ёлку поверх снега
    draw_tree(field)

    # выводим кадр
    print_field(field)

    frame += 1
    time.sleep(0.1)