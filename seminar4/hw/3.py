"""3. Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список."""

import decimal


CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'
RICHNESS_SUM = decimal.Decimal(5000000)
RICHNESS_TAX = decimal.Decimal(10) / decimal.Decimal(100)
WITHDRAW_PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
ADD_PERCENT = decimal.Decimal(3) / decimal.Decimal(100)
MULTIPLICITY = 50
MIN_LEVEL = 30
MAX_LEVEL = 600
COUNT_OPER = 3

account = decimal.Decimal(0)
count = 0
while True:
    command = input(f'Пополнить - "{CMD_DEPOSIT}", снять - "{CMD_WITHDRAW}", выйти - "{CMD_EXIT}": ')
    if command == CMD_EXIT:
        print(f'Заберите карту. Текущий баланс: {account} у.е.')
        break
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержан налог на богатство {RICHNESS_TAX}% в размере {percent} у.е. Итого на карте осталось: {account}')
    if command in (CMD_DEPOSIT, CMD_WITHDRAW):
        amount = 1
        while amount % MULTIPLICITY != 0:
            amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
        if command == CMD_DEPOSIT:
            account += amount
            count += 1
            print(f'Пополнение баланса на {amount} у.е. Итого на карте: {account} у.е.')
        elif command == CMD_WITHDRAW:
            withdraw_tax = amount * WITHDRAW_PERCENT
            withdraw_tax = MIN_LEVEL if withdraw_tax < MIN_LEVEL else MAX_LEVEL if withdraw_tax > MAX_LEVEL else withdraw_tax
            if account >= withdraw_tax + amount:
                account -= (amount + withdraw_tax)
                count += 1
                print(f'Снятие с баланса на {amount} у.е. Итого на карте: {account} у.е.')
            else:
                print(
                    f'Недостаточно средств на балансе для выполнения операции снятия. Затребованная сумма: {amount}, комиссия {withdraw_tax}.На карте {account} у.е.')
    if count and count % COUNT_OPER == 0:
        bonus = account * ADD_PERCENT
        account += bonus
        print(f'Начислен бонус в размере: {bonus}. Баланс на карте: {account} у.е.')
