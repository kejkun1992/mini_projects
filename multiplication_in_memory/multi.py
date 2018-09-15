# -*- coding: utf-8 -*-

import sys, random


def number_of_digits():
    # player chooses number of digits in each of multiplied numbers
    num = input('Test start. Choose number of digits in each of multiplied numbers(1-10): ')
    try:
        if int(num) > 10 and int(num) < 1:
            print('Wrong value. Bye')
            sys.exit()
        return int(num)
    except ValueError:
        print('Wrong value. Bye')
        sys.exit()


def number_of_numbers():
    # player chooses number of numbers to multiply
    num = input('Choose number of numbers to multiply(1-5): ')
    try:
        if int(num) > 5 and int(num) < 1:
            print('Wrong value. Bye')
            sys.exit()
        return int(num)
    except ValueError:
        print('Wrong value. Bye')
        sys.exit()
        
      
def list_to_str(nums: list) -> str:
    # changes list of numbers to operation in string
    nums = map(str, nums)
    return '*'.join(nums)
    
    
def random_operation(num_of_digits: int, num_of_nums: int) -> str:
    # creats random operation to solve
    nums = []
    for i in range(num_of_nums):
        if num_of_digits == 1:
            nums.append(random.randint(1, 9))
        elif num_of_digits == 2:
            nums.append(random.randint(10, 99))
        elif num_of_digits == 3:
            nums.append(random.randint(100, 999))
        elif num_of_digits == 4:
            nums.append(random.randint(1000, 9999))
        elif num_of_digits == 5:
            nums.append(random.randint(10000, 99999))
    return list_to_str(nums)
    

def main():
    num_of_digits = number_of_digits()
    num_of_nums = number_of_numbers()
    operation = random_operation(num_of_digits, num_of_nums)
    
if __name__ == '__main__':        
    main()