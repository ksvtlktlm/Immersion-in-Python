"""В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку."""

from sys import argv
from module_check_date import *

if __name__ == '__main__':
    param  = argv[1]
    print(check_date(param))