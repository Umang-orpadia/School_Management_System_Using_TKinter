from tkinter import *
import mysql.connector


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~First Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
root = Tk() #This is the 1st activated window
root.title("Page for student management system") #Defines the title of the window
root.geometry("800x600") # Defines the dimention of the window
root.configure(background="blue") #Decides the color of the page

user_label = Label(root,text="username")
user_label.grid(row=0 , column=0 ,padx=20 ,pady=20)

password_label = Label(root,text="password")
password_label.grid(row=1 , column=0 ,padx=20 ,pady=20)


username_entry = Entry(root)
username_entry.grid(row=0 , column=1 )

password_entry = Entry(root)
password_entry.grid(row=1 , column=1 )

conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "")
mycursor = conn.cursor()
mycursor.execute('use school_system;')

def Verify_details():
    # mycursor.execute(f"INSERT INTO student VALUES('{username_entry.get()}','{password_entry.get()}','21.01.2005','8591237049','orpadiau@gmail.com');")
    print(mycursor)
    conn.commit()

login_btn = Button(root ,text="Login", command=Verify_details)
login_btn.grid(row=2, column=1)



root1 = Tk()
root1.geometry('900x700')
root1.configure(background='purple')

student_name_label = Label(root1,text='Name')
student_name_label.grid(row = 0 , column = 0 , padx = 20 , pady = 20)

student_name_entry = Entry(root1)
student_name_entry.grid(row = 0 , column = 1 , padx = 20 , pady = 20)

student_roll_label = Label(root1,text='Roll no : ')
student_roll_label.grid(row = 1 , column = 0 , padx = 20 , pady = 20)

student_roll_entry = Entry(root1)
student_roll_entry.grid(row = 1 , column = 1 , padx = 20 , pady = 20)

student_dob_label = Label(root1,text='Date Of Birth')
student_dob_label.grid(row = 2 , column = 0 , padx = 20 , pady = 20)

student_dob_entry = Entry(root1)
student_dob_entry.grid(row = 2 , column = 1 , padx = 20 , pady = 20)

student_contact_label = Label(root1,text='Mobile No : ')
student_contact_label.grid(row = 3 , column = 0 , padx = 20 , pady = 20)

student_contact_entry = Entry(root1)
student_contact_entry.grid(row = 3 , column = 1 , padx = 20 , pady = 20)

student_email_label = Label(root1,text='E-mail : ')
student_email_label.grid(row = 4 , column = 0 , padx = 20 , pady = 20)

student_email_entry = Entry(root1)
student_email_entry.grid(row = 4 , column = 1 , padx = 20 , pady = 20)

def register():
    mycursor.execute(f"INSERT INTO student VALUES('{student_name_entry.get()}','{student_roll_entry.get()}','{student_dob_entry.get()}','{student_contact_entry.get()}','{student_email_entry.get()}');")
    print(mycursor)
    conn.commit()

register_btn = Button(root1,text = 'Register' , command = register)
register_btn.grid(row = 5 , column = 1 , padx = 20 , pady = 20)

root1.mainloop()


root.mainloop()

