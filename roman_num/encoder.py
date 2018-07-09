# -*- coding: utf-8 -*-

import math


def encoder(n: int) -> str:
        roman = []
        if n >= 1000:
            roman.append('M'*int(math.floor(float(n)/float(1000))))
            n = n - 1000 * int(math.floor(float(n)/float(1000)))
        if n >= 500 and n < 1000:
            if n < 900:
                roman.append('D')
                n = n - 500
            elif n >= 900:
                roman.append('CM')
                n = n - 900
        if n >= 100 and n < 500:
            if n >= 400:
                roman.append('CD')
                n = n - 400
            elif n < 400:
                roman.append('C'*int(math.floor(float(n)/float(100))))
                n = n - 100 * int(math.floor(float(n)/float(100)))
        if n >= 50 and n < 100:
            if n < 90:
                roman.append('L')
                n = n - 50
            elif n >= 90:
                roman.append('XC')
                n = n - 90
        if n >= 10 and n < 50:
            if n >= 40:
                roman.append('XL')
                n = n - 40
            elif n < 40:
                roman.append('X'*int(math.floor(float(n)/float(10))))
                n = n - 10 * int(math.floor(float(n)/float(10)))
        if n >= 5 and n < 10:
            if n < 9:
                roman.append('V')
                n = n - 5
            elif n >= 9:
                roman.append('IX')
                n = n - 9
        if n >= 1 and n < 5:
            if n >= 4:
                roman.append('IV')
                n = n - 4
            elif n < 4:
                roman.append('I'*int(math.floor(float(n)/float(1))))
                n = n - 1 * int(math.floor(float(n)/float(1)))
        return ''.join(roman)