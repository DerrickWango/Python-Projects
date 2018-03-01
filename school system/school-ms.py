from tkinter import *

from tkinter import ttk

from tkinter import messagebox as ms

import sqlite3

from main_db_attendance import Attendancedb

from main_db_class import classdb

from main_db_student import studentdb

from user_db import userdb




class main(Tk):
    
    def __init__(self,*args,**kwargs):

        Tk.__init__(self,*args,**kwargs)

        self.title('Attendance Management System')

        self.iconbitmap(self,default="myicon.ico")

        self.geometry("1280x550+50+50")

        main_frame = Frame(self,bg='white')

        main_frame.pack(side=TOP,fill=BOTH,expand=YES)

        main_frame.grid_rowconfigure(0,weight=1)

        main_frame.grid_columnconfigure(0,weight=1)

        self.frames={}

        for F in (startpage,mainpage,signup,Class,student,attendance,view_records,Admin):

            frame=F(main_frame,self)

            self.frames[F]= frame

            frame.grid(row=0,column=0,sticky='nsew')
            
        with sqlite3.connect('maindb.db') as db:

            cursor=db.cursor()

        initialize=('SELECT * FROM User')

        cursor.execute(initialize)

        user=cursor.fetchall()

        if user:

            self.show_frame(startpage)

        else:

            self.show_frame(signup)



    def show_frame(self,cont):
        
        frame=self.frames[cont]
        
        frame.tkraise()



class startpage(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.config(height=350,width=700)

        self.controller = controller

        self.username=StringVar()

        self.password=StringVar()

        label0=Label(self,text='Attendance Management System ',fg='steel blue',anchor='w',font='Times 30 bold italic')

        label0.place(anchor='c',relx=0.5,rely=0.1)

        label0=Label(self,text='Login',fg='steel blue',anchor='w',font='Times 15 bold italic')

        label0.place(anchor='c',relx=0.5,rely=0.4)

        label1= Label(self,text='Username',font='verdana 10 bold',fg='steel blue')

        label1.place(anchor='c',relx=0.4,rely=0.5)

        label2=Label(self,text='password',font='verdana 10 bold',fg='steel blue')

        label2.place(anchor='c',relx=0.4,rely=0.6)

        entry1=Entry(self,bd=10,textvariable=self.username)

        entry1.place(anchor='c',relx=0.6,rely=0.5)

        entry2=Entry(self,bd=10,textvariable=self.password,show='*')

        entry2.place(anchor='c',relx=0.6,rely=0.6)

        btn1=ttk.Button(self,text='login',command=self.login,width=30)

        btn1.place(anchor='c',relx=0.6,rely=0.7)

        btn1=ttk.Button(self,text='Add new user',command=self.show_admin,width=30)

        btn1.place(anchor='c',relx=0.4,rely=0.7)

    def show_admin(self):

        return self.controller.show_frame(Admin),self.username.set(''),self.password.set('')


    def login(self,Event=None):

        while True:

            with sqlite3.connect('maindb.db') as db:

                cursor=db.cursor()

            find_user= ("SELECT * FROM User WHERE username=? AND password =? ")

            cursor.execute(find_user,[(self.username.get()),(self.password.get())])

            result=cursor.fetchall()

            if result:

                for i in result:

                    return self.controller.show_frame(mainpage),self.username.set(''),self.password.set('')
                        
                        

            else:

                return self.username.set('User not found!!'), self.password.set('')





class Admin(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        self.password=StringVar()

        label1= Label(self,text='Enter Admin password',font='verdana 10 bold',fg='steel blue')

        label1.place(anchor='c',relx=0.4,rely=0.4)

        entry1=Entry(self,bd=10,textvariable=self.password,show='*')

        entry1.place(anchor='c',relx=0.6,rely=0.4)

        btn1=ttk.Button(self,text='login',command=self.Login,width=30)

        btn1.place(anchor='c',relx=0.6,rely=0.7)

        btn1=ttk.Button(self,text='back',command=self.back,width=30)

        btn1.place(anchor='c',relx=0.4,rely=0.7)

    def back(self):

        return self.controller.show_frame(startpage) ,self.password.set('')


    def Login(self):
        
            while True:

                        with sqlite3.connect('maindb.db') as db:

                            cursor=db.cursor()

                        find_user= ("SELECT * FROM User WHERE password =? ")

                        cursor.execute(find_user,[(self.password.get())])

                        result=cursor.fetchall()

                        if result:

                            for i in result:

                                return self.controller.show_frame(signup),self.password.set('')
                                    
                                    

                        else:

                            return ms.showinfo('Error','User not found!'),self.password.set('')


class signup(Frame):

    def __init__(self,parent,controller):

                Frame.__init__(self,parent)

                self.controller = controller

                self.username=StringVar()

                self.firstname=StringVar()

                self.surname=StringVar()

                self.password=StringVar()

                label0=Label(self,text='Sign up',fg='steel blue',anchor='w',font='Times 20 bold italic')

                label0.place(anchor='c',relx=0.5,rely=0.1)

                label0=Label(self,text="Add Admin account if It's your first time",fg='steel blue',anchor='w',font='Arial 7 bold ')

                label0.place(anchor='c',relx=0.5,rely=0.3)

                label1= Label(self,text='Username',font='verdana 10 bold',fg='steel blue')

                label1.place(anchor='c',relx=0.4,rely=0.4)

                label2= Label(self,text='Firstname',font='verdana 10 bold',fg='steel blue')

                label2.place(anchor='c',relx=0.4,rely=0.5)
                        
                label3= Label(self,text='surname',font='verdana 10 bold',fg='steel blue')

                label3.place(anchor='c',relx=0.4,rely=0.6)

                label4=Label(self,text='password',font='verdana 10 bold',fg='steel blue')

                label4.place(anchor='c',relx=0.4,rely=0.7)

                entry1=Entry(self,bd=10,textvariable=self.username)

                entry1.place(anchor='c',relx=0.6,rely=0.4)

                entry2=Entry(self,bd=10,textvariable=self.firstname)

                entry2.place(anchor='c',relx=0.6,rely=0.5)

                entry3=Entry(self,bd=10,textvariable=self.surname)

                entry3.place(anchor='c',relx=0.6,rely=0.6)

                entry4=Entry(self,bd=10,textvariable=self.password,show='*')

                entry4.place(anchor='c',relx=0.6,rely=0.7)

                btn1=ttk.Button(self,text='Login instead',command=self.Return,width=30)

                btn1.place(anchor='c',relx=0.4,rely=0.8)

                btn2=ttk.Button(self,text='Sign up',command=self.sign_up,width=30)

                btn2.place(anchor='c',relx=0.6,rely=0.8)

    def Return(self):

        return self.controller.show_frame(startpage),self.username.set(''),self.firstname.set(''),self.surname.set(''),self.password.set('')


    def validation(self):

                    return len(self.username.get()) != 0 and len(self.firstname.get()) != 0 and len(self.surname.get()) != 0 and len(self.password.get()) != 0

    def sign_up(self):

                    if self.validation():
                        
                                        
                                        found=0
                                        
                                        while found==0:

                                                with sqlite3.connect('maindb.db') as db:

                                                        cursor=db.cursor()

                                                finduser=("SELECT * FROM User WHERE username=? AND password=?")

                                                cursor.execute(finduser,[(self.username.get()),(self.password.get())])

                                                results=cursor.fetchall()

                                                if results:

                                                        return ms.showinfo("Error","User already exists!"),self.username.set(''),self.firstname.set(''),self.surname.set(''),self.password.set('')
                                                
                                                else:
                                                        found=1



                                        
                                        new_user=("""INSERT INTO User(username,firstname,surname,password)

                                                                          VALUES(?,?,?,?)""") 

                                        cursor.execute(new_user,[(self.username.get()),(self.firstname.get()),(self.surname.get()),(self.password.get())])

                                        db.commit()

                                        cursor.close()

                                        db.close()

                                        ms.showinfo("confirm","Added to database.")

                                        self.username.set('')

                                        self.firstname.set('')

                                        self.surname.set('')

                                        self.password.set('')






                    else:
                            

                                        return ms.showinfo("Error","Insert required Fields!")
                                                                                




                    

class mainpage(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.controller=controller

        lbl=Label(self,text='Attendance management system',font='Times 30 bold italic',fg='steel blue')

        lbl.place(anchor='c',relx=0.5,rely=0.1)

        btn1=Button(self,text='New class Record',bg='steel blue',font='verdana 10 bold',height=7,width=50,command=lambda:self.controller.show_frame(Class),bd=10)

        btn1.place(anchor='c',relx=0.3,rely=0.4)

        btn2=Button(self,text='New student',bg='steel blue',font='verdana 10 bold',height=7,width=50,command=lambda:self.controller.show_frame(student),bd=10)

        btn2.place(anchor='c',relx=0.7,rely=0.4)

        btn3=Button(self,text='New Attendance record',bg='steel blue',font='verdana 10 bold',height=7,width=50,command=lambda:self.controller.show_frame(attendance),bd=10)

        btn3.place(anchor='c',relx=0.3,rely=0.7)

        btn4=Button(self,text='View records',bg='steel blue',font='verdana 10 bold',height=7,width=50,command=lambda:self.controller.show_frame(view_records),bd=10)

        btn4.place(anchor='c',relx=0.7,rely=0.7)

        btn=ttk.Button(self,text='log out',command=self.logout)

        btn.place(anchor='sw',relx=0.9,rely=0.99)




    def logout(self):

        return self.controller.show_frame(startpage)
        
    

        



class student(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        btn=ttk.Button(self,text='Home',command=lambda:controller.show_frame(mainpage))

        btn.place(anchor='ne',relx=0.07,rely=0.05)

        self.Gr_no=StringVar()

        self.Firstname=StringVar()

        self.Lastname=StringVar()

        self.class_choose=StringVar()

        self.Roll_no=StringVar()

        lbl=Label(self,text=' Add new student ',fg='steel blue',font='Times 25 bold italic')

        lbl.place(anchor='c',relx=0.5,rely=0.1)

        label1= Label(self,text='Gr no. : ',font='verdana 10 bold',fg='steel blue')

        label1.place(anchor='c',relx=0.2,rely=0.4)

        label2= Label(self,text='First Name   :',font='verdana 10 bold',fg='steel blue')

        label2.place(anchor='c',relx=0.2,rely=0.5)
                        
        label3= Label(self,text='Last Name   :',font='verdana 10 bold',fg='steel blue')

        label3.place(anchor='c',relx=0.2,rely=0.6)

        label3= Label(self,text='Class   :',font='verdana 10 bold',fg='steel blue')

        label3.place(anchor='c',relx=0.2,rely=0.7)

        label3= Label(self,text='Roll no.   :',font='verdana 10 bold',fg='steel blue')

        label3.place(anchor='c',relx=0.2,rely=0.8)

        entry1=Entry(self,textvariable=self.Gr_no,bd=5,bg='white',width=50)

        entry1.place(anchor='c',relx=0.4,rely=0.4)

        entry2=Entry(self,textvariable=self.Firstname,bd=5,bg='white',width=50)

        entry2.place(anchor='c',relx=0.4,rely=0.5)

        entry3=Entry(self,textvariable=self.Lastname,bd=5,bg='white',width=50)

        entry3.place(anchor='c',relx=0.4,rely=0.6)

        entry4=Entry(self,textvariable=self.class_choose,bd=5,bg='white',width=50)
        
        entry4.place(anchor='c',relx=0.4,rely=0.7)

        entry5=Entry(self,textvariable=self.Roll_no,bd=5,bg='white',width=50)
        
        entry5.place(anchor='c',relx=0.4,rely=0.8)

        btn=Button(self,text='Add',bg='steel blue',font='Times 10 bold italic',bd=10,width=50,command=self.Add_student)

        btn.place(anchor='c',relx=0.4,rely=0.9)

    def validate_student(self):

        return len(self.Gr_no.get()) != 0 and len(self.Firstname.get()) != 0 and len(self.Lastname.get()) != 0 and len(self.class_choose.get()) != 0 and len(self.Roll_no.get()) !=0

        

    def Add_student(self):
        

            if self.validate_student():

                found1=0
                
                while found1==0:

                    with sqlite3.connect('maindb.db') as db:

                        cursor=db.cursor()

                    find_student=('SELECT * FROM Student WHERE Grno=?')

                    cursor.execute(find_student,[(self.Gr_no.get())])

                    result=cursor.fetchall()

                    if result:

                        return ms.showinfo('Error','Student already exists!'),self.Gr_no.set(''),self.Firstname.set(''),self.Lastname.set(''),self.class_choose.set(''),self.Roll_no.set('')

                    else:
                        found1=1
                        

                insert_student=('''INSERT INTO Student(Grno,firstname,lastname,class,Rollno)

                                VALUES(?,?,?,?,?)''')

                cursor.execute(insert_student,[(self.Gr_no.get()),(self.Firstname.get()),(self.Lastname.get()),(self.class_choose.get()),(self.Roll_no.get())])

                db.commit()

                cursor.close()

                db.close()

                ms.showinfo('Confirm','added to records')

                self.Gr_no.set('')

                self.Firstname.set('')

                self.Lastname.set('')

                self.class_choose.set('')

                self.Roll_no.set('')

            else:

                ms.showinfo('Error','Enter Required Fields!')



        




class attendance(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        btn=ttk.Button(self,text='Home',command=lambda:controller.show_frame(mainpage))

        btn.place(anchor='ne',relx=0.07,rely=0.05)

        lbl=Label(self,text='Add attendance record',fg='steel blue',font='Times 25 bold italic')

        lbl.place(anchor='c',relx=0.5,rely=0.1)



        
class Class(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        self.Class_Name=StringVar()

        self.Subjects=StringVar()

        self.Roll_no=StringVar()

        btn=ttk.Button(self,text='Home',command=lambda:controller.show_frame(mainpage))

        btn.place(anchor='ne',relx=0.07,rely=0.05)

        lbl=Label(self,text='Add New Class',fg='steel blue',font='Times 25 bold italic')

        lbl.place(anchor='c',relx=0.5,rely=0.1)

        label1= Label(self,text='Class Name : ',font='verdana 10 bold',fg='steel blue')

        label1.place(anchor='c',relx=0.2,rely=0.4)

        label2= Label(self,text='Subjects   :',font='verdana 10 bold',fg='steel blue')

        label2.place(anchor='c',relx=0.2,rely=0.5)
                        
        label3= Label(self,text='Starting Roll no.   :',font='verdana 10 bold',fg='steel blue')

        label3.place(anchor='c',relx=0.2,rely=0.6)

        entry1=Entry(self,textvariable=self.Class_Name,bd=5,bg='white',width=50)

        entry1.place(anchor='c',relx=0.4,rely=0.4)

        entry2=Entry(self,textvariable=self.Subjects,bd=5,bg='white',width=50)

        entry2.place(anchor='c',relx=0.4,rely=0.5)

        entry3=Entry(self,textvariable=self.Roll_no,bd=5,bg='white',width=50)

        entry3.place(anchor='c',relx=0.4,rely=0.6)

        btn=Button(self,text='Add',bg='steel blue',font='Times 10 bold italic',bd=10,width=50,command=self.Class_page)

        btn.place(anchor='c',relx=0.4,rely=0.8)


        

    def valid_details(self):

                    return len(self.Class_Name.get()) != 0 and len(self.Subjects.get()) != 0 and len(self.Roll_no.get()) != 0 


        


    def Class_page(self):

        if self.valid_details():

                with sqlite3.connect("maindb.db") as db:

                    cursor=db.cursor()


                insert_class=("""INSERT INTO  Class(Classname,Subjects,Startingrollno)

                                 VALUES(?,?,?)""")

                cursor.execute(insert_class,[(self.Class_Name.get()),(self.Subjects.get()),(self.Roll_no.get())])

                db.commit()

                cursor.close()

                db.close()

                ms.showinfo("Confirm" , "Added to Records")

                self.Class_Name.set('')

                self.Subjects.set('')

                self.Roll_no.set('')


        else:

                ms.showinfo("Error","Enter required fields!")


class view_records(Frame):

    def __init__(self,parent,controller):

        Frame.__init__(self,parent)

        btn=ttk.Button(self,text='Home',command=lambda:controller.show_frame(mainpage))

        btn.place(anchor='ne',relx=0.07,rely=0.05)

        lbl=Label(self,text='View Records',fg='steel blue',font='Times 25 bold italic')

        lbl.place(anchor='c',relx=0.5,rely=0.1)



                  








userdb()

app=main()

Attendancedb()

classdb()

studentdb()

app.mainloop()










                    
