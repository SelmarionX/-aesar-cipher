char_rus = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
char_eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

cipher = input('Что будем делать шифровать (введите 1) или дешифровать (введите 2) ')
lang = input('Выберите язык алфавита: английский (введите 1) или русский (введите 2) ')
step = int(input('Шаг сдвига (укажите целое число) '))
text = input('Введите текст: ')

if cipher == '2': step *= -1
char = char_eng if lang == '1' else char_rus
for c in text:
    if c.upper() not in char: print(c, end='')
    else:
        temp = char[(char.find(c.upper()) + step) % len(char)]
        if c.islower(): temp = temp.lower()
        print(temp, end='')
