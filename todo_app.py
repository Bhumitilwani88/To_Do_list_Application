# To-Do list Application
# Author : Bhumi Tilwani 
# Language : python 3 

import json
import os 

#Task load from file 
def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            return json.load(file)
    else:
        return []


# save tasks to file 
def save_task(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)


# Add a task 
def add_task(tasks):
    title = input("Enter task title: ")
    task = {
        "title" : title,
        "completed": False
    }
    tasks.append(task)
    save_task(tasks) 
    print("Task added! ")

# List all tasks
def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "Done" if task["completed"] else "Not done"
        print(f"{i}. {task['title']} [{status}]")


# Delete task 
def delete_task(tasks):
    list_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_task(tasks)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")
             
                    
#Mark task as done 
def mark_done(tasks):
    list_tasks(tasks)


    try:
        index= int(input ("Enter task number to mark as done: ")) -1 
        if 0 <= index < len(tasks):
            tasks[index] ["completed"] = True 
            save_task(tasks)
            print(f" Marked  as completed : {tasks[ index] ['title']}")
        else:
            print(" Invalid task number. ")
     
    except ValueError:
        print("please enter a valid number ")

# Main menu (CLI loop)

def main():
    tasks = load_tasks()
    while True:
        print("\n To-Do List menu")
        print("1, Add Task")
        print("2, View Task")
        print("3, Delete Task")
        print("4, Mark Task as Done")
        print("5, Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            delete_task(tasks)
        elif choice =="4":
            mark_done(tasks)
        elif choice == "5":
            print(" Exiting To-Do App . Bye!")
            break 
        else:
            print(" oops! Invalid choice. Try again ")

if __name__== "__main__":
                main()