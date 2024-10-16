"""Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника. Требуется сравнить длину каждого
отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше
суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли
треугольник разносторонним, равнобедренным или равносторонним."""

a, b, c = map(int, input('Введите длины сторон треугольника через пробел: ').split())
if all([a + b > c and a + c > b and b + c > a]):
    print('Треугольник существует.', end=' ')
    if a != b != c:
        print('Он разносторонний.')
    elif a == b == c:
        print('Он равносторонний.')
    else:
        print('Он равнобедренный.')
else:
    print('Треугольник не существует.')