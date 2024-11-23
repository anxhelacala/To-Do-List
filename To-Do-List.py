from tkinter import messagebox
from tkinter import *
import customtkinter 

root = customtkinter.CTk()
root.title("To-Do-List") #Title 
root.geometry("750x500")  #Geometry
 
root.resizable(False, False)  #Resizing Horizontally or Vertically
root.config(bg='#9F2B68')

def add_task():
  task=task_entry.get().capitalize()
  if task:
    tasks_list.insert(0,task)
    task_entry.delete(0,END)
    save_tasks()
  else:
    messagebox.showerror('Error','Enter a task')

def remove_task():
  selected=tasks_list.curselection()
  if selected:
    tasks_list.delete(selected[0])
    save_tasks()
  else:
    messagebox.showerror('Error','Choose a task to remove')

def save_tasks():
  with open("tasks.txt","w") as f:
    tasks=tasks_list.get(0,END)
    for task in tasks:
      f.write(task + "\n")

def load_tasks():
  try:
    with open("tasks.txt","r") as f:
      tasks=f.readlines()
      for task in tasks:
        tasks_list.insert(0,task.strip())
  except FileNotFoundError:
    pass



font1=('Arial',30,'bold')
font2=('Arial',18,'bold')
font3=('Arial',10,'bold')

title_label = customtkinter.CTkLabel(
    master=root,
    font=font1,
    text='To-Do-List',
    text_color='#F2D2BD',
    fg_color='#DE3163',      
    corner_radius=25,      
    bg_color='#9F2B68',     
    width=250,
    height=50
)
title_label.place(x=250, y=50)



add_button = customtkinter.CTkButton(
    command=add_task,
    master=root,
    font=font2,
    text='Add Task',
    text_color='#F2D2BD',
    fg_color='#E37383',      # Button background color
    hover_color='#C21E56',   # Hover color for the button
    corner_radius=25,        # Half of the height (50/2)
    bg_color='#9F2B68',
    width=200,
    height=50                
)
add_button.place(x=50, y=150)

remove_button = customtkinter.CTkButton(
    command=remove_task,
    master=root,
    font=font2,
    text='Remove Task',
    text_color='#F2D2BD',
    fg_color='#E37383',      # Button background color
    hover_color='#C21E56',   # Hover color for the button
    corner_radius=25,        # Half of the height (50/2)
    bg_color='#9F2B68',
    width=200,
    height=50                # Adjust height to match your needs
)
remove_button.place(x=500, y=150)

task_entry=customtkinter.CTkEntry(
     master=root,
    font=font2,
    text_color='#F2D2BD',
    fg_color='#E37383',    
    bg_color='#9F2B68',
    width=400,
    height=40 
)
task_entry.place(x=175,y=225)

tasks_list=Listbox(
    master=root,
    font=font3, 
    background='#E37383',
    selectbackground='#C21E56',
    width=100,
    height=10 

)
tasks_list.place(x=25,y=300)


              
load_tasks()



root.mainloop()
