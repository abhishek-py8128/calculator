from tkinter import*
win = Tk() # create object

win.geometry('200x200')
win.minsize(200,300)
win.maxsize(200,300)

a = Entry()
a.place(x=12,y=34)
label = Label(text='creative')
label.place(x=89,y=87)

v = Button(text='1')
v.place(x=45,y=56)
mainloop()

# def onclick(event):
#     text=event.widget.cget('text')
#     print(text)
#     a=val_Entery.get()
#     value=v.set(a+text)
#     val_Entery.update()

from tkinter import*
win = Tk()

def onclick(event):
        text=event.widget.cget('text')
        print(text)
        if text=='=':
                a=val_Entery.get()
                sum=eval(a)
                value=v.set(sum)
                val_Entery.update()
        else:        
                a=val_Entery.get()
                value=v.set(a+text)
                val_Entery.update()
        
# Define size
win.geometry('200x200')
win.minsize(250,310)
win.maxsize(250,310)

# Define label
label = Label(text='CalcMaster')
label.place(x=10,y=20)

# Define Box-size.
v=StringVar()
val_Entery = Entry(textvariable=v)
val_Entery.place(x=60,y=50)

sign = Button(text='÷')
sign.place(x=190.5,y=120,width=50.5)

sign1 = Button(text='7')  # Button-1 Name CReate varible
sign1.place(x=10,y=160,width=50.5)
sign1.bind('<Button-1>',onclick)

sign2 = Button(text='8')
sign2.place(x=70.5,y=160,width=50.5)
sign2.bind('<Button-1>',onclick)

sign3 = Button(text='9')
sign3.place(x=130.5,y=160,width=50.5)
sign3.bind('<Button-1>',onclick)

sign4 = Button(text='X')
sign4.place(x=190.5,y=160,width=50.5)
sign4.bind('<Button-1>',onclick)

sign5 = Button(text='4')
sign5.place(x=10,y=200,width=50.5)
sign5.bind('<Button-1>',onclick)

sign6 = Button(text='5')
sign6.place(x=70.5,y=200,width=50.5)
sign6.bind('<Button-1>',onclick)

sign7 = Button(text='6')
sign7.place(x=130.5,y=200,width=50.5)
sign7.bind('<Button-1>',onclick)

sign8 = Button(text='−')
sign8.place(x=190.5,y=200,width=50.5)
sign8.bind('<Button-1>',onclick)

sign9 = Button(text='1')
sign9.place(x=10,y=240,width=50.5)
sign9.bind('<Button-1>',onclick)

sign10 = Button(text='2')
sign10.place(x=70.5,y=240,width=50.5)
sign10.bind('<Button-1>',onclick)

sign11 = Button(text='3')
sign11.place(x=130.5,y=240,width=50.5)
sign11.bind('<Button-1>',onclick)

sign12 = Button(text='+')
sign12.place(x=10,y=280,width=50.5)
sign12.bind('<Button-1>',onclick)

sign14 = Button(text='0')
sign14.place(x=70.5,y=280,width=50.5)
sign14.bind('<Button-1>',onclick)

sign15 = Button(text='.')
sign15.place(x=130.5,y=280,width=50.5)
sign15.bind('<Button-1>',onclick)

sign13 = Button(text='=')
sign13.place(x=190.5,y=280,width=50.5)
sign13.bind('<Button-1>',onclick)

mainloop() 