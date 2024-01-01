from tkinter import *
# import tkinter as tk
import mysql.connector


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~First Window~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def login_window_function():


    login_window = Tk() #This is the 1st activated window
    login_window.title("This is login page") #Defines the title of the window
    login_window.geometry("800x600") # Defines the dimention of the window
    login_window.configure(background="blue") #Decides the color of the page

    user_label = Label(login_window,text="username").grid(row=0 , column=0 ,padx=20 ,pady=20)
    password_label = Label(login_window,text="password").grid(row=1 , column=0 ,padx=20 ,pady=20)
    username_entry = Entry(login_window)
    username_entry.grid(row=0 , column=1 )
    password_entry = Entry(login_window)
    password_entry.grid(row=1 , column=1 )

    conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "")
    mycursor = conn.cursor()
    mycursor.execute('use school_system;')
    # ~~~~~~~~~~~Verify Detail~~~~~~~~~~~~~~~~~
    def after_login():
        if username_entry.get() == 'admin' and password_entry.get() == 'admin':
            def admin_window_function():
                admin_window = Tk()
                admin_window.title('You are Logedin as admin')
                admin_window.geometry('800x700')


                def register_user_window_function():

                    register_user_window = Tk()
                    register_user_window.geometry('1500x900')
                    register_user_window.title('This is registration Window')
                    register_user_window.configure(background='purple')


                    student_name_label = Label(register_user_window,text='Name').grid(row = 0 , column = 0 , padx = 20 , pady = 20)
                    student_name_entry = Entry(register_user_window)
                    student_name_entry.grid(row = 0 , column = 1 , padx = 20 , pady = 20)
                    student_roll_label = Label(register_user_window,text='Roll no : ').grid(row = 1 , column = 0 , padx = 20 , pady = 20)
                    student_roll_entry = Entry(register_user_window)
                    student_roll_entry.grid(row = 1 , column = 1 , padx = 20 , pady = 20)
                    student_dob_label = Label(register_user_window,text='Date Of Birth').grid(row = 2 , column = 0 , padx = 20 , pady = 20)
                    student_dob_entry = Entry(register_user_window)
                    student_dob_entry.grid(row = 2 , column = 1 , padx = 20 , pady = 20)
                    student_contact_label = Label(register_user_window,text='Mobile No : ').grid(row = 3 , column = 0 , padx = 20 , pady = 20)
                    student_contact_entry = Entry(register_user_window)
                    student_contact_entry.grid(row = 3 , column = 1 , padx = 20 , pady = 20)
                    student_email_label = Label(register_user_window,text='E-mail : ').grid(row = 4 , column = 0 , padx = 20 , pady = 20)
                    student_email_entry = Entry(register_user_window)
                    student_email_entry.grid(row = 4 , column = 1 , padx = 20 , pady = 20)

                    options = ['Student','Teacher']
                    your_role = StringVar(register_user_window)
                    your_role.set('Student')

                    user_role = OptionMenu(register_user_window , your_role , *options )
                    user_role.grid(row = 6 , column = 1 , padx = 20 , pady = 20)
                    user_role_label = Label(register_user_window , text='Role : ').grid(row=6 , column=0 , padx = 20 , pady = 20)
                    student_password_label = Label(register_user_window,text='Password : ').grid(row = 5 , column = 0 , padx = 20 , pady = 20)
                    student_password_entry = Entry(register_user_window)
                    student_password_entry.grid(row = 5 , column = 1 , padx = 20 , pady = 20)

                    def register():

                        sql1 = (f"INSERT INTO student(sn,srn,sdob,scn,sei,ur,upass) VALUES(%s,%s,%s,%s,%s,%s,%s);")
                        val1 = (student_name_entry.get(),student_roll_entry.get(),student_dob_entry.get(),student_contact_entry.get(),student_email_entry.get(),your_role.get(),student_password_entry.get())
                        mycursor.execute(sql1 , val1)
                        print(mycursor)
                        conn.commit()

                    register_btn = Button(register_user_window,text = 'Register' , command = register)
                    register_btn.grid(row = 7 , column = 1 , padx = 20 , pady = 20)
                    register_user_window.mainloop()
                def admin_college_register_function():
                    # root1 = Tk()
                    admin_college_register_window = Tk()
                    admin_college_register_window.geometry('800x600')
                    admin_college_register_window.title('Register new institute')

                    name_of_college_label = Label(admin_college_register_window , text='Name Of The College').grid(row=0 , column=0)

                    name_of_college_entry = Entry(admin_college_register_window )
                    name_of_college_entry.grid(row=0 , column=1)

                    email_of_college_label = Label(admin_college_register_window , text='E-mail Of The College').grid(row=1 , column=0)

                    email_of_college_entry = Entry(admin_college_register_window )
                    email_of_college_entry.grid(row=1 , column=1)

                    contact_of_college_label = Label(admin_college_register_window , text='Contact Of The College').grid(row=2 , column=0)

                    contact_of_college_entry = Entry(admin_college_register_window )
                    contact_of_college_entry.grid(row=2 , column=1)

                    branch_of_college_label = Label(admin_college_register_window , text='Branch Of The College').grid(row=3 , column=0)

                    branch_of_college_entry = Entry(admin_college_register_window )
                    branch_of_college_entry.grid(row=3 , column=1)

                    address_of_college_label = Label(admin_college_register_window , text='Address Of The College').grid(row=4 , column=0)

                    address_of_college_entry = Entry(admin_college_register_window )
                    address_of_college_entry.grid(row=4 , column=1)
                    
                    password_of_college_label = Label(admin_college_register_window , text='Set Password').grid(row=5 , column=0)

                    password_of_college_entry = Entry(admin_college_register_window )
                    password_of_college_entry.grid(row=5 , column=1)
                    def register_institute_function():
                        sql2 = (f'INSERT INTO college_details(cn,ceid,ccn,cbr,cadd,cpass) VALUES(%s,%s,%s,%s,%s,%s);')
                        val2 = (name_of_college_entry.get() , email_of_college_entry.get() , contact_of_college_entry.get() , branch_of_college_entry.get() , address_of_college_entry.get() , password_of_college_entry.get())

                        mycursor.execute(sql2,val2)
                        conn.commit()
                    register_institute_btn = Button(admin_college_register_window,text='Register Institute' , command=register_institute_function).grid(row=6 , column=1) 
                    
                    admin_college_register_window.mainloop()
                # admin_college_register_function()
                
                register_btn = Button(admin_window ,text="Add User", command=register_user_window_function).grid(row=3, column=1 , padx = 20 , pady = 20)
                
                institute_register_btn = Button(admin_window ,text="Add College", command=admin_college_register_function).grid(row=4, column=1 , padx = 20 , pady = 20)

                
                admin_window.mainloop()
            admin_window_function()
        else :

            after_login_window =Tk()
            after_login_window.geometry('500x300')
            after_login_window.config(bg='green')
            def update_window_function():

                edit_window = Tk()
                edit_window.geometry("800x600")
                edit_window.title("This is Update Page")
                edit_window.configure(background='pink')


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

                student_name1_label = Label(edit_window , text="Name: ").grid(row = 0 , column = 0 , padx = 20 , pady = 20)
                student_name1_entry = Entry(edit_window)
                student_name1_entry.grid(row = 0 , column = 1 , padx = 20 , pady = 20)
                student_roll1_label = Label(edit_window,text='Roll no : ').grid(row = 1 , column = 0 , padx = 20 , pady = 20)
                student_roll1_entry = Entry(edit_window)
                student_roll1_entry.grid(row = 1 , column = 1 , padx = 20 , pady = 20)
                student_dob1_label = Label(edit_window,text='Date Of Birth').grid(row = 2 , column = 0 , padx = 20 , pady = 20)
                student_dob1_entry = Entry(edit_window)
                student_dob1_entry.grid(row = 2 , column = 1 , padx = 20 , pady = 20)
                student_contact1_label = Label(edit_window,text='Mobile No : ').grid(row = 3 , column = 0 , padx = 20 , pady = 20)
                student_contact1_entry = Entry(edit_window)
                student_contact1_entry.grid(row = 3 , column = 1 , padx = 20 , pady = 20)
                student_email1_label = Label(edit_window,text='E-mail : ').grid(row = 4 , column = 0 , padx = 20 , pady = 20)
                student_email1_entry = Entry(edit_window)
                student_email1_entry.grid(row = 4 , column = 1 , padx = 20 , pady = 20)
                student_password1_label = Label(edit_window,text='Password : ').grid(row = 5 , column = 0 , padx = 20 , pady = 20)
                student_password1_entry = Entry(edit_window)
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



                Update_btn = Button(edit_window , text='Update' , command=Update_entry).grid(row = 6 , column = 1 , padx = 20 , pady = 20)
                delete_btn = Button(edit_window , text='Delete' , command=delete_entry).grid(row = 7 , column = 1 , padx = 20 , pady = 20)

                edit_window.mainloop()
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

                after_login_window.mainloop()
            read_btn = Button(after_login_window , text='Dasplay Data' , command=read_data).grid(row=0 , column=1)

            update_btn = Button(after_login_window , text='Edit' ,command=update_window_function).grid(row= 1 ,column=1) 


    login_btn = Button(login_window ,text="Login", command=after_login).grid(row=2, column=1 , padx = 20 , pady = 20)


    login_window.mainloop()

login_window_function()
    
