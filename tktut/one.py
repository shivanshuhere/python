import tkinter as tk

todos = ["gym", "mouse", "key"]
task = None
update = True
def addTask():
    task = task_entry.get()
    print("add task " + task)
    todos.append(task)
    task_entry.delete(0, tk.END)
    update = True

def deleteTask():
    print("delete task")
    


window = tk.Tk()

# window config
window.config(bg="black")
window.geometry("400x400")
window.title("Todo App")

# buttons
add_button =  tk.Button(window,text="Add Task",
                        command=addTask)
delete_button =  tk.Button(window,text="Delete Task",
                        command=deleteTask)

# entery / input
task_entry = tk.Entry(window,textvariable=task)

app_title = tk.Label(window, text="My Todo")
app_title.pack()

task_entry.pack(side="left")
add_button.pack(side="left")

task_list_title = tk.Label(window, text="Task List")
task_list_title.pack(side="top")

while update:
    for todo in todos:
        task_list = tk.Label(window, text=todo)
        task_list.pack(side="top")
    udpate = False

window.mainloop()