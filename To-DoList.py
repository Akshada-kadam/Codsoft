from tkinter import 
from tkinter import messagebox
	
def newTask():
    task = my_entry.get()
    priority = priority_var.get()
    if task != "":
        lb.insert(END, f"{task} ({priority})")
        my_entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please enter some task.")

def deleteTask():
    try:
        index = lb.curselection()[0]
        lb.delete(index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def updateTask():
    try:
        index = lb.curselection()[0]
        task = my_entry.get()
        priority = priority_var.get()
        if task != "":
            lb.delete(index)
            lb.insert(index, f"{task} ({priority})")
            my_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Please enter some task.")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def searchTask():
    search_term = search_entry.get().lower()
    lb.delete(0, END)
    for task in tasks:
        if search_term in task.lower():
            lb.insert(END, task)

ws = Tk()
ws.geometry('600x500+500+200')
ws.title('Enhanced To-Do List')
ws.config(bg="#ffe6e6")
ws.resizable(width=False, height=False)

tasks = []

