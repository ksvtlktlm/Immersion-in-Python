def is_leap(year: int) -> bool:
    return year % 400 == 0 or year % 100 != 0 and year % 4 == 0

def check_date(full_date: str) -> bool:
    day, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and day > 29:
        return False
    if month == 2 and day > 28 and not is_leap(year):
        return False
    return True

if __name__ == '__main__':
    print(check_date())
