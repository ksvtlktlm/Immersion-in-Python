"""Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions"""

from fractions import Fraction


def gcd(a, b):  # находим НОД
    while b:
        a, b = b, a % b
    return a


def sum_and_product_of_fractions(num1, denom1, num2, denom2):
    # Вычисляем сумму
    sum_numerator = num1 * denom2 + num2 * denom1
    sum_denominator = denom1 * denom2

    # Сокращаем дробь
    gcd_sum = gcd(sum_numerator, sum_denominator)
    sum_numerator //= gcd_sum
    sum_denominator //= gcd_sum

    # Вычисляем произведение
    product_numerator = num1 * num2
    product_denominator = denom1 * denom2

    # Сокращаем дробь
    gcd_product = gcd(product_numerator, product_denominator)
    product_numerator //= gcd_product
    product_denominator //= gcd_product

    return (sum_numerator, sum_denominator), (product_numerator, product_denominator)


fr1, fr2 = input(), input()
# проверка
print(
    Fraction(int(fr1.split('/')[0]), int(fr1.split('/')[1])) + Fraction(int(fr2.split('/')[0]), int(fr2.split('/')[1])))
print(
    Fraction(int(fr1.split('/')[0]), int(fr1.split('/')[1])) * Fraction(int(fr2.split('/')[0]), int(fr2.split('/')[1])))

sum_result, product_result = sum_and_product_of_fractions(
    int(fr1.split('/')[0]), int(fr1.split('/')[1]), int(fr2.split('/')[0]), int(fr2.split('/')[1]))

print(f"Сумма дробей: {sum_result[0]}/{sum_result[1]}")
print(f"Произведение дробей: {product_result[0]}/{product_result[1]}")
