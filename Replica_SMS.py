from tkinter import *
# import tkinter as tk
import mysql.connector


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~  Connection Part  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
conn = mysql.connector.connect(host = "localhost" , user = "root" , password = "")
mycursor = conn.cursor()
mycursor.execute('use school_system;')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Widgits Function  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def labelthisas(mastername , displaytext , r,c):
    labelthisas = Label(mastername , text=displaytext)
    labelthisas.grid(row=r , column=c ,padx=20 , pady=20)

def entryfunction(mastername , r, c):
    entry = Entry(mastername)
    entry.grid(row=r , column=c)
    return entry

def btn(mastername , btntext,givecommand,r,c):
    Button(mastername , text=btntext , command=givecommand ).grid(row=r , column=c , padx=20 , pady=20)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Reading data from student table  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Inserting data into student table  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def insertfunction(student_name_entry,student_roll_entry,student_dob_entry,student_contact_entry,student_email_entry,your_role,student_password_entry):
    sql = (f"INSERT INTO student(sn,srn,sdob,scn,sei,ur,upass) VALUES(%s,%s,%s,%s,%s,%s,%s);")
    val = (student_name_entry,student_roll_entry,student_dob_entry,student_contact_entry,student_email_entry,your_role,student_password_entry)
    mycursor.execute(sql , val)
    print(mycursor)
    conn.commit()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Updaing records from student table  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def update_function(name ,rollno , dob ,cn , ei ,upass , ur ,basedon ):
    mycursor.execute(f"UPDATE student SET sn='{name}' ,srn ='{rollno}' , sdob = '{dob}' , scn = '{cn}' , sei = '{ei}' , upass = '{upass}' , ur = '{ur}' WHERE srn = '{basedon}';")
    print(mycursor)
    conn.commit()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Registering Student and techer into student table  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def register_user_window_function():

    register_user_window = Tk()
    register_user_window.geometry('1500x900')
    register_user_window.title('This is registration Window')
    register_user_window.configure(background='purple')


    labelthisas(register_user_window,'Name : ',0,0)
    student_name_entry = entryfunction(register_user_window,0,1)
    labelthisas(register_user_window,'Roll no : ',1,0)
    student_roll_entry = entryfunction(register_user_window,1,1)
    labelthisas(register_user_window,'Date of Birth : ',2,0)
    student_dob_entry = entryfunction(register_user_window,2,1)
    labelthisas(register_user_window,'Contact no : ',3,0)
    student_contact_entry = entryfunction(register_user_window,3,1)
    labelthisas(register_user_window,'E-mail : ',4,0)
    student_email_entry = entryfunction(register_user_window,4,1)

    options = ['Student','Teacher']
    your_role = StringVar(register_user_window)
    your_role.set('Student')

    user_role = OptionMenu(register_user_window , your_role , *options )
    user_role.grid(row = 6 , column = 1 , padx = 20 , pady = 20)
    labelthisas(register_user_window ,'Role : ',6,0)
    labelthisas(register_user_window,'Password',5,0)
    student_password_entry = entryfunction(register_user_window,5,1)

    def insertit():
        insertfunction(student_name_entry.get(),student_roll_entry.get(),student_dob_entry.get(),student_contact_entry.get(),student_email_entry.get(),your_role.get(),student_password_entry.get())

    btn(register_user_window,'Register',insertit,7,1)
    register_user_window.mainloop()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Admin View Window  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def admin_window_function():
    admin_window = Tk()
    admin_window.title('You are Logedin as admin')
    admin_window.geometry('800x700')

    btn(admin_window,'Add User',register_user_window_function,3,1)
    
    # btn(admin_window,'Add College',admin_college_register_function,4,1)
    # btn(admin_window,'Display Data',read_data,5,1)

    
    admin_window.mainloop()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~  Updating teacher and student  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def update_window_function():

    edit_window = Tk()
    edit_window.geometry("800x600")
    edit_window.title("This is Update Page")
    edit_window.configure(background='pink')


    sql2 = ( f' SELECT * FROM student WHERE sei = %s AND upass = %s ')
    val2 = (enteredusername,enteredpassword)
    mycursor.execute(sql2 , val2)

    fetch_data = mycursor.fetchone()
    print(fetch_data)
    student_name = fetch_data[0]
    student_rollno = fetch_data[1]
    student_dob = fetch_data[2]
    student_contactno = fetch_data[3]
    student_emailid = fetch_data[4]
    student_password = fetch_data[5]
    user_role = fetch_data[6]

    labelthisas(edit_window,'Name' ,0,0)
    student_name1_entry = entryfunction(edit_window,0,1)
    labelthisas(edit_window,'Roll No, : ' ,1,0)
    student_roll1_entry = entryfunction(edit_window,1,1)
    labelthisas(edit_window,'Date of Birth : ' ,2,0)
    student_dob1_entry = entryfunction(edit_window,2,1)
    labelthisas(edit_window,'Contact No. : ' ,3,0)
    student_contact1_entry =entryfunction(edit_window,3,1)
    labelthisas(edit_window,'E-mail : ' ,4,0)
    student_email1_entry = entryfunction(edit_window,4,1)
    labelthisas(edit_window,'Password : ' ,5,0)
    student_password1_entry = entryfunction(edit_window,5,1)
    labelthisas(edit_window,'Role : ' ,6,0)
    # student_role_entry = entryfunction(edit_window,6,1)

    student_name1_entry.insert(0,student_name)
    student_roll1_entry.insert(0,student_rollno)
    student_dob1_entry.insert(0,student_dob)
    student_contact1_entry.insert(0,student_contactno)
    student_email1_entry.insert(0,student_emailid)
    student_password1_entry.insert(0,student_password)
    # student_role_entry.insert(0,user_role)

    options = ['Student','Teacher']
    your_role = StringVar(edit_window)
    your_role.set(user_role)

    user_role1 = OptionMenu(edit_window , your_role , *options )
    user_role1.grid(row = 6 , column = 1 , padx = 20 , pady = 20)

    def try_update():
        update_function(student_name1_entry.get(),student_roll1_entry.get(),student_dob1_entry.get(),student_contact1_entry.get(),student_email1_entry.get(),student_password1_entry.get(),your_role.get(),student_rollno)

    def delete_entry():
        mycursor.execute(f"DELETE FROM student WHERE sei = '{student_email1_entry.get()}'")
        conn.commit()


    btn(edit_window,'Update',try_update,7,1)
    btn(edit_window,'Delete',delete_entry,8,1)

    edit_window.mainloop()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  After login button process  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def after_login():
        global enteredusername
        global enteredpassword
        enteredusername =username_entry.get()
        enteredpassword = password_entry.get()
        print(enteredusername)
        print(enteredpassword)
        if enteredusername == 'admin' and enteredpassword == 'admin':
            admin_window_function()
        elif enteredusername != 'admin' and  enteredpassword != 'admin':
            sql2 = ( f' SELECT * FROM student WHERE sei = %s AND upass = %s ')
            val2 = (enteredusername,enteredpassword)
            mycursor.execute(sql2 , val2)
            executed_query = mycursor.fetchone()
            print(executed_query)
            if executed_query[6]=='Teacher' :


                after_login_window =Tk()
                after_login_window.geometry('500x300')
                after_login_window.config(bg='green')
                
                btn(after_login_window,'Display Data',read_data,0,1)
                btn(after_login_window,'Edit',update_window_function,1,1)

                after_login_window.mainloop()
            elif executed_query[6]=='Student' :
                print('I Am A Student')
            else :
                print('Nither Student nor Teacher')
        else :
            print('Something went wrong')
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  First window Login User Window ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  
def login_window_function():


    login_window = Tk() #This is the 1st activated window
    login_window.title("This is login page") #Defines the title of the window
    login_window.geometry("800x600") # Defines the dimention of the window
    login_window.configure(background="blue") #Decides the color of the page



    labelthisas(login_window ,'Username',0,0)
    labelthisas(login_window,'Password',1,0)
    global username_entry
    global password_entry
    
    username_entry = entryfunction(login_window,0,1)
    password_entry = entryfunction(login_window,1,1)
    

    

    btn(login_window,'Login',after_login,2,1)  


    login_window.mainloop()

login_window_function()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~