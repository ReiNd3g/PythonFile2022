import mysql.connector

from tkinter import *
from tkinter import messagebox
#
def Login():
    mysql_db = mysql.connector.connect(host='localhost',user='root',password='root1234!',database='student')
    my_cursor= mysql_db.cursor()
    username = first.get()
    password = second.get()
    
    sql_query = 'select * from student_login where username = %s and password = %s'
    my_cursor.execute(sql_query,[(username),(password)])
    result = my_cursor.fetchall()
    
    if result:
        messagebox.showinfo('','Login Success')
        root.destroy()  
        
        return True
    else:
        messagebox.showinfo('','Incorrect Username and Password')
        return False
    
    
root =Tk()
root.title('Login')
root.geometry('300x200')

Label(root,text='Username').place(x=10,y =10)
Label(root,text='Password').place(x=10,y=40)

global first
global second

first = Entry(root)
second = Entry(root)

first.place(x = 140,y = 10)
second.place(x = 140,y = 40)
second.config(show='*')


Button(root,text='Login', command=Login, height= 3,width=13 ).place(x =10,y = 100)

root.mainloop


