# Добавить несколько черепах 
#     - или сразу 
#     * или в течении игры по одной через определенное количество кликов
#     - на каждой забиндить клик через одну и туже функцию cath


import turtle
import random

# список черепах
turtles = []

# функция обработки клика
def catch(x, y):
    print(f"Поймали черепаху в точке ({x}, {y})")

# функция для создания новой черепахи
def create_turtle():
    t = turtle.Turtle()
    t.shape("turtle")
    t.penup()
    # случайная позиция
    t.goto(random.randint(-200, 200), random.randint(-200, 200))
    # привязка клика к одной и той же функции
    t.onclick(catch)
    turtles.append(t)

# вариант 1: добавить несколько черепах сразу
for _ in range(3):
    create_turtle()

# вариант 2: добавлять черепах по одной через определённое количество кликов
click_counter = 0

def add_on_click(x, y):
    global click_counter
    click_counter += 1
    # каждые 3 клика создаём новую черепаху
    if click_counter % 3 == 0:
        create_turtle()

# назначаем обработчик кликов на экран
screen = turtle.Screen()
screen.onclick(add_on_click)

turtle.done()
