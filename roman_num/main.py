# -*- coding: utf-8 -*-

from encoder import encoder
from decoder import decoder


def calc(number):
    try:
        number = int(number)
        if number < 0:
            return 'We do not calculate negative numbers'
        return encoder(number)
    except:
        num = number
        for letter in ['I', 'V', 'X', 'L', 'C', 'D', 'M']:
            if letter in num:
                num = num.replace(letter, '')
        if len(num) != 0:
            return 'Wrong phrase'
        return str(decoder(number))
    
while True:
    number = input('Enter a Roman or Arabic number: ')
    print(calc(number))