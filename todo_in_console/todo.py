# -*- coding: utf-8 -*-


def display_list():
    print()
    print('__________________________________________________________________')
    with open('todo_tasks.txt') as tasks_list:
        print(tasks_list.read())
        
        
def adding(new_task):
    with open('todo_tasks.txt') as tasks_list:
        tasks = [line.split() for line in tasks_list]
        id_num = tasks[-1][0]
        try:
            id_num = str(int(id_num) + 1)
        except:
            id_num = '1'
    with open('todo_tasks.txt', 'a') as tasks_list:
        print(id_num+'\t'+new_task, file=tasks_list)


def deleting(id_num):
    with open('todo_tasks.txt') as tasks_list:
        tasks = [line.split('\t') for line in tasks_list]
    num_list = [item[0] for item in tasks]
    if id_num in num_list and id_num != 'ID':
        new_list = [line for line in tasks if line[0] != id_num]
        if len(new_list) > 1:
            n = 1
            for line in new_list[1::]:
                line[0] = str(n)
                n += 1
        with open('todo_tasks.txt', 'w') as tasks_list:
             for line in new_list:
                 print('\t'.join(line), file=tasks_list, end='')
    else:
        print('There is no task for such an ID.')


def replacing(id_num, new_task):
    with open('todo_tasks.txt') as tasks_list:
        tasks = [line.split('\t') for line in tasks_list]
    num_list = [item[0] for item in tasks]
    if id_num in num_list and id_num != 'ID':
        new_tasks = []
        for line in tasks:
            if id_num == line[0]:
                line = [line[0]] + [new_task + '\n']
                new_tasks.append(line)
            else:
                new_tasks.append(line)
        with open('todo_tasks.txt', 'w') as tasks_list:
            for line in new_tasks:
                 print('\t'.join(line), file=tasks_list, end='')
    else:
        print('There is no task for such an ID.')
        
def main():
    while True:
        display_list()
        what_todo = input('Add(A), replace(R) or delete(D) a task?\n')
        if what_todo == 'A':
            new_task = input('Enter the task:\n')
            adding(new_task)
        elif what_todo == 'D':
            id_num = input('Enter the ID of the task to be deleted:\n')
            deleting(id_num)
        elif what_todo == 'R':
            id_num = input('Enter the ID of the task to be replaced:\n')
            new_task = input('Enter the task:\n')
            replacing(id_num, new_task)
        else:
            main()

print('To-do list\n\n')
main()