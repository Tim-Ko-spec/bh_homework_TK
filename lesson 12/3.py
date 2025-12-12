# в файле hero1 добавить следующий функционал
#         - добавить несколько классов других героев унаследовав их от Hero.
#         - Каждому герою добавить уникальное свойство-спец.очки (мана, ярость, и т.п. ) и 
#                 и свойство cо значением урона от спец.атаки.
#         - Создать метод атаки special_attack которая возможна только если количество 
#                 спец.очков более 0.
#         - Добавить метод attack который при атаке с вероятностью 25% будет использовать 
#                 спец.способность героя если у него остались спец.очки. 
#                 При спец атаке вычитать из очков 1. Если вероятность пришлась на
#                 остальные 75% - выполнить обычную атаку. Вывести сообщение в консоль 
#                 о типе и результате атаки.

# добавить класс Arena:
#         - атрибут warriors - все воины на арене (тип list)
#         - магический метод __init__, который принимает необязательный аргумент warriors.
#                 Если был передан список warriors, та заполняет им атрибут. Если нет, то заполняет
#                 пустым списком.
#         - метод add_warrior, который принимает аргумент warrior и добавляет его к warriors.
#                 Если данный воин уже есть в списке, то бросить исключение ValueError("Воин уже на арене").
#                 Если нет, то добавить воина к списку warriors и вывести сообщение на экран
#                 "{warrior.name} участвует в битве"
#         - метод choose_warrior, который не принимает аргументов и возвращает случайного
#                 воина из warriors
#         - метод battle, который не принимает аргументов и симулирует битву. Сперва 
#                 должна пройти проверка, что воинов на арене больше 1. Если меньше, то бросить
#                 исключение ValueError("Количество воинов на арене должно быть больше 1").
#                 Битва продолжается, пока на арене не останется только один воин. Сперва
#                 в случайном порядке выбираются атакующий и защищающийся. Атакующий ударяет
#                 защищающегося. Если у защищающегося осталось 0 health_points, то удалить его
#                 из списка воинов и вывести на экран сообщение "{name} пал в битве".
#                 Когда останется только один воин, то вывести сообщение "Победил воин: {name}".
#                 Вернуть данного воина из метода battle.
                
                
# Создать несколько воинов используя разные классы, добавить их на арену и запустить битву. 
# Выжить должен только один.


import random

class Hero:
    def __init__(self, name, health_points, damage):
        self.name = name
        self.health_points = health_points
        self.damage = damage

    def is_alive(self):
        return self.health_points > 0

    def take_damage(self, amount):
        self.health_points = max(0, self.health_points - amount)

    def attack(self, target):
        """Обычная атака"""
        target.take_damage(self.damage)
        print(f"{self.name} атакует {target.name} и наносит {self.damage} урона.")

    def __str__(self):
        return f"{self.name} (HP: {self.health_points})"

class Mage(Hero):
    """Маг — использует ману"""
    def __init__(self, name):
        super().__init__(name, health_points=90, damage=10)
        self.mana = 3
        self.special_damage = 30

    def special_attack(self, target):
        if self.mana > 0:
            self.mana -= 1
            target.take_damage(self.special_damage)
            print(f"{self.name} использует ОГНЕННЫЙ ШАР! Наносит {self.special_damage} урона.")
        else:
            print(f"{self.name} хотел использовать магию, но мана закончилась.")
            self.attack(target)

    def attack(self, target):
        if self.mana > 0 and random.random() < 0.25:
            self.special_attack(target)
        else:
            super().attack(target)


class Warrior(Hero):
    """Воин — использует энергию"""
    def __init__(self, name):
        super().__init__(name, health_points=120, damage=12)
        self.energy = 2
        self.special_damage = 35

    def special_attack(self, target):
        if self.energy > 0:
            self.energy -= 1
            target.take_damage(self.special_damage)
            print(f"{self.name} проводит МОЩНЫЙ УДАР! Наносит {self.special_damage} урона.")
        else:
            print(f"{self.name} устал и не может провести мощный удар.")
            self.attack(target)

    def attack(self, target):
        if self.energy > 0 and random.random() < 0.25:
            self.special_attack(target)
        else:
            super().attack(target)


class Berserk(Hero):
    """Берсерк — использует ярость"""
    def __init__(self, name):
        super().__init__(name, health_points=110, damage=15)
        self.rage = 4
        self.special_damage = 40

    def special_attack(self, target):
        if self.rage > 0:
            self.rage -= 1
            target.take_damage(self.special_damage)
            print(f"{self.name} впадает в ЯРОСТЬ! Наносит {self.special_damage} урона.")
        else:
            print(f"{self.name} не может войти в ярость — силы на нуле.")
            self.attack(target)

    def attack(self, target):
        if self.rage > 0 and random.random() < 0.25:
            self.special_attack(target)
        else:
            super().attack(target)

class Arena:
    def __init__(self, warriors=None):
        self.warriors = warriors if warriors else []

    def add_warrior(self, warrior):
        if warrior in self.warriors:
            raise ValueError("Воин уже на арене")
        self.warriors.append(warrior)
        print(f"{warrior.name} участвует в битве")

    def choose_warrior(self):
        return random.choice(self.warriors)

    def battle(self):
        if len(self.warriors) < 2:
            raise ValueError("Количество воинов на арене должно быть больше 1")

        print("\n БИТВА НАЧАЛАСЬ! ⚔️\n")

        while len(self.warriors) > 1:
            attacker, defender = random.sample(self.warriors, 2)

            attacker.attack(defender)

            if not defender.is_alive():
                print(f"💀 {defender.name} пал в битве!")
                self.warriors.remove(defender)

        winner = self.warriors[0]
        print(f"\n🏆 Победил воин: {winner.name}!")
        return winner

if __name__ == "__main__":
    arena = Arena()

    hero1 = Mage("Гендальф")
    hero2 = Warrior("Арагорн")
    hero3 = Berserk("Конан")

    arena.add_warrior(hero1)
    arena.add_warrior(hero2)
    arena.add_warrior(hero3)

    arena.battle()
