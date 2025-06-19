tasks = []



def add_task():
    input_task = input("Enter your task: ")
    tasks.append(input_task)
    print(f"{input_task} has been added")


def remove_task():
    input_task = input("Enter your task: ")
    tasks.remove(input_task)
    print(f"{input_task} has been removed")

def task_menu():
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit menu")

def view_task():
    if not tasks :
        print("To-do list is empty")
    else :
        print("Your tasks:")

while True :
    task_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        view_task()
    if choice == "2" :
        add_task()
    if choice == "3" :
        remove_task()
    else : 
        print("Invalid option. Please choose from 1-4")
    