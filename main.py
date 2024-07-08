import tkinter as tk
from os import system
root = tk.Tk()
from tkinter import PhotoImage

def run_cal():
    system('python Calculater_GUI.py')

def RPS():
    system('python RPS_GUI.py')

def clicktest():
    system('python TestclickGUI.py')

def TicTacToe():
    system('python Tic-Tac-Toe.py')

def ตรวจคุณภาพชีวิต():
    system('python lifets.py')

def สูตรคูณ():
    system('python timesGUI.py')

def piano():
    system('python piano.py')

root.config(bg='light green')

#frame1
fm1=tk.Frame(bg='blue')
fm1.pack(side='left')
b1=tk.Button(fm1,text="calc",command=run_cal,height=3,width=20,font=60,relief='solid',bg='#bfff00')
b2=tk.Button(fm1,text="RPS",command=RPS,height=3,width=20,font=60,relief='solid',bg='#00ff80')
b3=tk.Button(fm1,text="clicktest",command=clicktest,height=3,width=20,font=60,relief='solid',bg='#bfff00')
b4=tk.Button(fm1,text="Tic-Tac-Toe",command=TicTacToe,height=3,width=20,font=60,relief='solid',bg='#00ff80')
b5=tk.Button(fm1,text="ตรวจคุณภาพชีวิต",command=ตรวจคุณภาพชีวิต,height=3,width=20,font=60,relief='solid',bg='#bfff00')
b6=tk.Button(fm1,text="สูตรคูณ",command=สูตรคูณ,height=3,width=20,font=60,relief='solid',bg='#00ff80')
b7=tk.Button(fm1,text="piano",command=piano,height=3,width=20,font=60,relief='solid',bg='#bfff00')

b1.pack(side='top')
b2.pack(side='top')
b3.pack(side='top')
b4.pack(side='top')
b5.pack(side='top')
b6.pack(side='top')
b7.pack(side='top')


#frame2
fm2=tk.Frame(bg='lightblue')
fm2.pack(side='right')
lb1=tk.Label(fm2,text=' จัดทำโดย >>> นาย ภูริ เตชตรีสุคนธ์ 4/11 13 ')
img = tk.PhotoImage(file='myself.png')
label = tk.Label(fm2, image=img)

lb1.pack(side='top')
label.pack(side='top')

root.mainloop()
