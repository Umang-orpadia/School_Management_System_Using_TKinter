from tkinter import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~First Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root = Tk() #This is the 1st activated window
root.title("Page for student management system") #Defines the title of the window
root.geometry("800x600") # Defines the dimention of the window
root.configure(background="blue") #Decides the color of the page

user_label = Label(text="username")
user_label.grid(row=0 , column=0 ,padx=20 ,pady=20)

password_label = Label(text="password")
password_label.grid(row=1 , column=0 ,padx=20 ,pady=20)


root.mainloop() 