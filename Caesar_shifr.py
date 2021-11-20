letter_list_russian = [chr(i).lower() for i in range(1040, 1072)]
letter_list_english = [chr(i).lower() for i in range(97, 123)]
encrypt_list = ''
decrypt_list = ''





def encryption(mod):
    encrypt_sentence_for_answer = ''
    global encrypt_list
    print('На каком языке будем шифровать? ru/en')
    encrypting_language = input()
    if encrypting_language == 'ru':
        encrypt_list = letter_list_russian
    elif encrypting_language == 'en':
        encrypt_list = letter_list_english
    print('Введите предложение, которое нужно зашифровать.')
    encrypt_sentence = input()
    for i in encrypt_sentence:
        if i.lower() in encrypt_list:
            encrypt_index = encrypt_list.index(i.lower())
            if (mod + encrypt_index) > len(encrypt_list):
                encrypt_index = encrypt_index - len(encrypt_list)
            if i.isupper():
                encrypt_sentence_for_answer += encrypt_list[encrypt_index + mod].upper()
            else:
                encrypt_sentence_for_answer += encrypt_list[encrypt_index + mod]
        else:
            encrypt_sentence_for_answer += i
    return encrypt_sentence_for_answer


def decryption(mod):
    decrypt_sentence_for_answer = ''
    global decrypt_list
    print('На каком языке будем дешифровать? ru/en')
    decrypting_language = input()
    if decrypting_language == 'ru':
        decrypt_list = letter_list_russian
    elif decrypting_language == 'en':
        decrypt_list = letter_list_english
    print('Введите предложение, которое нужно дешифровать.')
    decrypt_sentence = input()
    for i in decrypt_sentence:
        if i.lower() in decrypt_list:
            decrypt_index = decrypt_list.index(i.lower())
            if i.isupper():
                decrypt_sentence_for_answer += decrypt_list[decrypt_index - mod].upper()
            else:
                decrypt_sentence_for_answer += decrypt_list[decrypt_index - mod]
        else:
            decrypt_sentence_for_answer += i
    return decrypt_sentence_for_answer


print('Будем шифровать либо дешифровывать? enc/dec')
choise = input()
start_enc = 'y'
while start_enc == 'y':
    print('Введите шаг сдвига')
    step = int(input())
    if choise == 'enc':
        print(encryption(step))
    elif choise == 'dec':
        print(decryption(step))
    start_enc = input('Вы закончили? y/n').lower()