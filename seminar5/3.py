"""Создайте функцию генератор чисел Фибоначчи"""

def fibonacci_generator(f1=0, f2=1):
    while True:
        yield f1
        f1, f2 = f2, f1 + f2

fib = fibonacci_generator()
for i in range(10):
    print(next(fib))