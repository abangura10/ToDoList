tasks = []

def addTask():
    task = input("Please enter task: ")
    tasks.append(task)
    print(f"'{task}' has been added.")

def viewTask():
    if not tasks:
        print("To-Do List is curently empty.")
    else:
        print('To-DO LIST:')
        print("--------------------------")
        for index, task in enumerate(tasks):
            print(f'{index + 1}. {task}')

def deleteTask():
    viewTask()
    try:
        taskToDelete = int(input(" Enter number of task to delete: "))
        if taskToDelete > 0 and taskToDelete <= len(tasks):
           tasks.pop(taskToDelete - 1)
           print(f'Task #{taskToDelete} has been removed from list.')
        else:
            print('Task is not listed.')
            
    except:
        print('Invalid input.')
        

if __name__ == "__main__":
    # Loop to run app
    print("Welcome to your To-Do List!")
    while True:
        # Ask user for task
        print("\n")
        print("What would you like to do?")
        print("--------------------------")
        print("1. Add task")
        print("2. Delete task")
        print("3. View task")
        print("4. Exit")
        print("--------------------------")
        
        option = input("Enter number of option: ")
        
        if option == '1':
            addTask()
        elif option == '2':
            deleteTask()
        elif option == '3':
            viewTask()
        elif option == '4':
            break
        else:
            print('Invalid option. Please enter number of listed option.')

print("Exiting To-Do List")
        
        
        
