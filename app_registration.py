from tkinter import *
app=Tk()

#Lets say we are creating an app which will take user registration data like Facebook,Instagram,Twitter etc.
#In order to do that,we have to include datas such as Name,username,password,email,mobile number etc.

#First we are adding the data which the user is going to input

#Full name adding
fullname_text=StringVar()
fullname_label=Label(app,text='Full name',font=('bold',15),padx=20,pady=20)
fullname_label.grid(row=0,column=0)
fullname_entry=Entry(app,textvariable=fullname_text)
fullname_entry.grid(row=0,column=1)

#username adding
username_text=StringVar()
username_label=Label(app,text='Username',font=('bold',15),padx=20,pady=20)
username_label.grid(row=1,column=0)
username_entry=Entry(app,textvariable=username_text)
username_entry.grid(row=1,column=1)

#email adding
email_text=StringVar()
email_label=Label(app,text='Email',font=('bold',15),padx=20,pady=20)
email_label.grid(row=2,column=0)
email_entry=Entry(app,textvariable=email_text)
email_entry.grid(row=2,column=1)

#password adding
password_text=StringVar()
password_label=Label(app,text='Password',font=('bold',15),padx=20,pady=20)
password_label.grid(row=3,column=0)
password_entry=Entry(app,textvariable=password_text)
password_entry.grid(row=3,column=1)

#Mobile number adding
mnumber_text=StringVar()
mnumber_label=Label(app,text='Mobile number',font=('bold',15),padx=20,pady=20)
mnumber_label.grid(row=4,column=0)
mnumber_entry=Entry(app,textvariable=mnumber_text)
mnumber_entry.grid(row=4,column=1)
#1st part ended here adding the data which user gives as input

#Now we are going to add 2 buttons.Register and login.
register_button=Button(app,text='Register now')
register_button.grid(row=5,column=1,pady=10)

login_button=Button(app,text='Login here')
login_button.grid(row=6,column=1,pady=10)

app.title("Registration app")
app.geometry('400x500')
app.mainloop()