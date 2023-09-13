from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import tkinter.ttk as ttk

menu={0:['Chicken',2000],1:['Sushi',1500],2:['Takoyaki',1200],
3:['Cola',1000],4:['Juice',800],5:['Water',500],
6:['Pizza',6500]}
sb=[]

screen = Tk()
screen.title('Food-Ordering System')
screen.geometry("1000x500")

screen.columnconfigure(0,weight=8)
screen.columnconfigure(1,weight=2)
screen.rowconfigure(0, weight=1) 
screen.rowconfigure(1, weight=12)
screen.rowconfigure(2, weight=1)

top= tk.Frame(screen)
bottom= tk.Frame(screen)

right= tk.Frame(screen,bg='brown')
left= tk.Frame(screen,bg='brown')

top.grid(row=0,column=0,sticky='WENS',columnspan=2)
left.grid(row=1,column=0,sticky='WENS')
right.grid(row=1,column=1,sticky='WENS')
bottom.grid(row=2,column=0,sticky='WENS',columnspan=2)
trv = Treeview(right, selectmode ='browse')
trv.grid(row=0,column=0,columnspan=2,padx=3,pady=2)

trv["columns"] = ("1", "2","3")
trv.column("#0", width= 90, anchor ='w')
trv.column("1", width = 60, anchor ='w')
trv.column("2", width = 60, anchor ='c')
trv.column("3", width = 50, anchor ='c')
  
trv.heading("#0", text ="Items",anchor='w')
trv.heading("1", text ="Price",anchor='w')
trv.heading("2", text ="Quantity",anchor='c')
trv.heading("3", text ="Total",anchor='c')
def reset():
    for item in trv.get_children():
        trv.delete(item)
    #for i in range(len(sb)):
    #    sb[i].config(textvariable=0)    # reset spinbox 
    l1=[]
    for i in range(9):
        l1.append(IntVar(value=0))
    for i in range(len(sb)):
        print(sb[i].config(textvariable=l1[i]))

    for w in right.grid_slaves(1):
        w.grid_remove()
    for w in right.grid_slaves(2):
        w.grid_remove()    
    for w in right.grid_slaves(3):
        w.grid_remove()
    
def bill():
    total=0
    for item in trv.get_children():
        trv.delete(item)
    for i in range(len(sb)):
        if(int(sb[i].get())>0):
            price=int(sb[i].get())*menu[i][1]
            total=total+price
            my_str1=(str(menu[i][1]), str(sb[i].get()), str(price))
            trv.insert("",'end',iid=i,text=menu[i][0],values=my_str1)
    lr1= tk.Label(right,text='Total :', font=font1, bg= "brown", fg="yellow")
    lr1.grid(row=1,column=0,sticky='nw')
    
    tk.Label(right, bg= "brown").grid(row=2,column=0,sticky='nw') #Insert Blank
    
    lr2= tk.Label(right,text=str(total),font=font1, bg= "brown", fg="yellow")
    lr2.grid(row=1,column=1,sticky='nw')
    
    lr21= tk.Label(right,text='10% Tax :',font=font1, bg= "brown", fg="yellow")
    lr21.grid(row=3,column=0,sticky='nw')
    tax=0.01*total
    
    tk.Label(right, bg= "brown").grid(row=4,column=0,sticky='nw') #Insert Blank
    
    lr22= tk.Label(right,text=str(tax),font=font1, bg= "brown", fg="yellow")
    lr22.grid(row=3,column=1,sticky='nw')
    
    lr31= tk.Label(right,text='Total Bill:',font=font2, bg= "brown", fg="yellow")
    lr31.grid(row=5,column=0,sticky='nw')
    final=total+tax
    
    lr32= tk.Label(right,text=str(final),font=font2, bg= "brown", fg="yellow")
    lr32.grid(row=5,column=1,sticky='nw')

font1=('Calibri', 20,'bold')
font2=('noah-medium',20,'bold')
font3=('Avalon', 10,'bold')
pdx,pdy=40,5

v = StringVar(screen)
chkn= ["Lotteria", "MarryBrown", "Five Star", "CP"]
sushi= ["Nigiri", "Chirashi", "Tobiko", "Uramaki", "Tekkamaki", "Masago", "Maki"]
juice= ["Coca Cola", "Sprite", "Pepsi", "Avocado", "Melon", "Lemon", "Banana"]
pizza= ["Neapolitan", "Margherita", "Stuffed crust", "Hawaiian", "Cheese", "BBQ Chicken"]

def order() :
    
    menu1['text'] = 'Ordered'
    menu1['bg'] = 'black'
    menu1['fg'] = 'yellow'
    
def order1() :
    
    menu2['text'] = 'Ordered'
    menu2['bg'] = 'black'
    menu2['fg'] = 'yellow'
    
def order2() :
    
    menu3['text'] = 'Ordered'
    menu3['bg'] = 'black'
    menu3['fg'] = 'yellow'
    
def order3() :
    
    menu4['text'] = 'Ordered'
    menu4['bg'] = 'black'
    menu4['fg'] = 'yellow'
    
def order4() :
    
    menu5['text'] = 'Ordered'
    menu5['bg'] = 'black'
    menu5['fg'] = 'yellow'
    
def order5() :
    
    menu6['text'] = 'Ordered'
    menu6['bg'] = 'black'
    menu6['fg'] = 'yellow'

menu1= tk.Button(left,text='Fried Chicken', font=font3, command=order)
menu1.grid(row=1,column=1,sticky='nw',padx=pdx,pady=pdy)
menu2= tk.Button(left,text='Sushi', font=font3, command=order1)
menu2.grid(row=1,column=2,sticky='nw',padx=pdx,pady=pdy)
menu3= tk.Button(left,text='Takoyaki', font=font3, command=order2)
menu3.grid(row=1,column=3,sticky='nw',padx=pdx,pady=pdy)

sv1=IntVar()
sb1 = ttk.Spinbox(left,from_=0,to_=1000,font=font1,width=1,textvariable=sv1)
sb1.grid(row=2,column=1,sticky='nw',padx=pdx,pady=0)
sb.append(sb1)
Spinbox(screen, values = chkn, textvariable= v, width= 11, font= font2)

sv2=IntVar()
sb2 = Spinbox(left,from_=0,to_=1000,font=font1,width=1,textvariable=sv2)
sb2.grid(row=2,column=2,sticky='nw',padx=pdx,pady=0)
sb.append(sb2)
Spinbox(screen, values = sushi, textvariable= v, width= 11, font= font2)

sv3=IntVar()
sb3 = Spinbox(left,from_=0,to_=1000,font=font1,width=1,textvariable=sv3)
sb3.grid(row=2,column=3,sticky='nw',padx=pdx,pady=0)
sb.append(sb3)
Spinbox(screen, values = juice, textvariable= v, width= 11, font= font2)

menu4= tk.Button(left,text='Juice', font=font3, command=order3)
menu4.grid(row=3,column=1,sticky='nw',padx=pdx,pady=pdy)
menu5= tk.Button(left,text='Water', font=font3, command=order4)
menu5.grid(row=3,column=2,sticky='nw',padx=pdx,pady=pdy)
menu6= tk.Button(left,text='Pizza', font=font3, command=order5)
menu6.grid(row=3,column=3,sticky='nw',padx=pdx,pady=pdy)

sv4=IntVar()
sb4 = Spinbox(left,from_=0,to_=1000,font=font1,width=1,textvariable=sv4)
sb4.grid(row=4,column=1,sticky='nw',padx=pdx,pady=0)
sb.append(sb4)
Spinbox(screen, values = pizza, textvariable= v, width= 11, font= font2)

sv5=IntVar()
sb5 = Spinbox(left,from_=0,to_=1000,font=font1,width=1,textvariable=sv5)
sb5.grid(row=4,column=2,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb5)

sv6=IntVar()
sb6 = Spinbox(left,from_=0,to_=1000,font=font1,width=1,textvariable=sv6)
sb6.grid(row=4,column=3,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb6)

# Insert the Blanks
tk.Label(left, bg= "brown").grid(row=7, column=1)
tk.Label(left, bg= "brown").grid(row=7, column=3)
tk.Label(left, bg= "brown").grid(row=8, column=1)
tk.Label(left, bg= "brown").grid(row=8, column=3)

b1= tk.Button(left,text='Get Bill',command=bill, font=("noah-medium",12,'bold'), bg= "brown", fg="white")
b1.grid(row=2,column=5)
b2= tk.Button(left,text='Reset',command=reset, font=("noah-medium",12,'bold'), bg= "brown", fg="white")
b2.grid(row=5,column=5)

screen.mainloop()