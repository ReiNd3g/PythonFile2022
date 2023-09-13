from tkinter import *
import customtkinter as ctk

screen = ctk.CTk()
screen.geometry("280x240")
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
screen.title("LOGIN SYSTEM")

def change_appearance_mode(new_appearance_mode):
        ctk.set_appearance_mode(new_appearance_mode)
        
ctk.CTkOptionMenu(master=screen, values=["Light", "Dark", "System"],command=change_appearance_mode).pack(pady=3)

ctk.CTkLabel(master=screen, text="LOGIN TO YOUR ACCOUNT", text_font= ("Avalon", 13, "bold")).pack(pady=5)

def login():
    global screen2
    screen2 = ctk.CTkToplevel(screen)
    screen2.title("Login")
    screen2.geometry("400x250")
    
    ctk.CTkLabel(master=screen2, text="Enter the Username and Password to Login", text_font=("Calibri", 12, 'bold')).pack()

    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    global username_entry1
    global password_entry1

    ctk.CTkLabel(master=screen2, text="Username", text_font=("Avalon", 10,'bold')).pack()
    username_entry1 = ctk.CTkEntry(screen2, textvariable=username_verify)
    username_entry1.pack(pady=10)
    
    ctk.CTkLabel(master=screen2, text="Password", text_font=("Avalon", 10, "bold")).pack()
    password_entry1 = ctk.CTkEntry(screen2, textvariable=password_verify)
    password_entry1.pack(pady=11)
    
    ctk.CTkButton(master=screen2, text="Login", text_font=("Calibri", 10, "bold"),command=login_verify).pack(pady=12)

def delete() :
    screen.destroy()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    while True:
        
        if username1 == "Izaac" and password1 == "iZ3kiu!":
            delete()
            break
        
        else :
            user_not_found()
            break
    
def user_not_found():
    global screen2
    screen2 = ctk.CTkToplevel(screen)
    screen2.title("Invalid Username")
    screen2.geometry("250x100")
    ctk.CTkLabel(master=screen2, text="User doesn't exist!", text_font=("Calibri",12,"bold")).pack(pady=5)
    ctk.CTkButton(master=screen2, text="OK", command=delete).pack(pady=6)
    
def Exit() :
    screen.destroy()

ctk.CTkButton(master=screen, text="Login", text_font=("Calibri", 12, "bold"),command=login).pack(pady=10)
ctk.CTkLabel(master=screen, text="Or", text_font=("Avalon", 12,"bold")).pack(pady=10.25)
ctk.CTkButton(master=screen, text="Exit", text_font=("Calibri", 12, 'bold'), command=Exit).pack(pady=11)
        
screen.mainloop()