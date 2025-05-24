todos = open("todos.txt").readlines()

print("MY TODO")
choice = None

def addTask():
        task = input("Enter task\n")
        todos.append(task)

def showTasks():
        print("My Task list\n")
        for index, task in enumerate(todos):
            print(f"Task{index+1} : {task}")  
            
def saveTasks():
        file = open("todos.txt","w")
        for task in todos:
            file.write(task + "\n")
        file.close()
        print("Saved")

while choice != "3" :
    choice = input("Menu\n1. Add task \n2.View Tasks\n3. Save and Exit..\n");

    if choice == "1" :
        addTask()
    elif choice == "2":
        showTasks()
    else :
        saveTasks()

