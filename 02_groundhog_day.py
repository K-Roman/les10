# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

import random
import time

# class IamGodError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#     def __str__(self):
#         return self.message
#
# class DrunkError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#     def __str__(self):
#         return self.message
#
# class CarCrashError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#     def __str__(self):
#         return self.message
#
# class GluttonyError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#     def __str__(self):
#         return self.message
#
# class DepressionError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#     def __str__(self):
#         return self.message
#
# class SuicideError(Exception):
#     def __init__(self, message):
#         self.message = message
#
#     def __str__(self):
#         return self.message

class IamGodError(BaseException):
    def __init__(self):
        self.message = 'Я понял - я бог'
        self.time = time.ctime(time.time())

    def __str__(self):
        return self.message

class DrunkError(BaseException):
    def __init__(self):
        self.message = 'буду просто пить, завтра не будет похмелья'
        self.time = time.ctime(time.time())

    def __str__(self):
        return self.message


class CarCrashError(BaseException):
    def __init__(self):
        self.message = 'разобьюсь и ладно'
        self.time = time.ctime(time.time())

    def __str__(self):
        return self.message

class GluttonyError(BaseException):
    def __init__(self):
        self.message = 'обжорство не проблема'
        self.time = time.ctime(time.time())

    def __str__(self):
        return self.message

class DepressionError(BaseException):
    def __init__(self):
        self.message = 'я никогда не выберусь отсюда'
        self.time = time.ctime(time.time())

    def __str__(self):
        return self.message

class SuicideError(BaseException):
    def __init__(self):
        self.message = 'время пришло'
        self.time = time.ctime(time.time())

    def __str__(self):
        return self.message



def one_day():
    global ENLIGHTENMENT_CARMA_LEVEL
    global errors
    ENLIGHTENMENT_CARMA_LEVEL += random.randint(1,7)
    dice = random.randint(1,13)
    errors = [IamGodError(), DrunkError(), CarCrashError(),
              GluttonyError(), DepressionError(), SuicideError()]
    if dice == 1:
        with open('log12.txt', mode='a', encoding='utf8') as file:
            a = random.choice(errors)
            file.write(str(type(a)) + str(a.message) + ' ' + str(a.time)+ "\n")
            raise a

    return ENLIGHTENMENT_CARMA_LEVEL


ENLIGHTENMENT_CARMA_LEVEL = 0

while ENLIGHTENMENT_CARMA_LEVEL < 777:
    try:
        one_day()
    except (IamGodError, DrunkError, CarCrashError,
                      GluttonyError, DepressionError, SuicideError) as exc:
        print(f'Сегодня {exc}')
    print(ENLIGHTENMENT_CARMA_LEVEL)

# TODO здесь ваш код

# https://goo.gl/JnsDqu
