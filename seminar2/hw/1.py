"""Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата."""

num = int(input())
#проверка результата
print(hex(num))
res = ''
letters = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}
while num > 0:
    residue = num % 16
    if residue in letters:
        res += letters[residue]
    else:
        res += str(residue)
    num //= 16
print('0x' + res[::-1])
