from tkinter import *
# import tkinter as tk
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
    root3 = Tk()
    root3.geometry("800x600")
    root3.title("This is Update Page")
    root3.configure(background='pink')

    sql2 = ( f' SELECT * FROM student WHERE sei = %s AND upass = %s ')
    val2 = (username_entry.get(),password_entry.get())
    mycursor.execute(sql2 , val2)

    fetch_data = mycursor.fetchone()
    student_name = fetch_data[0]
    student_rollno = fetch_data[1]
    student_dob = fetch_data[2]
    student_contactno = fetch_data[3]
    student_emailid = fetch_data[4]
    student_password = fetch_data[5]

    student_name1_label = Label(root3 , text="Name: ")
    student_name1_label.grid(row = 0 , column = 0 , padx = 20 , pady = 20)

    student_name1_entry = Entry(root3)
    student_name1_entry.grid(row = 0 , column = 1 , padx = 20 , pady = 20)

    student_roll1_label = Label(root3,text='Roll no : ')
    student_roll1_label.grid(row = 1 , column = 0 , padx = 20 , pady = 20)

    student_roll1_entry = Entry(root3)
    student_roll1_entry.grid(row = 1 , column = 1 , padx = 20 , pady = 20)

    student_dob1_label = Label(root3,text='Date Of Birth')
    student_dob1_label.grid(row = 2 , column = 0 , padx = 20 , pady = 20)

    student_dob1_entry = Entry(root3)
    student_dob1_entry.grid(row = 2 , column = 1 , padx = 20 , pady = 20)

    student_contact1_label = Label(root3,text='Mobile No : ')
    student_contact1_label.grid(row = 3 , column = 0 , padx = 20 , pady = 20)

    student_contact1_entry = Entry(root3)
    student_contact1_entry.grid(row = 3 , column = 1 , padx = 20 , pady = 20)

    student_email1_label = Label(root3,text='E-mail : ')
    student_email1_label.grid(row = 4 , column = 0 , padx = 20 , pady = 20)

    student_email1_entry = Entry(root3)
    student_email1_entry.grid(row = 4 , column = 1 , padx = 20 , pady = 20)

    student_password1_label = Label(root3,text='Password : ')
    student_password1_label.grid(row = 5 , column = 0 , padx = 20 , pady = 20)

    student_password1_entry = Entry(root3)
    student_password1_entry.grid(row = 5 , column = 1 , padx = 20 , pady = 20)

    student_name1_entry.insert(0,student_name)
    student_roll1_entry.insert(0,student_rollno)
    student_dob1_entry.insert(0,student_dob)
    student_contact1_entry.insert(0,student_contactno)
    student_email1_entry.insert(0,student_emailid)
    student_password1_entry.insert(0,student_password)

    def Update_entry():
        mycursor.execute( f"UPDATE student SET sn = '{student_name1_entry.get()}' ,srn = '{student_roll1_entry.get()}' ,sdob = '{student_dob1_entry.get()}' ,scn = '{student_contact1_entry.get()}' ,sei = '{student_email1_entry.get()}' ,upass = '{student_password1_entry.get()}' WHERE srn = '{student_rollno}';" )
        print(mycursor)
        conn.commit()

    def delete_entry():
        mycursor.execute(f"DELETE FROM student WHERE sei = '{student_email1_entry.get()}'")
        conn.commit()

    def read_data():
        root4 = Tk()
        mycursor.execute('SELECT * FROM student ')

        fetch_data = mycursor.fetchall()
        m=0
        for i in fetch_data:
            for j in range(len(i)):
                e = Label(root4 , text=i[j])
                e.grid(row=m,column=j)
                print(i[j] , end=' ')
            m=m+1
            print('\n')
        root4.mainloop()


    Update_btn = Button(root3 , text='Update' , command=Update_entry)
    Update_btn.grid(row = 6 , column = 1 , padx = 20 , pady = 20)

    delete_btn = Button(root3 , text='Delete' , command=delete_entry)
    delete_btn.grid(row = 7 , column = 1 , padx = 20 , pady = 20)

    read_btn = Button(root3 , text='Dasplay Data' , command=read_data)
    read_btn.grid(row=8 , column=1)
    root3.mainloop()

login_btn = Button(root ,text="Login", command=Verify_details)
login_btn.grid(row=2, column=1)


def register_window():

    root1 = Tk()
    root1.geometry('900x700')
    root1.title('This is registration Window')
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

    student_password_label = Label(root1,text='Password : ')
    student_password_label.grid(row = 5 , column = 0 , padx = 20 , pady = 20)

    student_password_entry = Entry(root1)
    student_password_entry.grid(row = 5 , column = 1 , padx = 20 , pady = 20)

    def register():

        sql1 = (f"INSERT INTO student(sn,srn,sdob,scn,sei,upass) VALUES(%s,%s,%s,%s,%s,%s);")
        val1 = (student_name_entry.get(),student_roll_entry.get(),student_dob_entry.get(),student_contact_entry.get(),student_email_entry.get(),student_password_entry.get())
        mycursor.execute(sql1 , val1)

        print(mycursor)
        conn.commit()

    register_btn = Button(root1,text = 'Register' , command = register)
    register_btn.grid(row = 6 , column = 1 , padx = 20 , pady = 20)
    root1.mainloop()

register_btn = Button(root ,text="Add Student", command=register_window)
register_btn.grid(row=3, column=1 , padx = 20 , pady = 20)

root.mainloop()
