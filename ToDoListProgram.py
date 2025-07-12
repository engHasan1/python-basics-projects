def menu():
    print('Welcome to the To-Do List Program!')
    print('1. Add a task')
    print('2. View tasks')
    print('3. Remove a task')
    print('4. Exit')
    pass

def addtask(taskList):
    task=input('Enter the task you want to add: ')
    if task:
        taskList.append(task)
        pass
    else:
        print('Task cannot be empty. Please enter a valid task.')
        addtask(taskList)

def viewtask(taskList):
    if not taskList:
        print('No tasks available.')
        pass
    else:
        print('Current tasks:')
        for i, task in enumerate(taskList, start=1):
            print(f'{i}. {task}')
        pass    
def removetask(taskList):
    if not taskList:
        print('No tasks available to remove.')
        pass
    else:
        viewtask(taskList)
        try:
            tasknum=int(input('Enter the task number you want to remove: '))
            if 1<= tasknum <= len(taskList):
                removed_task = taskList.pop(tasknum - 1)
                print(f'Task "{removed_task}" has been removed.')

        except ValueError:
            print('Invalid input. Please enter a valid task number.')


def main():
    taskList = []
    while True:
        menu()
        choice = input('Enter your choice (1-4): ')
        if choice == '1':
            addtask(taskList)
        elif choice == '2':
            viewtask(taskList)
        elif choice == '3':
            removetask(taskList)
        elif choice == '4':
            print('Thank you for using the To-Do List Program!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 4.')
        print()

if __name__ == '__main__':
    main()