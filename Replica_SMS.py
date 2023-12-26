from tkinter import *
import mysql.connector


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~First Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root = Tk() #This is the 1st activated window
root.title("Page for student management system") #Defines the title of the window
root.geometry("800x600") # Defines the dimention of the window
root.configure(background="blue") #Decides the color of the page

user_label = Label(text="username")
user_label.grid(row=0 , column=0 ,padx=20 ,pady=20)

password_label = Label(text="password")
password_label.grid(row=1 , column=0 ,padx=20 ,pady=20)


username_entry = Entry()
username_entry.grid(row=0 , column=1 )

password_entry = Entry()
password_entry.grid(row=1 , column=1 )

def Verify_details():
    conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "")
    mycursor = conn.cursor()
    mycursor.execute('')


login_btn = Button(root ,text="Login", command=Verify_details)
login_btn.grid(row=2, column=1)

root.mainloop() 