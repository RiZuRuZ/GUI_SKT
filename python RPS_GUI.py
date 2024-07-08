from tkinter import *
import random
import string
root = Tk()
root.title('Rock-Paper-Scissor')
list = ["rock", "paper", "scissors"]
countplay=0
countai=0
iii=StringVar(value='0')
jjj=StringVar(value='0')
roc=''
pap=''
sis=''
o=''
lb=''
l=StringVar()


def check(x,y):
    global countplay
    global countai
    global roc,pap,sis,o,lb,l
    you=Label(text=f'you choose {x}',height=2,width=50,font=60,relief='solid',bg='orange').grid(row=5,column=0)
    ai=Label(text=o,height=2,width=50,font=60,relief='solid',bg='orange').grid(row=5,column=1)
    if x == y:
        lb=Label(text=f"Both players selected {x}. It's a tie!").grid(row=3,columnspan=3,sticky='news')
        lb1=Label(text='',height=2,width=100).grid(row=2,column=0)
        lb2=Label(text="",height=2,width=100).grid(row=3,column=0)
        lb3=Label(text="",height=2,width=100).grid(row=4,column=0)
        lb4=Label(text="END",height=2,width=100).grid(row=3,columnspan=2,sticky='news')
    elif x == "rock":
        if y == "scissors":
            lb=Label(text="Rock smashes scissors! You win!").grid(row=3,columnspan=3,sticky='news')
            countplay+=1
            lb1=Label(text='',height=2,width=100).grid(row=2,column=0)
            lb2=Label(text="",height=2,width=100).grid(row=3,column=0)
            lb3=Label(text="",height=2,width=100).grid(row=4,column=0)
            lb4=Label(text="END",height=2,width=100).grid(row=3,columnspan=2,sticky='news')
        else:
            lb=Label(text="Paper covers rock! You lose.").grid(row=3,columnspan=3,sticky='news')
            countai+=1
            lb1=Label(text='',height=2,width=100).grid(row=2,column=0)
            lb2=Label(text="",height=2,width=100).grid(row=3,column=0)
            lb3=Label(text="",height=2,width=100).grid(row=4,column=0)
            lb4=Label(text="END",height=2,width=100).grid(row=3,columnspan=2,sticky='news')
     elif x == "paper":
         if y == "rock":
             lb=Label(text="Paper covers rock! You win!").grid(row=3,columnspan=3,sticky='news')
             countplay+=1
             lb1=Label(text='',height=2,width=100).grid(row=2,column=0)
             lb2=Label(text="",height=2,width=100).grid(row=3,column=0)
             lb3=Label(text="",height=2,width=100).grid(row=4,column=0)
             lb4=Label(text="END",height=2,width=100).grid(row=3,columnspan=2)
         else:
             lb=Label(text="Scissors cuts paper! You lose.").grid(row=3,columnspan=3,sticky='news')
             countai+=1
             lb1=Label(text='',height=2,width=100).grid(row=2,column=0)
             lb2=Label(text="",height=2,width=100).grid(row=3,column=0)
             lb3=Label(text="",height=2,width=100).grid(row=4,column=0)
             lb4=Label(text="END",height=2,width=100).grid(row=3,columnspan=2,sticky='news')
     elif x == "scissors":
         if y == "paper":
             lb=Label(text="Scissors cuts paper! You win!").grid(row=3,columnspan=3,sticky='news')
             countplay+=1
             lb1=Label(text='',height=2,width=100).grid(row=2,column=0)
             lb2=Label(text="",height=2,width=100).grid(row=3,column=0)
             lb3=Label(text="",height=2,width=100).grid(row=4,column=0)
             lb4=Label(text="END",height=2,width=100).grid(row=3,columnspan=2,sticky='news')
         else:
             lb=Label(text="Rock smashes scissors! You lose.").grid(row=3,columnspan=3,sticky='news')
             countai+=1
             lb1=Label(text='',height=2,width=100).grid(row=2,column=0)
             lb2=Label(text="",height=2,width=100).grid(row=3,column=0)
             lb3=Label(text="",height=2,width=100).grid(row=4,column=0)
             lb4=Label(text="END",height=2,width=100).grid(row=3,columnspan=2,sticky='news')
      iii.set(countplay)
      jjj.set(countai)
    
    gameshowtitle=Label(text='Rock-Paper-Scissors',height=2,width=100,font=60,relief='solid',bg='orange').grid(row=0,columnspan=3,sticky='news')
    a1=Label(text='PLAYER',height=2,width=50,font=60,relief='solid',bg='lightblue').grid(row=1,column=0)
    a2=Label(text='AI',height=2,width=50,font=60,relief='solid',bg='hotpink').grid(row=1,column=1)
    
    o=random.choice(list)
    roc=Button(text='rock',font='100',command=lambda:check('rock',o),bg='#4597d6').grid(row=2,column=0)
    pap=Button(text='paper',font='100',command=lambda:check('paper',o),bg='#45d6cf').grid(row=3,column=0)
    sis=Button(text='scissors',font='100',command=lambda:check('scissors',o),bg='#45d6a1').grid(row=4,column=0)
    
    sc1=Entry(font=('arial',30,'bold'),fg="white",bg="gray",textvariable=str(iii))
    sc1.grid(row=6,column=0)
    
    sc2=Entry(font=('arial',30,'bold'),fg="white",bg="gray",textvariable=str(jjj))
    sc2.grid(row=6,column=1)
    
    root.mainloop()

   
