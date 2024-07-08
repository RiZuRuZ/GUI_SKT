from tkinter import *
root = Tk()
root.title('Calculator eiei')

#main cal
content=''
txt=StringVar(value='0')

def clear():
    global content
    result="0"
    content =""
    txt.set(result)
  
def btn(number):
    global content
    content=content+str(number)
    txt.set(content)

def equal():
    global content
    cal=str(eval(content))
    txt.set(cal)
    content=''

#bar calculator
display=Entry(font=('arial',30,'bold'),fg="white",bg="gray",textvariable=txt)
display.grid(columnspan=4)
txt.set(0)

#รับค่า
#row1
num7=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='7',command=lambda:btn(7)).grid(row='1',column='0')
num8=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='8',command=lambda:btn(8)).grid(row='1',column='1')
num9=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='9',command=lambda:btn(9)).grid(row='1',column='2')
bc=Button(fg="black",font=('arial',30,'bold'),bg="red",padx="30",pady="15",text='c',command=clear).grid(row='1',column='3')

#row2
num4=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='4',command=lambda:btn(4)).grid(row='2',column='0')
num5=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='5',command=lambda:btn(5)).grid(row='2',column='1')
num6=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='6',command=lambda:btn(6)).grid(row='2',column='2')
bplus=Button(fg="black",font=('arial',30,'bold'),bg="yellow",padx="30",pady="15",text='+',command=lambda:btn('+')).grid(row='2',column='3')


#row3
num1=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='1',command=lambda:btn(1)).grid(row='3',column='0')
num2=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='2',command=lambda:btn(2)).grid(row='3',column='1')
num3=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='3',command=lambda:btn(3)).grid(row='3',column='2')
bminus=Button(fg="black",font=('arial',30,'bold'),bg="yellow",padx="35",pady="15",text='-',command=lambda:btn('-')).grid(row='3',column='3')

#row4
bdot=Button(fg="black",font=('arial',30,'bold'),bg="green",padx="35",pady="15",text='.',command=lambda:btn('.')).grid(row='4',column='0')
num0=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='0',command=lambda:btn(0)).grid(row='4',column='1')
btime=Button(fg="black",font=('arial',30,'bold'),bg="lightgreen",padx="30",pady="15",text='x',command=lambda:btn('*')).grid(row='4',column='2')
bdivide=Button(fg="black",font=('arial',30,'bold'),bg="yellow",padx="35",pady="15",text='/',command=lambda:btn('/')).grid(row='4',column='3')

#row5
beq=Button(fg="black",font=('arial',30,'bold'),bg="blue",padx="88",pady="15",text='=',command=equal).grid(row='5',columnspan=2)
bF=Button(fg="black",font=('arial',30,'bold'),bg="yellow",padx="35",pady="15",text='(',command=lambda:btn('(')).grid(row='5',column='2')
bL=Button(fg="black",font=('arial',30,'bold'),bg="yellow",padx="35",pady="15",text=')',command=lambda:btn(')')).grid(row='5',column='3')
root.mainloop()
