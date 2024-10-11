"""Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой
длины: имена str, ставка int, премия str с указанием процентов вида “10.25%”.
В результате получаем словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии"""


names = ['Иван', 'Мария', 'Олег', 'Геннадий', 'Наталья', 'Оксана']
salaries = [10000, 10000, 12000, 8500, 9700, 12800]
bonuses = ['10.00%', '12.55%', '7.00%', '8.50%', '14.00%', '9.00%']
res = {name: salary * float(bonus.strip('%')) * 0.01  for name, salary, bonus in zip(names, salaries, bonuses)}
print(res)