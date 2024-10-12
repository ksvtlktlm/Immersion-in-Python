"""Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки
ферзей в задаче выше.
Проверяйте различный случайные варианты и выведите 4 успешных расстановки."""


import random
from module_chess import *

def generate_positions():
    positions = list(range(1, 9))
    for i in range(4):
        random.shuffle(positions)
        while not the_queen(positions):
            random.shuffle(positions)
        print(positions)