
template = "Юзер с именем <имя> заходил на сайт в 15:00"

name = input("Введите ваше имя: ")

result = template.replace("<имя>", name)

print(result)