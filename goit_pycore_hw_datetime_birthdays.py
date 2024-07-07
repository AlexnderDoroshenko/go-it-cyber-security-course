"""
Завдання 4

У межах вашої організації, ви відповідаєте за організацію привітань колег з днем народження. Щоб оптимізувати цей процес, вам потрібно створити функцію get_upcoming_birthdays, яка допоможе вам визначати, кого з колег потрібно привітати. Функція повинна повернути список всіх у кого день народження вперед на 7 днів включаючи поточний день.

У вашому розпорядженні є список users, кожен елемент якого містить інформацію про ім'я користувача та його день народження. Оскільки дні народження колег можуть припадати на вихідні, ваша функція також повинна враховувати це та переносити дату привітання на наступний робочий день, якщо необхідно.



Вимоги до завдання:

Параметр функції users - це список словників, де кожен словник містить ключі name (ім'я користувача, рядок) та birthday (день народження, рядок у форматі 'рік.місяць.дата').
Функція має визначати, чиї дні народження випадають вперед на 7 днів включаючи поточний день. Якщо день народження припадає на вихідний, дата привітання переноситься на наступний понеділок.
Функція повертає список словників, де кожен словник містить інформацію про користувача (ключ name) та дату привітання (ключ congratulation_date, дані якого у форматі рядка 'рік.місяць.дата').


Рекомендації для виконання:

Припускаємо, що ви отримали список users, де кожен словник містить name (ім'я користувача) та birthday (дата народження у форматі рядка 'рік.місяць.дата'). Ви повинні перетворити дати народження з рядків у об'єкти datetime. Конвертуйте дату народження із рядка у datetime об'єкт - datetime.strptime(user["birthday"], "%Y.%m.%d").date(). Оскільки потрібна лише дата (без часу), використовуйте .date() для отримання тільки дати.
Визначте поточну дату системи за допомогою datetime.today().date().
Пройдіться по списку users та аналізуйте дати народження кожного користувача (for user in users:).
Перевірте, чи вже минув день народження в цьому році (if birthday_this_year < today). Якщо так, розгляньте дату на наступний рік.
Визначте різницю між днем народження та поточним днем для визначення днів народження на наступний тиждень.
Перевірте, чи день народження припадає на вихідний. Якщо так, перенесіть дату привітання на наступний понеділок.
Створіть структуру даних, яка зберігатиме ім'я користувача та відповідну дату привітання, якщо день народження відбувається протягом наступного тижня.
Виведіть зібрані дані у вигляді списку словників з іменами користувачів та датами привітань.


Критерії оцінювання:

Актуальність та коректність визначення днів народження на 7 днів вперед.
Правильність обробки випадків, коли дні народження припадають на вихідні.
Читабельність та структурованість коду.


Приклад:

Припустимо, у вас є список users:

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

Використання функції get_upcoming_birthdays:

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

Якщо сьогодні 2024.01.22 результатом може бути:

[
    {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
    {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
]

Цей список містить інформацію про те, кого і коли потрібно привітати з днем народження.
"""
from datetime import datetime, timedelta
from typing import List

# Constants
DATE_FORMAT = "%Y.%m.%d"
DAYS_IN_WEEK = 7
WEEKEND_DAYS = [5, 6]

def get_upcoming_birthdays(users: List[dict]) -> List[dict]:
    """
    Function returns users list with birthdays in the next 7 days.
    
    Args:
    users (List[dict]): List of users with birthdays in string format ('YYYY.MM.DD')
    
    Returns:
    List[dict]: List of users with upcoming birthday greetings.
    
    The function iterates through each user, parsing their birthday and calculating if their
    birthday occurs within the next 7 days from today. If a birthday falls on a weekend,
    the congratulation date is adjusted to the next Monday.
    """
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        try:
            # Parse the birthday string into a date object
            birthday = datetime.strptime(user["birthday"], DATE_FORMAT).date()
            # Adjust the year to the current year for comparison
            birthday_this_year = birthday.replace(year=today.year)
        except ValueError:
            # Handle incorrect date format by skipping the user
            print(f"Incorrect date format '{user["birthday"]}', should be '{DATE_FORMAT}'")
            continue

        # If the birthday has already passed this year, consider next year's birthday
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Calculate the number of days until the birthday
        delta_days = (birthday_this_year - today).days

        # Skip if the birthday is not within the next 7 days
        if not 0 <= delta_days <= 7:
            continue

        # Adjust the congratulation date if it falls on a weekend
        congratulation_date = adjust_for_weekend(birthday_this_year)

        # Add the user to the list with the adjusted congratulation date
        upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime(DATE_FORMAT)
        })

    return upcoming_birthdays

def adjust_for_weekend(date: datetime.date) -> datetime.date:
    """
    Adjusts the date to the next Monday if it falls on a weekend.
    
    Args:
    date (datetime.date): The date to adjust if necessary.
    
    Returns:
    datetime.date: The adjusted date.
    
    This function checks if the given date falls on a weekend (Saturday or Sunday) and
    adjusts it to the following Monday to ensure that birthday greetings are not sent
    over the weekend.
    """
    if date.weekday() in WEEKEND_DAYS:
        # Calculate the adjustment needed to move the date to the next Monday
        return date + timedelta(days=(DAYS_IN_WEEK - date.weekday()))
    return date

# Test function with test cases
def test_get_upcoming_birthdays():
    """
    Tests the get_upcoming_birthdays function with various scenarios to ensure accuracy.
    
    This test function creates a set of test users with birthdays on different dates relative
    to today and checks if the function correctly identifies those whose birthdays are within
    the next 7 days. It also verifies that the congratulation dates do not fall on weekends.
    """
    today = datetime.today().date()
    test_data = [
        # Various test cases with birthdays on different days relative to today
        {"name": "Johny Duke", "birthday": "1985-01-23"},  # Wrong format
        {"name": "John Doe", "birthday": (today - timedelta(days=1)).strftime(DATE_FORMAT)},  # Yesterday
        {"name": "Jane Smith", "birthday": today.strftime(DATE_FORMAT)},  # Today
        {"name": "Alice Wonderland", "birthday": (today + timedelta(days=7)).strftime(DATE_FORMAT)},  # In 7 days
        {"name": "Bob Builder", "birthday": (today + timedelta(days=3)).strftime(DATE_FORMAT)},  # In 3 days
        {"name": "Charlie Brown", "birthday": (today + timedelta(days=8)).strftime(DATE_FORMAT)},  # In 8 days, just outside the range
        {"name": "Diana Prince", "birthday": (today + timedelta(days=10)).strftime(DATE_FORMAT)},  # In 10 days, well outside the range
        {"name": "George Jungle", "birthday": (today + timedelta((5 - today.weekday()) % 7)).strftime(DATE_FORMAT)},  # Next Saturday
        {"name": "Helen Troy", "birthday": (today + timedelta((6 - today.weekday()) % 7)).strftime(DATE_FORMAT)}  # Next Sunday
    ]
    results = get_upcoming_birthdays(test_data)
    print(results)

    # Expected names of users with upcoming birthdays within the next 7 days
    expected_names = ["Jane Smith", "Alice Wonderland", "Bob Builder", "George Jungle", "Helen Troy"]
    for expected_name in expected_names:
        # Check if each expected user is in the results
        found = any(user["name"] == expected_name for user in results)
        assert found, f"{expected_name} should be in the results."
        print(f"Test passed for user '{expected_name}'")

    for user in results:
        # Verify that the congratulation date does not fall on a weekend
        congratulation_date = datetime.strptime(user["congratulation_date"], DATE_FORMAT).date()
        assert congratulation_date.weekday() not in WEEKEND_DAYS, f"{user['name']}'s congratulation date falls on a weekend."
        print(f"Test falls on a weekend passed for user '{user['name']}'")
        
# Uncomment the line below to run the test function
# test_get_upcoming_birthdays()