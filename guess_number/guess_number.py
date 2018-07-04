# -*- coding: utf-8 -*-
import random


def random_num():
    return random.randint(1, 100)


def checking_num(num, players_num, tries_num):
    if players_num > 100 or players_num < 1:
        print('Wrong number!')
    elif num == players_num:
        print('Win')
        print('Number of tries: %s' % tries_num)
        main()
    elif num > players_num:
        print('Give a larger number')
    elif num < players_num:
        print('Give a smaller number')


def main():
    tries_num = 0
    num = random_num()
    print('Guess the number from 1 to 100')
    while 1:
        players_num = input('')
        try:
            tries_num += 1
            players_num = int(players_num)
            checking_num(num, players_num, tries_num)
            print('Try again!')  
        except ValueError:
            print('This is not a number!')
            
main()