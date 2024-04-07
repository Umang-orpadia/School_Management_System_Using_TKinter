import tkinter
from tkinter import *
import mysql.connector

conn = mysql.connector.connect(host = "localhost" ,database='IOTPro', user = "root" , password = "khushi@5885")
mycursor = conn.cursor()
mycursor.execute('use iotpro;')

# ~~~~~~~~~~~~~~~~~~~~  Reading Data ~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_data_function():
    read_window = Tk()
    read_window.geometry('1915x1075+0+0')
    mycursor.execute('SELECT * FROM test1 ')
    fetch_data = mycursor.fetchall()
    m=0
    for i in fetch_data:
        for j in range(len(i)):
            e = Label(read_window , text=i[j] ,font="lucida 20 bold", bg='red' , fg='white' )
            e.grid(row=m,column=j , padx=10 , pady=10)
            print(i[j] , end=' ')
        m=m+1
        print('\n')
    btnclo = Button(read_window,text='Close',command=lambda:read_window.destroy())
    btnclo.grid(row=405 , column=0)    
    read_window.mainloop()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
# ~~~~~~~~~~~~~~~~~~~~ Add user ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def add_user_function():
    add_user_window = Tk()
    add_user_window.geometry('1915x1075+0+0')
    add_user_window.title("This is the adding user window")

    name_lable = Label(add_user_window,text='Enter Your Name : ')
    name_lable.grid(row=0,column=0)

    name_input = Entry(add_user_window)
    name_input.grid(row=0 , column=1)
    
    roll_lable = Label(add_user_window,text='Enter Your RollNo : ')
    roll_lable.grid(row=1,column=0)

    roll_input = Entry(add_user_window)
    roll_input.grid(row=1 , column=1)
    
    Attend_label = Label(add_user_window , text='Addendence')
    Attend_label.grid(row=2 , column=0)
    
    checking1 = BooleanVar(add_user_window)
    print(checking1)
    Attend_entry = Checkbutton(add_user_window,variable=checking1 , text='OPtion')
    Attend_entry.grid(row=2 , column=1)
    
    def adding_details_function():
        print(checking1)
        checking2  = checking1.get()
        checking = int(checking2)
        print(checking)
        Name = name_input.get()
        Roll_no = roll_input.get()
        Attend = checking

        mycursor.execute(f"INSERT INTO test1(name,roll,attend) values('{Name}','{Roll_no}',{Attend});")
        print(Name , Roll_no ,Attend)
        conn.commit()

    btnAdd = Button(add_user_window,text='Add Details', command=adding_details_function)
    btnAdd.grid(row=44,column=0)

    btnclo = Button(add_user_window,text='Close',command=lambda:add_user_window.destroy())
    btnclo.grid(row=45 , column=0)    
    
    add_user_window.mainloop()
    
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        
# ~~~~~~~~~~~~~~~~~~~~~~~~~  Entry Window ~~~~~~~~~~~~~~~~~~~~~~~~~~
def entry_window_function():
    entry_window = Tk()
    entry_window.geometry('1915x1075+0+0')
    entry_window.title('Entry Window')
    btn1 = Button(entry_window , text= 'Read Data', command=read_data_function)
    btn1.grid(row=0,column=0)
    btn2 = Button(entry_window,text='Add user',command=add_user_function)
    btn2.grid(row=1, column=0)
    btnclo = Button(entry_window,text='Close',command=lambda:entry_window.destroy())
    btnclo.grid(row=2 , column=0)
    entry_window.mainloop()
    
entry_window_function()
conn.close()
print("connection closed")
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~