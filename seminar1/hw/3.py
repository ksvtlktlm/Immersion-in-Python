"""Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
Программа должна подсказывать “больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)"""

from random import randint

class WrongNumError(Exception):
    pass

hidden_num = randint(0, 1000)
tries = 0
while tries < 10:
    try:
        user_num = int(input('Введите число от 0 до 1000: '))
        if user_num < 0 or user_num > 1000:
            raise WrongNumError('Введено неверное число!')
        if user_num == hidden_num:
            print(f'Вы угадали за {tries + 1} попыток!')
            break
        elif user_num > hidden_num:
            tries += 1
            print('Меньше!')
        else:
            tries += 1
            print('Больше!')
    except WrongNumError as e:
        print(e)
if tries >= 10:
    print(f'Попытки исчерпаны. Загаданное число: {hidden_num}.')
