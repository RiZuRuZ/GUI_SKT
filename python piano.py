import winsound
import tkinter as tk
import time
x=500

c4=261.63
d4=293.66
e4=329.63
f4=349.23
g4=392.00
a4=440.00
b4=493.88
c5=523.25
def play_c4():
    winsound.Beep(int(c4), x)
def play_d4():
    winsound.Beep(int(d4), x)
def play_e4():
    winsound.Beep(int(e4), x)
def play_f4():
    winsound.Beep(int(f4), x)
def play_g4():
    winsound.Beep(int(g4), x)
def play_a4():
    winsound.Beep(int(a4), x)
def play_b4():
    winsound.Beep(int(b4), x)
def play_c5():
    winsound.Beep(int(c5), x)



def song1():
    winsound.Beep(int(e4), x)
    winsound.Beep(int(d4), x)
    winsound.Beep(int(c4), x)
    winsound.Beep(int(d4), x)
    winsound.Beep(int(e4), x)
    winsound.Beep(int(e4), x)
    winsound.Beep(int(e4), x)
    time.sleep(0.5)
    winsound.Beep(int(d4), x)
    winsound.Beep(int(d4), x)
    winsound.Beep(int(d4), x)
    time.sleep(0.5)
    winsound.Beep(int(e4), x)
    winsound.Beep(int(g4), x)
    winsound.Beep(int(g4), x)
    time.sleep(0.5)
    winsound.Beep(int(e4), x)
    winsound.Beep(int(d4), x)
    winsound.Beep(int(c4), x)
    winsound.Beep(int(d4), x)
    winsound.Beep(int(e4), x)
    winsound.Beep(int(e4), x)
    winsound.Beep(int(e4), x)
    winsound.Beep(int(e4), x)
    winsound.Beep(int(d4), x)
    winsound.Beep(int(d4), x)
    winsound.Beep(int(e4), x)
    winsound.Beep(int(d4), x)
    winsound.Beep(int(c4), x)
        
    def song2():
      winsound.Beep(int(f4), x)
      winsound.Beep(int(f4), x)
      winsound.Beep(int(f4), x)
      winsound.Beep(int(c4), x)
      winsound.Beep(int(d4), x)
      winsound.Beep(int(d4), x)
      winsound.Beep(int(c4), x)
      time.sleep(0.5)
      winsound.Beep(int(a4), x)
      winsound.Beep(int(a4), x)
      winsound.Beep(int(g4), x)
      winsound.Beep(int(g4), x)
      winsound.Beep(int(f4), x)
    
    
    def song3():
      winsound.Beep(int(c4), x)
      winsound.Beep(int(c4), x)
      winsound.Beep(int(d4), x)
      time.sleep(0.2)
      winsound.Beep(int(c4), x)
      winsound.Beep(int(f4), x)
      winsound.Beep(int(e4), x)
      time.sleep(0.5)
      winsound.Beep(int(c4), x)
      winsound.Beep(int(c4), x)
      winsound.Beep(int(d4), x)
      time.sleep(0.2)
      winsound.Beep(int(c4), x)
      winsound.Beep(int(g4), x)
      winsound.Beep(int(f4), x)
      time.sleep(0.5)
      winsound.Beep(int(c4), x)
      winsound.Beep(int(c4), x)
      winsound.Beep(int(c5), x)
      winsound.Beep(int(a4), x)
      winsound.Beep(int(f4), x)
      winsound.Beep(int(e4), x)
      winsound.Beep(int(d4), x)
      time.sleep(0.5)
      winsound.Beep(int(c5), x)
      winsound.Beep(int(c5), x)
      winsound.Beep(int(a4), x)
      winsound.Beep(int(f4), x)
      winsound.Beep(int(g4), x)
      winsound.Beep(int(f4), x)
root = tk.Tk()
tk.Label(text='Piano Beep Sound in python',font='40').grid(row=0,columnspan=8)

c = tk.Button(root, text="โด", command=play_c4,height=10,width=5,font=60,relief='solid',bg='orange')
c.grid(row=1,column=0)
d = tk.Button(root, text="เร", command=play_d4,height=10,width=5,font=60,relief='solid',bg='orange')
d.grid(row=1,column=1)
e = tk.Button(root, text="มี", command=play_e4,height=10,width=5,font=60,relief='solid',bg='orange')
e.grid(row=1,column=2)
f = tk.Button(root, text="ฟา", command=play_f4,height=10,width=5,font=60,relief='solid',bg='orange')
f.grid(row=1,column=3)
g = tk.Button(root, text="ซอล", command=play_g4,height=10,width=5,font=60,relief='solid',bg='orange')
g.grid(row=1,column=4)
a = tk.Button(root, text="ลา", command=play_a4,height=10,width=5,font=60,relief='solid',bg='orange')
a.grid(row=1,column=5)
b = tk.Button(root, text="ที", command=play_b4,height=10,width=5,font=60,relief='solid',bg='orange')
b.grid(row=1,column=6)
c2 = tk.Button(root, text="โด", command=play_c5,height=10,width=5,font=60,relief='solid',bg='orange')
c2.grid(row=1,column=7)

play = tk.Button(root, text="เพลงหนูมาลี", command=song1,height=2,width=30,font=60,relief='solid',bg='hotpink')
play.grid(row=2,columnspan=8)

play2 = tk.Button(root, text="E-I-E-I-O", command=song2,height=2,width=30,font=60,relief='solid',bg='hotpink')
play2.grid(row=3,columnspan=8)

play3 = tk.Button(root, text="HBD", command=song3,height=2,width=30,font=60,relief='solid',bg='hotpink')
play3.grid(row=4,columnspan=8)
root.mainloop()
           
