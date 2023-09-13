from tkinter import *
import pygame.mixer as mixer
import customtkinter
from tkinter import filedialog
import os
import tkinter as tk
import tkinter.ttk as ttk

r = customtkinter.CTk()
r.title('Music Player Testing Window')
filepath = "D:/Downloads from Chrome/"
r.iconbitmap(filepath+"video-icon-8036-Windows.ico")
r.geometry("460x565")
r.resizable(False,False)
customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("blue")

mixer.init()

def play_song(song_name: customtkinter.StringVar, songs_list: customtkinter.CTkTextbox, status: customtkinter.StringVar):
    song_name.set(songs_list.get(ACTIVE))
    
    mixer.music.load(songs_list.get(ACTIVE))
    mixer.music.play()
    status.set("Song: Playing...")

def stop_song(status: customtkinter.StringVar):
    mixer.music.stop()
    status.set("Song: STOPPED")

def load(listbox):
    os.chdir(filedialog.askdirectory(title='Open songs directory'))
    tracks = os.listdir()

    for track in tracks:
        listbox.insert(END, track)

def pause_song(status: customtkinter.StringVar):
    mixer.music.pause()
    status.set("Song: PAUSED")

def resume_song(status: customtkinter.StringVar):
    mixer.music.unpause()
    status.set("Song: RESUMED")

def repeat_song() :
    mixer.music.rewind()
                    
current_song = customtkinter.StringVar(master=r, value='< Not Selected >')
song_status = customtkinter.StringVar(master=r, value='< Not Available >')

def change_appearance_mode(new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
    
k = customtkinter.CTkLabel(master=r, text="Izaac's Music Player", text_font=("Calibri", 15,"bold"))
k.grid(row=0, column=1)

customtkinter.CTkLabel(master=r,text="").grid(row=1,column=1) # Blank

def format_duration(ms):
    total_s = ms / 1000
    total_min = total_s / 60
    remain_s = total_s % 60
    return "%0d:%02d" % (total_min, remain_s)

def start(pb, music_file):
    
        pb.music = mixer.music.load(music_file)

        # Update the title
        pb.music_title.set(music_file)

        # Start playback
        mixer.music.play()

        # Start periodically updating the progress bar and progress label
        mixer.music.update_progress(pb)

def update_progress(self):
    pos_ms = self.music.current_position()
    total_ms = self.music.milliseconds()
    progress_percent = pos_ms / float(total_ms) * 100
    label_text = "%s / %s (%0.2f %%)" % (format_duration(pos_ms), format_duration(total_ms), progress_percent)
    pb.set(label_text)
    pb["value"] = progress_percent       
    self.after(100, self.update_progress)

pb = customtkinter.CTkProgressBar(master=r, orient=HORIZONTAL, mode="determinate", progress_color="brown")
pb.grid(row=2, column=1, sticky="ew")

customtkinter.CTkLabel(master=r, text="").grid(row=3, column= 1) # Blank

playlist = tk.Listbox(r, font=('Core Sans', 10,'bold'), selectbackground='brown', activestyle=DOTBOX, width=40, background="light grey", fg="black") # customtkinter.CTkTextbox(r, borderwidth=3, height=12, width=50, border_color="blue")
playlist.grid(row=4, column=1, sticky='nsew')

scroll_bar = customtkinter.CTkScrollbar(r, command=playlist.yview)
scroll_bar.grid(row=4, column=2, sticky='ns')

playlist.configure(yscrollcommand=scroll_bar.set)

customtkinter.CTkLabel(master=r,text="").grid(row=5,column=1) # Blank
    
b1 = customtkinter.CTkButton(master=r, text="Play", text_color="white", text_font=("Calibri", 15,"bold"), width=85, height=3, command=lambda: play_song(current_song, playlist, song_status))
b1.grid(row=6, column=1)

b2 = customtkinter.CTkButton(master=r, text="Stop", command=lambda: stop_song(song_status), text_color="white", text_font=("Calibri",15,"bold"), width=85, height=3)
b2.grid(row=8, column=0)

b3 = customtkinter.CTkButton(master=r, text="Pause", text_color="white", text_font=("Calibri", 15,"bold"),command=lambda: pause_song(song_status), width=85, height=3)
b3.grid(row=8, column=2)

customtkinter.CTkLabel(master=r, text="").grid(row=7, column= 1) # Blank

count = 0
def next_song() :
    global count
    song_list = []
    for file in os.listdir():
        if file.endswith('.mp3'):
            song_list.append(file)
    mixer.music.load(song_list[count])
    mixer.music.play()
    count += 1
    
customtkinter.CTkButton(master=r, text="Next", text_color="white", text_font=("Calibri", 15,"bold"), width=85, height=3, command=next_song).grid(row=6, column=2)

b4 = customtkinter.CTkButton(master=r, text="Resume", text_color="white", text_font=("Calibri", 15,"bold"),command=lambda: resume_song(song_status), width=88, height=3)
b4.grid(row=8, column=1)

customtkinter.CTkButton(master=r, text="Back", text_color="white", text_font=("Calibri", 14,"bold"), width=85, height=3).grid(row=6, column=0)

customtkinter.CTkOptionMenu(master=r, values=["Light", "Dark", "System"], command=change_appearance_mode, width=88).grid(row=0, column=2)

customtkinter.CTkLabel(master=r, text="").grid(row=9, column= 1) # Blank

def volchange(level) :
    
    if level < 1 :
        level = level + 0.10
        
        mixer.music.set_volume(level)
        
    else :
        pass
        print("High volume")
        
    if level > 0 :
        level = level - 0.10
        mixer.music.set_volume(level)
        
    else :
        pass

vol_slider = customtkinter.CTkSlider(master=r, from_=0, to=1, command=volchange, number_of_steps=18, button_length=20, button_color="brown").grid(row=10, column=1)

customtkinter.CTkLabel(master=r, text="").grid(row=11, column=1) # Blank

def random_playlist() :
    
    for file in os.listdir():
        if file.endswith('.mp3'):
            mixer.music.load(file)
            mixer.music.play()

customtkinter.CTkButton(master=r, text="Shuffle" , text_font=("Calirbri", 14, 'bold'), width=85, height=3, command=random_playlist).grid(row=12, column=0)
customtkinter.CTkButton(master=r, text='Load Playlist', text_font=("Calibri", 14,'bold'), width=50, height=3, command=lambda: load(playlist)).grid(row=12, column=1)
customtkinter.CTkButton(master=r, text="Repeat" , text_font=("Calirbri", 14, 'bold'), width=87, height=3,command=repeat_song).grid(row=12, column=2)

customtkinter.CTkLabel(master=r, text="").grid(row=13, column=1) # Blank
customtkinter.CTkLabel(master=r, textvariable=song_status, text_font=("Core Sans",10,'bold')).grid(row=14, column= 1)

r.mainloop()