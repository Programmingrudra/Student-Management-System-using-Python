from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox,ttk
import mysql.connector
import pandas as pd

conn = mysql.connector.connect(host='localhost', password='datascience2025', user = 'root')
if conn.is_connected():
    print(" Database Connection established....")

curobj = conn.cursor(buffered = True)
curobj.execute('use litdb;')

background = "#06283D"
framebg = "#EDEDED"
framefg= "#06283D"

def Exit():
    username=entry1.get()
    password=entry2.get()
    
    if (username=="" and password==""):
        messagebox.showinfo("","Thank you !!")
        window.destroy()
    else:
        messagebox.showinfo("","Thank you")
        window.destroy()
    

window = Tk()
def login():
    username=entry1.get()
    password=entry2.get()

    if (username=="" and password==""):
        messagebox.showinfo("","Please fill the username")
    elif (username=="ADMIN" and password=="lit@india"):
        window.destroy()
        background = "#070033"
        def new():
            win.destroy()
            background = "#154360"

            def remove():
                messagebox.showinfo("","Thank You !!")
                win4.destroy()

            
            def register():
                curobj.execute(f"insert into student(Roll_no,Student_name,Academic_year,Department,Password) values('{n1.get()}','{n2.get()}','{year.get()}','{dept.get()}','{n3.get()}');")
                conn.commit()

            def reset():
                n1.delete(0,END)
                n2.delete(0,END)
                n3.delete(0,END)

            def student():
                win2.destroy()
                background = "#154360"

                '''def remove():
                    c1.delete(0,END)
                    c2.delete(0,END)
                    c3.delete(0,END)
                    c4.delete(0,END)
                    c5.delete(0,END)
                    c6.delete(0,END)
                    c7.delete(0,END)'''

                def login1():
                    roll = b1.get()
                    password = b2.get()

                    query = "select * from student where Roll_no=%s and Password=%s"
                    curobj.execute(query,[(roll),(password)])
                    result = curobj.fetchall()

                    if result:
                        messagebox.showinfo("","Login Successful !!")
                        win3.destroy()
                        background = "#154360"

                        def update():
                            roll = c1.get()
                            parent = c2.get()
                            email =  c3.get()
                            branch = dept.get()
                            dob = c4.get()
                            name = c5.get()
                            number = c6.get()
                            sex = gender.get()
                            academic = year.get()
                            security = c7.get()

                            q1 = "select * from student where Roll_no=%s and Password=%s"
                            curobj.execute(q1,[(roll),(password)])
                            res = curobj.fetchall()

                            if res:
                                update = "update student set Parent_name=%s,Email=%s,DOB=%s,Contact_no=%s,Gender=%s where Roll_no=%s"
                                vals = (parent,email,dob,number,sex,roll)
                                curobj.execute(update,vals)
                                messagebox.showinfo("","Successfully Updated")
                                conn.commit()
                            
                            else:
                                messagebox.showinfo("","Student does not exist")
                            
                            
                        
                        win4 = Tk()
                        win4.title("Student Management System")
                        win4.geometry('1180x700')
                        win4.resizable(False,False)
                        win4.config(bg = background)
                            
                        Label (win4, text = "STUDENT HOME PAGE", font = ('Elephant',15), width= "50", height ="1", fg="Red", relief = "raised").place(x=265, y=100)

                        
                        a1=Label (win4, text = "Roll number", font=('Elephant',13),width= "15",height="1", fg ="Black", relief = "raised").place(x=100, y=200)
                        a2=Label (win4, text = "Parent Name", font=('Elephant',13),width= "15",height="1", fg ="Black", relief = "raised").place(x=100, y=260)
                        a3=Label (win4, text = "Email", font=('Elephant',13),width= "15",height="1", fg ="Black", relief = "raised").place(x=100, y=320)
                        a4=Label (win4, text = "Department", font=('Elephant',13),width= "15",height="1", fg ="Black", relief = "raised").place(x=100, y=380)
                        a5=Label (win4, text = "DOB", font=('Elephant',13),width= "15",height="1", fg ="Black", relief = "raised").place(x=100, y=440)
                        a6=Label (win4, text = "Student Name", font=('Elephant',13),width= "15",height="1", fg ="Black", relief = "raised").place(x=628, y=200)
                        a7=Label (win4, text = "Cont. Number", font=('Elephant',13),width= "15",height="1", fg ="Black", relief = "raised").place(x=628, y=260)
                        a4=Label (win4, text = "Gender", font=('Elephant',13),width= "15",height="1", fg ="Black", relief = "raised").place(x=628, y=320)
                        a4=Label (win4, text = "Academic Year", font=('Elephant',13),width= "15",height="1", fg ="Black", relief = "raised").place(x=628, y=380)
                        a8=Label (win4, text = "Password", font=('Elephant',13),width= "15",height="1", fg ="Black", relief = "raised").place(x=628, y=440)

                        c1=Entry(win4,font = ('Elephant',15), bg = "silver",fg = "black", width = 15)
                        c1.place(x = 320, y = 199)
                        c2=Entry(win4,font = ('Elephant',15), bg = "silver",fg = "black", width = 15)
                        c2.place(x = 320, y = 259)
                        c3=Entry(win4,font = ('Elephant',15), bg = "silver",fg = "black", width = 15)
                        c3.place(x = 320, y = 319)
                        c4=Entry(win4,font = ('Elephant',15), bg = "silver",fg = "black", width = 15)
                        c4.place(x = 320, y = 439)
                        c5=Entry(win4,font = ('Elephant',15), bg = "silver",fg = "black", width = 15)
                        c5.place(x = 855, y = 199)
                        c6=Entry(win4,font = ('Elephant',15), bg = "silver",fg = "black", width = 15)
                        c6.place(x = 855, y = 259)
                        c7=Entry(win4,font = ('Elephant',15), bg = "silver",fg = "black", width = 15)
                        c7.place(x = 855, y = 439)
                

                        gender = StringVar()
                        g1 = Radiobutton(win4, text="Male",variable=gender,value = "Male",font = "time 15").place(x=855,y=320)
                        g2 = Radiobutton(win4, text="Female",variable=gender,value = "Female",font = "time 15").place(x=955,y=320)
                        

                        
                       
                        # for Academic year
                        list = ['21-23','22-25','23-26']
                        year = StringVar()
                        droplist = OptionMenu(win4,year,*list)
                        year.set('Select academic year')
                        droplist.config(width=30)
                        droplist.place(x =855 , y = 378)

                        # for Department
                        list = ['Bsc.ITM','BSC.CS','BCA','Data Science']
                        dept =StringVar()
                        droplist = OptionMenu(win4,dept,*list)
                        dept.set('Select department')
                        droplist.config(width=30)
                        droplist.place(x = 320, y = 380)


                        Button(win4,text = "Update", font = ('arial',15), relief = "raised",fg="Black", width="10", command = update).place(x= 250,y=540)
                        Button(win4,text = "Reset", font = ('arial',15), relief = "raised",fg="Black", width="10", command = remove).place(x= 500,y=540)
                        Button(win4,text = "Exit", font = ('arial', 15),relief = "raised", fg = "Black", width = "10",command = remove).place(x= 750, y= 540)

                        
                        win4.mainloop
                    else:
                        messagebox.showinfo("Error","Invalid Roll_no and Password !!")
                    

                def clear():
                    b1.delete(0,END)
                    b2.delete(0,END)
                    

                
                win3 = Tk()
                win3.title("Student Management System")
                win3.geometry('1080x700')
                win3.resizable(False,False)
                win3.config(bg = background)

                # Body making:-

                # for heading
                Label (win3, text = "STUDENT LOGIN", font = ('Elephant',15), width= "50", height ="1", fg="Red", relief = "raised").place(x=165, y=100)

                a1=Label (win3, text = "Student Roll number", font=('Elephant',13),width= "26",height="1", fg ="Black", relief = "raised").place(x=150, y=200)
                a2=Label (win3, text = "Academic Year", font=('Elephant',13),width= "26",height="1", fg ="Black", relief = "raised").place(x=150, y=260)
                a3=Label (win3, text = "Password", font=('Elephant',13),width= "26",height="1", fg ="Black", relief = "raised").place(x=150, y=320)

                b1=Entry(win3,font = ('Elephant',15), bg = "silver",fg = "black", width = 25)
                b1.place(x = 520, y = 199)
                b2 = Entry(win3, font = ('Elephant',15), bg = "silver",fg = "black", width = 25 )
                b2.place(x = 520, y = 319)
            
                # for Academic year
                list = ['21-23','22-25','23-26']
                year = StringVar()
                droplist = OptionMenu(win3,year,*list)
                year.set('Select academic year')
                droplist.config(width=56)
                droplist.place(x = 520, y = 259)

                
                Button(win3,text = "Login", font = ('arial',15), relief = "raised",fg="Black", width="10",command = login1).place(x= 180,y=440)
                Button(win3,text = "Reset", font = ('arial',15), relief = "raised",fg="Black", width="10",command = clear).place(x= 475,y=440)
                Button(win3,text = "Exit", font = ('arial', 15),relief = "raised", fg = "Black", width = "10",command = exxit).place(x= 750, y= 440)
                

                
                
                win3.mainloop()
                
        
            win2 = Tk()
            win2.title("Student Management System")
            win2.geometry('1080x700')
            win2.resizable(False,False)
            win2.config(bg = background)

            # trying to add data in database

            Label (win2, text = "Add New Student", font = ('Elephant',15), width= "50", height ="1", fg="Red", relief = "raised").place(x=165, y=100)
            
            l1=Label (win2, text = "Student Roll number", font=('Elephant',13),width= "26",height="1", fg ="Black", relief = "raised").place(x=150, y=200)
            l2=Label (win2, text = "Student Name", font=('Elephant',13),width= "26",height="1", fg ="Black", relief = "raised").place(x=150, y=260)
            l3=Label (win2, text = "Academic Year", font=('Elephant',13),width= "26",height="1", fg ="Black", relief = "raised").place(x=150, y=320)
            l4=Label (win2, text = "Department Name", font=('Elephant',13),width= "26",height="1", fg ="Black", relief = "raised").place(x=150, y=380)
            l5=Label (win2, text = "Password", font=('Elephant',13),width= "26",height="1", fg ="Black", relief = "raised").place(x=150, y=440)

    
            n1=Entry(win2,font = ('Elephant',15), bg = "silver",fg = "black", width = 25)
            n1.place(x = 520, y = 199)
            n2= Entry(win2, font = ('Elephant',15), bg = "silver",fg = "black", width = 25 )
            n2.place(x = 520, y = 259)
            n3 = Entry(win2, font = ('Elephant',15), bg = "silver",fg = "black", width = 25 )
            n3.place(x = 520, y = 439)
            #n3 = Entry(win2, font = ('Elephant',15),bg = "silver",fg = "black", width= 25)
            #n3.place(x = 520, y = 319)
            
            # for Academic year
            list = ['21-23','22-25','23-26']
            year = StringVar()
            droplist = OptionMenu(win2,year,*list)
            year.set('Select academic year')
            droplist.config(width=56)
            droplist.place(x = 520, y = 319)
            

            # for Department
            list = ['Bsc.ITM','BSC.CS','BCA','Data Science']
            dept =StringVar()
            droplist = OptionMenu(win2,dept,*list)
            dept.set('Select department')
            droplist.config(width=56)
            droplist.place(x = 520, y = 380)

            
            Button(win2,text = "Add Student", font = ('arial',15), relief = "raised",fg="Black", width="15",command = register).place(x= 180,y=540)
            Button(win2,text = "Reset", font = ('arial',15), relief = "raised",fg="Black", width="10",command = reset).place(x= 475,y=540)
            Button(win2,text = "Student Login", font = ('arial', 15),relief = "raised", fg = "Black", width = "15",command = student).place(x= 750, y= 540)

            win2.mainloop()

        def Exitt():
            messagebox.showinfo("","Thank You !!")
            win.destroy()
        
        def save():
             q1 = "select Roll_no, Student_name,Parent_name,Contact_no,Email,Gender,Academic_year,Department,Password from student;"
             curobj.execute(q1)
             data = curobj.fetchall()

             roll = []
             name = []
             parent = []
             phone = []
             email = []
             gender = []
             year = []
             dept = []
             password = []
             for Roll_no,Student_name,Parent_name,Contact_no,Email,Gender,Academic_year,Department,Password in data:
                 roll.append(Roll_no)
                 name.append(Student_name)
                 parent.append(Parent_name)
                 phone.append(Contact_no)
                 email.append(Email)
                 gender.append(Gender)
                 year.append(Academic_year)
                 dept.append(Department)
                 password.append(Password)

              # For store this all data to CSV
             dic = {'Roll_no': roll,'Student_name':name,'Academic_year':year,'Department':dept,'Password':password}
             df = pd.DataFrame(dic)
             df_csv = df.to_csv('D:/Student/Student_management.csv')
             messagebox.showinfo("","CSV file downloaded !!")


        

        win = Tk()
        win.title("Student Management System")
        win.geometry('1280x700')
        win.resizable(False,False)
        win.config(bg = background)

        #background image
        frame =Frame(win,bg="red")
        frame.pack(fill=Y)


        image = Image.open(r"C:\Users\Rudra PC\PycharmProjects\Student management system\student\bgg.jpg")
        photo = ImageTk.PhotoImage(image)

        lbl = Label(win,image = photo)
        lbl.pack(pady=200,padx=100)

        # Body 
        
        Button(win,text = "Add New Student", font = ('arial',15), relief = "raised",fg="Red", width="20", command = new).place(x= 520,y=250)
        Button(win,text = "Download Student details", font = ('arial',15), relief = "raised",fg="Red", width="20", command = save).place(x= 520,y=320)
        Button(win, text = "Exit",command=Exitt, height=2, width = 7 , bd =3).place(x= 600, y= 426)

        win.mainloop()
        #messagebox.showinfo("","login successful")
    else:
        messagebox.showinfo("","Invalid Username and password")

window.title ("Student Management System")
window.geometry("1280x700")
window.config(bg = background)
window.resizable(False,False)


#background image
frame =Frame(window,bg="red")
frame.pack(fill=Y)


image = Image.open(r"C:\Users\Rudra PC\Desktop\student management\bg.jpg")
photo = ImageTk.PhotoImage(image)

lbl = Label(window,image = photo)
lbl.pack(pady=200,padx=100)

# user entry

global entry1
global entry2

entry1 = Entry(window,bd=5)
entry1.place(x = 520, y = 310)

entry2= Entry(window,bd=5)
entry2.place(x = 520, y = 364)

Button(window,text="Login", command=login,height=2, width=7,bd = 3).place(x=480,y=426)
Button(window, text = "Exit",command=Exit, height=2, width = 7 , bd =3).place(x= 620, y= 426)


window.mainloop()
