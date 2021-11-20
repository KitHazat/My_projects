import random

digits = '0123456789'
lowercase_letter = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letter = lowercase_letter.upper()
symbols = '!#$%&*+-=?@^_'
expect = 'il1Lo0O'
chars = []


def generate_password(lenght, char):
    password = []
    for _ in range(lenght):
        password.append(random.choice(char))
    return password


print('Количество паролей для генерации:')
number_pass = int(input())
print('Длина одного пароля:')
len_pass = int(input())
print('Включать ли цифры? y/n')
digit_ans = input().lower()
if digit_ans == 'y':
    for i in digits:
        chars.append(i)
print('Включать ли прописные буквы? y/n')
lower_ans = input().lower()
if lower_ans == 'y':
    for i in lowercase_letter:
        chars.append(i)
print('Включать ли строчные буквы? y/n')
upper_ans = input().lower()
if upper_ans == 'y':
    for i in uppercase_letter:
        chars.append(i)
print('Включать ли символы? y/n')
symb_ans = input().lower()
if symb_ans == 'y':
    for i in symbols:
        chars.append(i)
print('Исключать ли неоднозначные символы - il1Lo0O? y/n')
expection = input().lower()
if expection == 'y':
    for i in chars[::-1]:
        if i in expect:
            chars.remove(i)


print('Ваши пароли:')
for _ in range(number_pass):
    print(*generate_password(len_pass, chars), sep='')
