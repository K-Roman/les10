# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

# TODO здесь ваш код


def regist(line):
    name, email, age = line.split(' ')
    # print(name, email, age)
    if name is None or email is not None or age is not None:
        pass
    else:
        raise ValueError('отсутствует одно из полей')

    if name.isalpha():
        data = name
    else:
        raise NotNameError("поле имени содержит что-то кроме букв")

    if "@" in email and '.' in email:
        data += ' ' + email
    else:
        raise NotEmailError('что-то не так с почтой')
    if 10 < int(age) <= 99:
        data += ' ' + age
    else:
        raise ValueError('что-то не так с возрастом')
    return data




class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass
number = 0
with open('registrations.txt', 'r', encoding='utf8') as ff:
    for line in ff:
        number += 1
        try:
            da = regist(line)
            with open("registrations_good.log", 'a', encoding='utf8') as f1:
                f1.write(f'{da[:-1]} номер строки {number}' + '\n')
                print(da[:-1], str(number))
        except (ValueError, NotNameError, NotEmailError) as exc:
            with open("registrations_bad.txt", 'a', encoding='utf8') as f2:
                if "unpack" in exc.args[0]:
                    f2.write(f'ошибка отсутствует одно из полей в строке {line[:-1]} под номером {number} \n')
                    print(f'ошибка отсутствует одно из полей в строке {line[:-1]} под номером {number}')
                else:
                    f2.write(f'ошибка {exc} в строке {line[:-1]} под номером {number}' + '\n')
                    print(f'ошибка {exc} в строке {line[:-1]} под номером {number}')

