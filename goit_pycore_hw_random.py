"""
Завдання 2

Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, що випали випадковим чином і в певному діапазоні під час чергового тиражу. Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей. Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.



Вимоги до завдання:

Параметри функції:
min - мінімальне можливе число у наборі (не менше 1).
max - максимальне можливе число у наборі (не більше 1000).
quantity - кількість чисел, які потрібно вибрати (значення між min і max).
Функція генерує вказану кількість унікальних чисел у заданому діапазоні.
Функція повертає список випадково вибраних, відсортованих чисел. Числа в наборі не повинні повторюватися. Якщо параметри не відповідають заданим обмеженням, функція повертає пустий список.


Рекомендації для виконання:

Переконайтеся, що вхідні параметри відповідають заданим обмеженням.
Використовуйте модуль random для генерації випадкових чисел.
Використовуйте множину або інший механізм для забезпечення унікальності чисел.
Пам'ятайте, що функція get_numbers_ticket повертає відсортований список унікальних чисел.


Критерії оцінювання:

Валідність вхідних даних: функція повинна перевіряти коректність параметрів.
Унікальність результату: усі числа у видачі повинні бути унікальними.
Відповідність вимогам: результат має бути у вигляді відсортованого списку.
Читабельність коду: код має бути чистим і добре документованим.


Приклад: Припустимо, вам потрібно вибрати 6 унікальних чисел для лотерейного квитка, де числа повинні бути у діапазоні від 1 до 49. Ви можете використати вашу функцію так:

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

Цей код викликає функцію get_numbers_ticket з параметрами min=1, max=49 та quantity=6. В результаті ви отримаєте список з 6 випадковими, унікальними та відсортованими числами, наприклад, [4, 15, 23, 28, 37, 45]. Кожен раз при виклику функції ви отримуватимете різний набір чисел.
"""
import random
from typing import List

def get_numbers_ticket(min: int, max: int, quantity: int) -> List[int]:
    """
    Generates a list of unique, random, and sorted numbers within a specified range.

    Parameters:
    - min (int): The minimum possible number in the set (inclusive).
    - max (int): The maximum possible number in the set (inclusive).
    - quantity (int): The number of unique numbers to generate.

    Returns:
    - List[int]: A sorted list of unique random numbers if input parameters are valid; otherwise, an empty list.
    """
    # Validity of input data
    if min < 1 or max > 1000 or quantity < 1 or min > max or quantity > (max - min + 1):
        return []

    # Uniqueness of the result
    numbers = set()
    while len(numbers) < quantity:
        numbers.add(random.randint(min, max))

    # The result in the form of a sorted list
    return sorted(numbers)

# Test function with test cases
def test_get_numbers_ticket():
    # Test case 1: Check for correct number of unique numbers
    result = get_numbers_ticket(1, 10, 5)
    assert len(result) == 5 and len(set(result)) == len(result), "Test case 1 failed"
    
    # Test case 2: Check for sorted order
    assert result == sorted(result), "Test case 2 failed"
    
    # Test case 3: Check for empty list on invalid input
    assert get_numbers_ticket(1, 2, 5) == [], "Test case 3 failed"

# Uncomment the line below to run the test function
# test_get_numbers_ticket()
