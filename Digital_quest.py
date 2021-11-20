from random import *
print('Для начала игры напишите "start"')
start_command = input().lower()


def is_valid(a):
    if a.isdigit():
        if 1 <= int(a) <= 100:
            return True
    else:
        return False


def game():
    count = 0
    while True:
        number = input()
        count += 1
        if is_valid(number):
            if num > int(number):
                print('Ваше число меньше загадоного, попробуйте еще разок')
                continue
            elif num < int(number):
                print('Ваше число больше загадоного, попробуйте еще разок')
                continue
            else:
                print('Вы угадали, поздравляем!', '\n' + f'Количество попыток : {count}')
                print('Для начала игры напишите "start"')
                break
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


while start_command == 'start':
    print('Добро пожаловать в числовую угадайку', '\n' + 'Введите число от 1 до 100')
    num = randint(1, 100)
    game()
    start_command = input().lower()
    if start_command != 'start':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')