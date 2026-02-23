def main():
    name = input("What is your name? ")
    while name.strip() == '' or name.isdigit():
        print("Name is invalid. Please enter a valid name.")
        name = input("What is your name? ")
    print(f"Hello, {name}! Welcome to your To-Do List.")
    to_do_list = []
    while True:
        print("\nTo-Do List:")
        print("1. Add a task") 
        print("2. Remove a task (by number)")
        print("3. View all tasks")
        print('4. Exit\n')  
        choice = input("Enter your choice from the menu! (1-4): ")
        print("Tasks added: ", len(to_do_list))
        # main menu is complete, now we need to add the functionality for each choice
        if choice == '1':
            print("Loading...")
            task = input(f"Give the task a name: ")
            if task.strip() == '':
                print("Task name cannot be empty. Please enter a valid task name.")
                return
            task_date = int(input("Give the task a date (in the format YYYYMMDD)(No slashes): "))
            task_time = int(input("Give the task a time (in the format HHMM)(No colons): "))
            print(f"The task' {task} ' been added to the to-do list.")
            to_do_list.append((task, task_date, task_time))
            #this is choice one and it adds a task to the to do list, it also asks for a date and adds that to the list as well, the date is in the format of YYYYMMDD and it is an integer, this is because it makes it easier to sort the tasks by date later on if we want to add that functionality in the future.
        elif choice == '3':
            print("Loading...\n")
            if len(to_do_list) == 0:
                print("The to-do list is empty.")
            else: 
                for i, task in enumerate(to_do_list, start=1):
                    print(f"{i}. {task}")
                    # this is choice three and it prints out all the tasks in the to do list, it also numbers them so that we can easily remove them later on if we want
        elif choice == '2':
            print("Loading...")
            if len(to_do_list) == 0:
                print("The to-do list is empty. No tasks to remove.")
            else: 
                for i, task in enumerate(to_do_list, start=1):
                    print(f"{i}. {task}")
                if len(to_do_list) > 0:
                    try:
                        task_number = int(input("Enter the number of the task to remove: "))
                        if task_number > 0 and task_number <= len(to_do_list):
                            removed_task = to_do_list.pop(task_number - 1)
                            print(f"The task '{removed_task}' has been removed from the to-do list.")
                        else:                            
                            print("Invalid task number. Please enter a valid task number.")
                    except ValueError:
                        print("Invalid input. Please enter a valid task number.")
# this is choice two and it allows the user to remove a task from the to do list by entering the number of the task they want to remove, it also checks if the input is valid and if the task number exists in the list before trying to remove it, if the input is invalid it will print an error message and ask the user to try again.
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
                      # this is the exit option and it allows the user to exit the program, it also checks if the input is valid and if the user enters an invalid choice it will print an error message and ask them to try again.
                
main()
# end of my first project, I hope you like it!