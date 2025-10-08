# Simple To-Do List Application in Python
# It allows you to add tasks, view all tasks, remove tasks, and quit.

tasks = []  #it is a list to store the tasks

def display_menu(): 
    """Display the main menu options.""" 
    print("\n=== Mini To-Do List ===") 
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Quit")
    print("==========================")

def add_task(): 
    """Add a new task to the list."""
    task = input("Enter the task: ").strip()
    if task:
        tasks.append(task)
        print(f"Task '{task}' added successfully!")
    else:
        print("Task cannot be empty. Try again.")

def view_tasks():
    """Display all tasks with numbering."""
    if not tasks:
        print("No tasks in the list yet.")
    else:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    """Remove a task by its index."""
    view_tasks()
    if tasks:
        try:
            index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= index < len(tasks):
                removed_task = tasks.pop(index)
                print(f"Task '{removed_task}' removed successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """Main function to run the application."""
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye! Your tasks are saved in memory for this session.")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
