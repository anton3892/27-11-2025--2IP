from datetime import date
from datetime import time
from datetime import timedelta
import datetime
import time
from datetime import datetime
from datetime import datetime, date

print("Таблица соотношения температур")
print("Цельсий\tФаренгейт")
print("-" * 20)

for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C\t{fahrenheit:.1f}°F")


def is_palindrome(text):
    # Удаляем пробелы и приводим к нижнему регистру
    text = text.replace(" ", "").lower()

    # Проверяем с помощью цикла
    length = len(text)
    for i in range(length // 2):
        if text[i] != text[length - i - 1]:
            return False
    return True


# Основная программа
user_input = input("Введите строку для проверки: ")

if is_palindrome(user_input):
    print(f"'{user_input}' - это палиндром!")
else:
    print(f"'{user_input}' - это не палиндром.")


def create_russian_binary_code():
    """Создает словарь для кодирования русских букв в двоичный код"""
    russian_alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    binary_codes = {}

    for i, letter in enumerate(russian_alphabet):
        # Преобразуем номер в двоичный код (минимум 6 бит)
        binary_code = format(i, '06b')  # 6 бит с ведущими нулями
        binary_codes[letter] = binary_code

    return binary_codes


def word_to_binary(word, code_dict):
    """Преобразует слово в двоичную кодовую комбинацию"""
    word = word.lower()
    binary_result = []

    for letter in word:
        if letter in code_dict:
            binary_result.append(code_dict[letter])
        else:
            binary_result.append('??????')  # Для символов не из алфавита

    return ' '.join(binary_result)


# Основная программа
binary_dict = create_russian_binary_code()

# Демонстрация кодирования
print("Таблица кодирования русских букв:")
for letter, code in list(binary_dict.items())[:10]:  # Покажем первые 10 букв
    print(f"{letter} -> {code}")

print("\n... и так далее")

# Кодирование слова
word = input("\nВведите слово на русском для кодирования: ")
binary_word = word_to_binary(word, binary_dict)

print(f"Слово '{word}' в двоичном коде:")
print(binary_word)


# Декодирование (дополнительная функция)
def binary_to_word(binary_string, code_dict):
    """Преобразует двоичную строку обратно в слово"""
    reverse_dict = {v: k for k, v in code_dict.items()}
    binary_codes = binary_string.split()
    word_result = []

    for code in binary_codes:
        if code in reverse_dict:
            word_result.append(reverse_dict[code])
        else:
            word_result.append('?')

    return ''.join(word_result)


# Пример полного цикла кодирования-декодирования
if binary_word != '??????':
    decoded_word = binary_to_word(binary_word, binary_dict)
    print(f"Декодированное слово: {decoded_word}")