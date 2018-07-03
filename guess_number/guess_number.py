# -*- coding: utf-8 -*-
import random


def random_num():
    return random.randint(1, 100)


def checking_num(num, players_num, tries_num):
    if num == players_num:
        print('Win')
        main()
    elif num > players_num:
        print('Give a larger number')
    elif num > players_num:
        print('Give a smaller number')


def main():
    tries_num = 0
    num = random_num()
    print('')
    while 1:
        pass