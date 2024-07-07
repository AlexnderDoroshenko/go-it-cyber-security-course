"""
Завдання 1

Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.

Вимоги до завдання:

Функція приймає один параметр: date — рядок, що представляє дату у форматі 'РРРР-ММ-ДД' (наприклад, '2020-10-09').
Функція повертає ціле число, яке вказує на кількість днів від заданої дати до поточної. Якщо задана дата пізніша за поточну, результат має бути від'ємним.
У розрахунках необхідно враховувати лише дні, ігноруючи час (години, хвилини, секунди).
Для роботи з датами слід використовувати модуль datetime Python.


Рекомендації для виконання:

Імпортуйте модуль datetime.
Перетворіть рядок дати у форматі 'РРРР-ММ-ДД' у об'єкт datetime.
Отримайте поточну дату, використовуючи datetime.today().
Розрахуйте різницю між поточною датою та заданою датою.
Поверніть різницю у днях як ціле число.


Критерії оцінювання:

Коректність роботи функції: функція повинна точно обраховувати кількість днів між датами.
Обробка винятків: функція має впоратися з неправильним форматом вхідних даних.
Читабельність коду: код повинен бути чистим і добре документованим.


Приклад:

Якщо сьогодні 5 травня 2021 року, виклик get_days_from_today("2021-10-09") повинен повернути 157, оскільки 9 жовтня 2021 року є на 157 днів пізніше від 5 травня 2021 року.

"""
from datetime import datetime, timedelta

# Constants
DATE_FORMAT = "%Y-%m-%d"
ONE_YEAR_DAYS = 365

def get_days_from_today(date_str: str) -> int:
    """
    Calculate the number of days from the given date to today.

    Args:
    date_str (str): The date in 'YYYY-MM-DD' format.

    Returns:
    int: The number of days from the given date to today. Negative if the given date is in the future.
    """
    try:
        given_date = datetime.strptime(date_str, DATE_FORMAT).date()
        today = datetime.today().date()
        return (today - given_date).days
    except ValueError:
        raise ValueError(f"Incorrect date format, should be {DATE_FORMAT}")

# Test function with test cases
def test_get_days_from_today():
    today = datetime.today().date()
    future_date = (today + timedelta(days=ONE_YEAR_DAYS)).strftime(DATE_FORMAT)  # 1 year in the future
    past_date = (today - timedelta(days=ONE_YEAR_DAYS)).strftime(DATE_FORMAT)    # 1 year in the past

    test_cases = [
        (future_date, -ONE_YEAR_DAYS),  # Assuming the future date is exactly 365 days ahead
        (past_date, ONE_YEAR_DAYS),     # Assuming the past date was exactly 365 days ago
    ]

    for date_str, expected in test_cases:
        actual = get_days_from_today(date_str)
        assert actual == expected, f"Failed for {date_str}: expected {expected}, got {actual}"
        print(f"Test passed for {date_str}")

# Uncomment the line below to run the test function
# test_get_days_from_today()
