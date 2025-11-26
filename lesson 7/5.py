#Дан списк:
#['qwertyu','asdfggh','zxcvbnm','yuiop[]','hjklasd','mnbvnbv']
#Для каждого элемента в списке 
#    - вывести на экран сначала номер элемента 
#    - сам элемент 
#    - символ данного элемента, соответствующий номеру его позиции в списке. 
#Образец:
#1 - qwertyu - q
#2 - asdfggh - s
#3 - zxcvbnm - c
#и так далее...


def main():
    words = ['qwertyu', 'asdfggh', 'zxcvbnm', 'yuiop[]', 'hjklasd', 'mnbvnbv']

    for index, word in enumerate(words, start=1):
        # Берём символ по позиции (индекс элемента в списке)
        # index начинается с 1, поэтому используем word[index-1]
        char = word[index - 1]
        print(f"{index} - {word} - {char}")

if __name__ == "__main__":
    main()