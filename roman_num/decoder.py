# -*- coding: utf-8 -*-


def decoder(r: str) -> int:
        number = 0
        if 'CM' in r:
            number += 900
            r = r.replace('CM','')
        if 'CD' in r:
            number += 400
            r = r.replace('CD','')
        if 'XC' in r:
            number += 90
            r = r.replace('XC','')
        if 'XL' in r:
            number += 40
            r = r.replace('XL','')
        if 'IX' in r:
            number += 9
            r = r.replace('IX','')
        if 'IV' in r:
            number += 4
            r = r.replace('IV','')
        for x in r:
            if x == 'M':
                number += 1000
            if x == 'D':
                number += 500
            if x == 'C':
                number += 100
            if x == 'L':
                number += 50
            if x == 'X':
                number += 10
            if x == 'V':
                number += 5
            if x == 'I':
                number += 1
        return number