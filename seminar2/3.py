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


def apply_richness_tax(account):
    if account > RICHNESS_SUM:
        percent = account * RICHNESS_TAX
        account -= percent
        print(f'Удержан налог на богатство {RICHNESS_TAX}% в размере {percent} у.е. Итого на карте осталось: {account}')
    return account


def deposit(account, amount, operations, operations_list):
    account += amount
    operations += 1
    operations_list.append(f'Пополнение: {amount} у.е.')
    print(f'Пополнение баланса на {amount} у.е. Итого на карте: {account} у.е.')
    return account, operations


def withdraw(account, amount, operations, operations_list):
    withdraw_tax = amount * WITHDRAW_PERCENT
    withdraw_tax = max(MIN_LEVEL, min(MAX_LEVEL, withdraw_tax))
    if account >= withdraw_tax + amount:
        account -= (amount + withdraw_tax)
        operations += 1
        operations_list.append(f'Снятие: {amount} у.е., Комиссия: {withdraw_tax} у.е.')
        print(f'Снятие с баланса на {amount} у.е. Итого на карте: {account} у.е.')
    else:
        print(
            f'Недостаточно средств на балансе для выполнения операции снятия. Затребованная сумма: {amount}, комиссия {withdraw_tax}.На карте {account} у.е.')
    return account, operations


def add_bonus(account, operations):
    if operations > 0 and operations % COUNT_OPER == 0:
        bonus = account * ADD_PERCENT
        account += bonus
        print(f'Начислен бонус в размере: {bonus}. Баланс на карте: {account} у.е.')
    return account


def get_valid_amount():
    amount = 1
    while amount % MULTIPLICITY != 0:
        amount = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    return amount


def main():
    account = decimal.Decimal(0)
    operations = 0
    operations_list = []

    while True:
        command = input(f'Пополнить - "{CMD_DEPOSIT}", снять - "{CMD_WITHDRAW}", выйти - "{CMD_EXIT}": ')
        if command == CMD_EXIT:
            print(f'Заберите карту. Текущий баланс: {account} у.е.')
            print('История операций:', operations_list)
            break

        account = apply_richness_tax(account)

        if command in (CMD_DEPOSIT, CMD_WITHDRAW):
            amount = get_valid_amount()
            if command == CMD_DEPOSIT:
                account, operations = deposit(account, amount, operations, operations_list)
            elif command == CMD_WITHDRAW:
                account, operations = withdraw(account, amount, operations, operations_list)

        account = add_bonus(account, operations)


if __name__ == "__main__":
    main()