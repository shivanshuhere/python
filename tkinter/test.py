from tkinter import *

window = Tk()

# window config
window.title("Todo App")
window.geometry("500x500")
window.config(bg="black")

todos = []
def addTask():
    task = label["text"]
    print(f"task : {task}")
    todos.append(task)

label = Label(window,
            text="Todo App", 
            font=("Arial", 20)
            )

entry = Entry(window, width=50)
button  = Button(window,
                text="Add Task",
                padx=10,
                pady=10,
                command=addTask               
                )
entry.pack()
button.pack()

window.mainloop()