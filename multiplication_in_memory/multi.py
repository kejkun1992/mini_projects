# -*- coding: utf-8 -*-

import sys, random, time


def numbers_range():
    # player chooses range of numbers to multiply
    num = input('Test start. Choose range of numbers to multiply(e.g.: 1-10): ')
    num = num.split('-')
    return list(map(int, num))

      
def list_to_str(nums: list) -> str:
    # changes list of numbers to operation in string
    nums = map(str, nums)
    return '*'.join(nums)
    
    
def random_operation(num1: int, num2: int) -> str:
    # creats random operation to solve
    nums = []
    for i in range(2):
        nums.append(random.randint(num1, num2))
    return list_to_str(nums)
    

def main():
    numbersRange = numbers_range()
    list_of_time = []
    for i in range(20):
        operation = random_operation(numbersRange[0], numbersRange[1])
        t1 = time.time()
        result = input(operation + ' = ')
        if int(result) == eval(operation):
            # saves user's time if result is good
            t2 = time.time()
            t = t2 - t1
            list_of_time.append(round(t, 2))
        else:
            print('Wrong answer')
    print(round(sum(list_of_time)/len(list_of_time), 2))
    with open('results\\results.txt', 'at') as results:
        print(str(numbersRange[0])+'-'+str(numbersRange[1])+'\t'+str(len(list_of_time))+'\t'+str(round(sum(list_of_time)/len(list_of_time),2)), file=results)
    
if __name__ == '__main__':        
    main()