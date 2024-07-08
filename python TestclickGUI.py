from tkinter import *
root = Tk()
root.title('Click Test eiei')

#setting
#def
def counting():
    global count
    count += 1
    count_var.set(count)

def reset():
    global count
    count=0
    count_var.set(count)

count=0
#show
count_var = StringVar()
score_show = Entry(root, font=('arial',30,'bold'), fg="white", bg="gray", textvariable=count_var)
score_show.pack()
count_var.set(count)
#button
clickthis=Button(root,font=('arial',30,'bold'),fg="white",bg="#26D387",text='Click Here',padx=60,pady=20,command=counting).pack()
clearthis=Button(root,font=('arial',30,'bold'),fg="white",bg="#E96350",text='Reset',padx=105,command=reset).pack()
#geometry
root.geometry('350x250')

root.mainloop()
