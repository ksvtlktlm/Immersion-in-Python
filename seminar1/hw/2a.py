"""Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”.
Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч."""

#решение с использованием библиотеки sympy

from sympy import isprime

class WrongNumError(Exception):
    pass

while True:
    try:
        num = int(input('Введите число от 0 до 100_000: '))
        if num ==0 or num == 1:
            print('Это число не является ни простым, ни составным.')
            break
        if num < 0 or num > 100_000:
            raise WrongNumError('Введено неверное число!')
        print('Простое' if isprime(num) else 'Составное')
        break
    except WrongNumError as e:
        print(e)


