# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Require Modules ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from tkinter import *
import firebase_admin
from firebase_admin import db , credentials
# from tkcalendar import Calendar , DateEntry
from tkcalendar import *
import datetime
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Database Connection Part ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
cred = credentials.Certificate('IOTproject/credentials.json')
firebase_admin.initialize_app(cred,{"databaseURL":"https://iotproject-bcff9-default-rtdb.asia-southeast1.firebasedatabase.app/"})
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Readind data function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def read_data_function():
    # @DeprecationWarning       !!!!!!!!!!!!!!!!!!!!!       Reading Data Not Updated        !!!!!!!!!!!!!!!
    read_data_window = Tk()
    read_data_window.title('Reading Attendence data from database')
    read_data_window.geometry('1915x1075+0+0')
    reading_data_frame = Frame(read_data_window,bd='10',relief='groove')
    # reading_data_frame.place(x=10,y=10,height=350,width=1000)
    reading_data_frame.grid(row=2,column=0,rowspan=20,columnspan=20)

    cal = DateEntry(read_data_window , width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern="dd-mm-yyyy",font="lucida 20 bold")    
    cal.grid(row=0 ,column=0)
    # Name_lable = Label(read_data_window,text='Enter Your Name : ',font="lucida 20 bold",bg="powder blue")
    # Name_lable.grid(row=1,column=0)

    # Name_Entry = Entry(read_data_window,font="lucida 20 bold",bg="powder blue")
    # Name_Entry.grid(row=1,column=1)


    def Show_attendence_data_for_student():
        lecture_date = db.reference(f'/lecture').get(shallow=True)
        lecture_date_list = list(lecture_date.keys())
        row_counter = 0
        column_counter = 0
        for i in lecture_date_list:
            if str(cal.get_date()) == i:

                Label(reading_data_frame,text='Date').grid(row=row_counter,column=column_counter)

                row_counter += 1 #1
                column_counter += 1 #1

                Label(reading_data_frame,text=f'{i}').grid(row=row_counter,column=column_counter)

                row_counter += 1 #2
                column_counter += 1 #2

                lecture_duration = db.reference(f'/lecture/{i}/').get(shallow=True)
                lecture_duration_list = list(lecture_duration.keys())

                for j in lecture_duration_list:

                    Label(reading_data_frame,text=f'{j}').grid(row=row_counter,column=2)

                    row_counter += 1 #3
                    column_counter += 1 #3

                    lecture_subject_fetch = db.reference(f'/lecture/{i}/{j}/Subject').get()
                    Label(reading_data_frame,text=lecture_subject_fetch).grid(row=row_counter - 1,column=3)

                    # row_counter +=1

                    try :
                        attendes_from_database = db.reference(f'/lecture/{i}/{j}/Attendes/').get(shallow=True)
                        attendes_from_database_list = list(attendes_from_database.keys())
                        # print(attendes_from_database_list,attendes_from_database)


                        for k in attendes_from_database_list:

                            row_counter += 1 #4
                            column_counter += 1 #4

                            Label(reading_data_frame,text=f'{k}').grid(row=row_counter,column = 3)
                            row_counter +=1
                    except AttributeError:
                        print('no further data found')
                        Label(reading_data_frame,text='No further Data found').grid(row=row_counter,column=3)
                        row_counter += 1
                    # lecture_details = db.reference(f'/lecture/{i}/{j}').get(shallow=True)
                    # lecture_details_list = list(lecture_details)
                    # for k in lecture_details_list:
                        

            else:
                print('show attendence else block')
                # print(str(cal.get_date()))

    btn_Show_record = Button(read_data_window,text='Show',command=Show_attendence_data_for_student,font="lucida 20 bold",bg="light green",fg="red",width=25)
    btn_Show_record.grid(row=23,column=0)
    btnclo = Button(read_data_window,text='Close',command=lambda:read_data_window.destroy(),font="lucida 20 bold",bg="red",fg="light green",width=25)
    btnclo.grid(row=24 , column=0)
    # btnclo.place(x=420,y=1550)

    read_data_window.mainloop()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Adding User Function ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def add_user_function():
    add_user_window = Tk()
    add_user_window.geometry('1915x1075+0+0')
    add_user_window.title('This is the Adding User Window')

    Register_frame = Frame(add_user_window,bd='10',relief='groove')
    Register_frame.place(x=550,y=150,height=400,width=800)

    name_lable = Label(Register_frame,text='Enter Your Name : ',font="lucida 20 bold",bg="powder blue")
    name_lable.grid(row=0,column=0,padx=10,pady=10)

    name_input = Entry(Register_frame,font="lucida 20 bold",bg="powder blue",bd='10',relief=SUNKEN)
    name_input.grid(row=0 , column=1)
    
    roll_lable = Label(Register_frame,text='Enter Rollno',font="lucida 20 bold",bg="powder blue")
    roll_lable.grid(row=1,column=0)

    roll_input = Entry(Register_frame,font="lucida 20 bold",bg="powder blue",bd='10',relief=SUNKEN)
    roll_input.grid(row=1 , column=1)

    email_id_lable = Label(Register_frame,text='Email Id',font="lucida 20 bold",bg="powder blue")
    email_id_lable.grid(row=2,column=0)

    email_id_entry = Entry(Register_frame,font="lucida 20 bold",bg="powder blue",bd='10',relief=SUNKEN)
    email_id_entry.grid(row=2,column=1)
    
    password_lable = Label(Register_frame,text='Enter Password',font="lucida 20 bold",bg="powder blue")
    password_lable.grid(row=3,column=0)

    password_input = Entry(Register_frame,font="lucida 20 bold",bg="powder blue",bd='10',relief=SUNKEN)
    password_input.grid(row=3,column=1)

    feedback_lable = Label(Register_frame,font="lucida 20 bold",bg="powder blue")
    feedback_lable.grid(row=4,column=1)


    def changeabc(*args): 
        your_role1= your_role.get()
        if your_role1 == 'Student':
            print('Traced student')
            roll_lable.config(text='Rollno : ')
        elif your_role1 == 'Teacher':
            print('Traced Teacher')
            roll_lable.config(text='Subject : ')
        else:
            print('Unable to trace')

    options = ['Student','Teacher']
    your_role = StringVar(Register_frame)
    your_role.set('Student')

    user_role = OptionMenu(Register_frame , your_role , *options )
    user_role.grid(row = 5 , column = 1 )
    user_role.configure(bg='#afff00',width = 10,font="lucida 20 bold",fg='red')
    your_role.trace_add('write',changeabc)

    def Register_user():
        db.reference(f'/student/{email_id_entry.get()}').child('email').set(f'{email_id_entry.get()}')
        db.reference(f'/student/{email_id_entry.get()}').child('name').set(f"{name_input.get()}")
        db.reference(f'/student/{email_id_entry.get()}').child('password').set(f"{password_input.get()}")
        if your_role.get() == 'Student':
            db.reference(f'/student/{email_id_entry.get()}').child('Rollno').set(f"{roll_input.get()}")
        else:
            db.reference(f'/student/{email_id_entry.get()}').child('Subject').set(f"{roll_input.get()}")
        db.reference(f'/student/{email_id_entry.get()}').child('Role').set(f"{your_role.get()}")
        
        feedback_lable.config(text='Inserted Sucessfully')

    register_user_btn = Button(Register_frame,text='Register',command=Register_user,font="lucida 20 bold",bg="light green",fg="red",width=25)
    register_user_btn.grid(row=4,column=0)

    btnclo = Button(Register_frame,text='Close',command=lambda:add_user_window.destroy(),font="lucida 20 bold",bg="red",fg="light green",width=25)
    btnclo.grid(row=5 , column=0)

    add_user_window.mainloop()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Lecture Schedule ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def lecture_schedule_function():
    lecture_schedule_window = Tk()
    lecture_schedule_window.geometry('1915x1075+0+0')
    lecture_schedule_window.title('This the Lecture Scheduling Window')

    Label(lecture_schedule_window,text='Select Date',font="lucida 20 bold").grid(row=0,column=0)

    cal = DateEntry(lecture_schedule_window, width= 16, background= "magenta3", foreground= "white",bd=2, date_pattern="dd-mm-yyyy",font="lucida 20 bold")
    cal.grid(row=0 ,column=1)
    
    Label(lecture_schedule_window,text='From',font="lucida 20 bold").grid(row=1,column=0)

    from_hour = Spinbox(lecture_schedule_window,from_=0,to=23,font="lucida 20 bold")
    from_hour.grid(row=1,column=1)

    from_minutes = Spinbox(lecture_schedule_window,from_=0,to=59,font="lucida 20 bold")
    from_minutes.grid(row=1,column=2)

    Label(lecture_schedule_window,text='To',font="lucida 20 bold").grid(row=2,column=0)

    to_from_hour = Spinbox(lecture_schedule_window,from_=0,to=23,font="lucida 20 bold")
    to_from_hour.grid(row=2,column=1)

    to_from_minutes = Spinbox(lecture_schedule_window,from_=0,to=59,font="lucida 20 bold")
    to_from_minutes.grid(row=2,column=2)


    subject_name_lable = Label(lecture_schedule_window,text='Enter Subject',font="lucida 20 bold")
    subject_name_lable.grid(row=3,column=0)

    subject_input = Entry(lecture_schedule_window,font="lucida 20 bold")
    subject_input.grid(row=3,column=1)

    btn_frame = Frame(lecture_schedule_window,bd='10',relief='groove')
    btn_frame.place(x=100,y=200,height=200,width=460)

    def scheduling_lecture():
        c = from_hour.get() +"_"+from_minutes.get()+"_To_"+ to_from_hour.get()+"_"+to_from_minutes.get()
        e = from_hour.get() +"_"+from_minutes.get()
        d = to_from_hour.get() +"_"+to_from_minutes.get()
        db.reference(f'/lecture/{cal.get_date()}/{c}').child('Start_time').set(f'{e}')
        db.reference(f'/lecture/{cal.get_date()}/{c}').child('End_time').set(f'{d}')
        db.reference(f'/lecture/{cal.get_date()}/{c}').child('Subject').set(f'{subject_input.get()}')
    schedule_btn = Button(btn_frame,text='Schedule',command=scheduling_lecture,font="lucida 20 bold",bg="light green",fg="red",width=25)
    schedule_btn.grid(row=4,column=0)

    def Lecture_displaying_function():
        the_schedule_display_frame = Frame(lecture_schedule_window,bd=10,relief=GROOVE)
        # the_schedule_display_frame.grid(row=5,column=0)
        the_schedule_display_frame.place(x=600,y=200,height=700,width=1000)
        lecture_date = db.reference(f'/lecture').get(shallow=True)
        lecture_date_list = list(lecture_date.keys())
        row_count = 0
        column_count = 0
        for i in lecture_date_list:
            column_count = 0
            # row_count = 0
            Label(the_schedule_display_frame,text=i,font="lucida 10 bold").grid(row=row_count,column=column_count)
            column_count +=1
            lecture_timeing = db.reference(f'/lecture/{i}').get(shallow=True)
            lecture_timeing_list = list(lecture_timeing.keys())
            for j in lecture_timeing_list:
                
                Label(the_schedule_display_frame,text=j,font="lucida 10 bold").grid(row=row_count,column=column_count)
                column_count +=1
                hours = db.reference(f'/lecture/{i}/{j}/Start_time').get()
                Minute = db.reference(f'/lecture/{i}/{j}/End_time').get()
                Subject = db.reference(f'/lecture/{i}/{j}/Subject').get()
                print(hours,Minute,Subject)
                Label(the_schedule_display_frame,text=hours,font="lucida 10 bold").grid(row=row_count,column=column_count)
                column_count +=1
                # row_count +=1
                Label(the_schedule_display_frame,text=Minute,font="lucida 10 bold").grid(row=row_count,column=column_count)
                column_count +=1
                # row_count +=1
                Label(the_schedule_display_frame,text=Subject,font="lucida 10 bold").grid(row=row_count,column=column_count)
                column_count +=1

            row_count +=1

    # Lecture_displaying_function()
    show_schedule_btn = Button(btn_frame,text='Refresh',command=Lecture_displaying_function,font="lucida 20 bold",bg="light green",fg="red",width=25)
    show_schedule_btn.grid(row=5,column=0)

    btnclo = Button(btn_frame,text='Close',command=lambda:lecture_schedule_window.destroy(),font="lucida 20 bold",bg="red",fg="light green",width=25)
    btnclo.grid(row=16 , column=0)

    lecture_schedule_window.mainloop()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~Attendence Marking ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def Attendence_marking_function():
    attendence_marking_window = Tk()
    attendence_marking_window.title('This is Attendence marking Window')
    attendence_marking_window.geometry('1915x1075+0+0')

    Name_label = Label(attendence_marking_window,text='Enter Name',font="lucida 20 bold")
    Name_label.grid(row=0,column=0)
    Name_entry = Entry(attendence_marking_window,font="lucida 20 bold")
    Name_entry.grid(row=0,column=1)

    Email_id_label = Label(attendence_marking_window,text='Enter Email id: ',font="lucida 20 bold")
    Email_id_label.grid(row=1 , column=0)
    Email_id_entry = Entry(attendence_marking_window,font="lucida 20 bold")
    Email_id_entry.grid(row=1,column=1)

    def mark_attendence():
        a = datetime.datetime.now()
        b = a.strftime('%Y/%m/%d/%H/%M')
        c=b.split('/')
        Currrent_time = c[3]+""+c[4]
        day = c[2]
        month = c[1]
        year = c[0]
        date = year+'-'+month+'-'+day
        
        retrive = db.reference('/lecture')
        snapshot = retrive.get(shallow=True)
        yeye = list(snapshot.keys())
        for i in yeye:
            if i == date:
                duration_retrive = db.reference(f'/lecture/{i}').get(shallow=True)
                duration_list = list(duration_retrive.keys())
                print(duration_list)
                flag = 0
                for i in duration_list:
                    x = i.split('_')
                    start_time = x[0]+''+x[1]
                    end_time = x[3]+''+x[4]
                    if start_time <= Currrent_time <= end_time:
                        lec_details = db.reference(f'/lecture/{date}/{i}/Subject')
                        db.reference(f'/Attendence/{Email_id_entry.get()}/{date}').child('Time').set(Currrent_time)
                        db.reference(f'/Attendence/{Email_id_entry.get()}/{date}').child('name').set(Name_entry.get())
                        db.reference(f'/Attendence/{Email_id_entry.get()}/{date}').child('email').set(Email_id_entry.get())
                        db.reference(f'/Attendence/{Email_id_entry.get()}/{date}/Lecture/{start_time+"_"+end_time}').child(f'{lec_details.get()}').set(Currrent_time)
                        db.reference(f'/lecture/{date}/{i}/Attendes/').child(f'{Email_id_entry.get()}').set(f'{Name_entry.get()}')
                        print('Attendence Sucessfull')
                        flag = 1
                    # elif end_time <= Currrent_time:
                    #     print('You are late')
                    elif start_time >= Currrent_time :
                        print('You are early')
                    else :
                        print('something went wrong with the attendnece mark timing')
                if flag == 0:
                    print('No Lecture At This Time')
                elif flag == 1:
                    print('Attendence Updated')
                else : 
                    print('Crazy Crazy')
            elif i != date:
                pass
            else:
                print('Today No Lectures')

    att_btn = Button(attendence_marking_window,text='Mark',command=mark_attendence,font="lucida 20 bold",bg="light green",fg="red",width=15)
    att_btn.grid(row=5 , column=0)

    clontn = Button(attendence_marking_window,text='Close',command=lambda:attendence_marking_window.destroy(),font="lucida 20 bold",bg="red",fg="light green",width=15)
    clontn.grid(row=6, column=0)
    attendence_marking_window.mainloop()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Entry Window , Login Window~~~~~~~~~~~~~~~~~~~~~~~~~
def entry_window_function():
    entry_window = Tk()
    entry_window.geometry('1915x1075+0+0')
    entry_window.title('This is the entry window')
    entry_window.configure(background='powder blue')

    login_frame = LabelFrame(entry_window,text='Login',bd='10',relief='groove')
    login_frame.place(x=600,y=100,height=600,width=700)
    login_frame.configure(background='powder blue')

    Email_id_lable = Label(login_frame,text='Email_id',font="lucida 20 bold",bg="powder blue")
    Email_id_lable.grid(row=0,column=0,padx=10,pady=10)

    Email_id_entry = Entry(login_frame,font="lucida 20 bold",bg="powder blue",bd='10',relief=SUNKEN)
    Email_id_entry.grid(row=0,column=1,padx=10,pady=10)

    password_id_lable = Label(login_frame,text='password',font="lucida 20 bold",bg="powder blue")
    password_id_lable.grid(row=1,column=0,padx=10,pady=10)

    password_id_entry = Entry(login_frame,font="lucida 20 bold",bg="powder blue",bd='10',relief=SUNKEN)
    password_id_entry.grid(row=1,column=1,padx=10,pady=10)

    message_lable = Label(login_frame,font="lucida 20 bold",bg="powder blue")
    message_lable.grid(row=2,column=1,padx=10,pady=10)

    btn_frame = Frame(login_frame,bd='10',relief='groove')
    btn_frame.place(x=100,y=200,height=360,width=460)
    
    def login_function():
        checkit = db.reference(f'/student/{Email_id_entry.get()}/email').get()
        email = Email_id_entry.get()

        checkit2 = db.reference(f'/student/{Email_id_entry.get()}/password').get()
        password = password_id_entry.get()

        if email == checkit and password == checkit2:
            # Label(entry_window,text='Login SUcessfull').grid(row=4,column=0)
            message_lable.config(text='Login Sucessfull')
        else :
            print(checkit,email)
            message_lable.config(text='Incorrect Username Or password')
            # Label(entry_window,text='Invalid Username or password').grid(row=4,column=0)
            # Label(entry_window,text=f'{Email_id_entry.get(),checkit.get()}').grid(row=4,column=0)


    login_btn = Button(btn_frame,text='Login',command=login_function,font="lucida 20 bold",bg="light green",fg="red",width=25)
    login_btn.grid(row=2,column=0)

    add_user_btn = Button(btn_frame,text='Add User',command=add_user_function,font="lucida 20 bold",bg="light green",fg="red",width=25)
    add_user_btn.grid(row=5,column=0)

    read_btn = Button(btn_frame,text='Read Data',command=read_data_function,font="lucida 20 bold",bg="light green",fg="red",width=25)
    read_btn.grid(row=3,column=0)

    lec_schedule_btn = Button(btn_frame,text='Schedule Lecture',command=lecture_schedule_function,font="lucida 20 bold",bg="light green",fg="red",width=25)
    lec_schedule_btn.grid(row=6,column=0)

    attendence_btn = Button(btn_frame,text='Attendence Mark',command=Attendence_marking_function,font="lucida 20 bold",bg="light green",fg="red",width=25)
    attendence_btn.grid(row=7,column=0)

    btnclo = Button(btn_frame,text='Close',command=lambda:entry_window.destroy(),font="lucida 20 bold",bg="red",fg="light green",width=25)
    btnclo.grid(row=16 , column=0)


    entry_window.mainloop()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

entry_window_function()

# read_data_function()
# lele = db.reference().update

# print(lele.get())
# ~~~~~~~~~~~~~~~~~~~~ Read Replace update delete ~~~~~~~~~~~~~~~~~~~~~~~~
# db.reference('/').update({'student_detail':['python','java','c++']})
# db.reference('/').update({'student_detail':{'language':['python','java','c++']}})
# db.reference('/student_detail/language').child('first').set('other')
# print(db.reference('/name').get())
# db.reference('/name').set({'sd':'asdasdasdasdas'})
# db.reference('/student_detail/language/').push().set('javascript')
# print(db.reference('/').get())
# db.reference('/name/sd').delete()
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
