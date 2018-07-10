# -*- coding: utf-8 -*-

import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
all_fields = [l+n for l in letters for n in numbers]

class Computer:
    def __init__(self, all_fields):
        self.battelfield = []
        self.used_fields = []
        self.all_fields = all_fields
        self.ships_to_make = [[1, 4], [2, 3], [3, 2], [4, 1]]
    
    def create_battlefiled(self):
        pass
            
    def attack(self):
        pass
    
    def defence(self):
        pass
    
    def display(self):
        pass
    
    
class Player:
    def __init__(self, all_fields):
        self.battelfield = []
        self.used_fields = []
        self.all_fields = all_fields
        self.ships_to_make = [[1, 4], [2, 3], [3, 2], [4, 1]]
    
    def create_battlefiled(self):
        for i in range(len(self.ships_to_make)):
            for j in range(self.ships_to_make[i][0]):
                temp_fields = input('Enter %s fileds next to each other separated by a comma: ' % (self.ships_to_make[i][1]))
    
    def attack(self):
        pass
    
    def defence(self):
        pass
    
    def display(self):
        pass
    
    
class MainLoop:
    def __init__(self, computer, player):
        self.computer = computer
        self.player = player
        
    def battelfield(self):
        pass
        
    def game_loop(self):
        print('Enter fields names')
        self.player.create_battlefiled()
        
main_loop = MainLoop(Computer(all_fields), Player(all_fields))
main_loop.game_loop()