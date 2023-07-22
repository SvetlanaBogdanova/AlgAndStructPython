# 1. Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша (hash(), sha1() или любой другой из модуля hashlib задача считается
# не решённой.
from hashlib import sha1


def find_num_of_substrings(s: str) -> int:
    hashes = set()
    for sub_len in range(1, len(s)):
        for i in range(len(s) - sub_len + 1):
            hashes.add(sha1(s[i:i + sub_len].encode('utf-8')).hexdigest())
    return len(hashes)


s = input("Введите строку: ")
print(f'Количество различных подстрок: {find_num_of_substrings(s)}')
