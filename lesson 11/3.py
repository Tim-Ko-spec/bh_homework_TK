# класс Counter, реализующий целочисленный счетчик.
# который может увеличивать или уменьшать свое значение (атрибут value)
# на единицу в заданном диапазоне.

# Предусмотреть инициализацию счетчика значениями по умолчанию и произвольными значениями.

# Определить атрибуты(свойства):
#     - value - текущее значение счетчика
#     ...

# Определить методы:
#     - инициализатор __init__, который устанавливает значение счетчика или 0 по умолчанию
#     - increase(num=1), увеличивает счетчик на заданную величину или 1 по умолчанию
#     - decrease(num=1), уменьшает счетчик на заданную величину или 1 по умолчанию
#     - reset, сбрасывает значение счетчика на стартовое    
#     - метод __iter__
#     - метод __next__
    
#     ** - stat, возвращает среднее количество изменений счетчика в секунду


import time


class Counter:
    def __init__(self, value=0, min_value=None, max_value=None):
        self.value = value
        self.start_value = value
        self.min_value = min_value
        self.max_value = max_value

        self._changes = 0          # количество изменений
        self._start_time = time.time()  # время начала работы

    def increase(self, num=1):
        new_value = self.value + num

        if self.max_value is not None:
            new_value = min(new_value, self.max_value)

        self.value = new_value
        self._changes += 1

    def decrease(self, num=1):
        new_value = self.value - num

        if self.min_value is not None:
            new_value = max(new_value, self.min_value)

        self.value = new_value
        self._changes += 1

    def reset(self):
        self.value = self.start_value
        self._changes += 1

    def __iter__(self):
        return self

    def __next__(self):
        self.increase()
        return self.value

    def stat(self):
        elapsed = time.time() - self._start_time
        if elapsed == 0:
            return 0
        return self._changes / elapsed

    def __str__(self):
        return f"Counter(value={self.value})"

c = Counter(value=5, min_value=0, max_value=10)

c.increase()
c.increase(3)
c.decrease()

print(c)

for _ in range(3):
    print(next(c))

print("Изменений в секунду:", c.stat())