from tkinter import*
win = Tk()

def onclick(event):
    text=event.widget.cget('text')
    print(text)

    if text == '=':
        store_Actual_value = val_Entery.get()
        store_New_variable = round(eval(store_Actual_value))
        value = v.set(store_New_variable)
        val_Entery.update()

    elif text == '%':
        percentage = float(val_Entery.get()) / 100
        v.set(percentage)
        val_Entery.update()    

    else:        
        store_Actual_value = val_Entery.get()
        value = v.set(store_Actual_value+text)
        val_Entery.update()
            
def clear_display(check):
    check_value = check.widget.cget('text')
    print(check_value)
    
    if check_value == 'CE' or check_value == 'C':
        check_value = v.set("")

def last_value_Delete(update_value) :
    actual_value = update_value.widget.cget('text')
    print(actual_value)
    
    if (actual_value == 'x') :
        actual_value = val_Entery.get()[:-1]
        v.set(actual_value)
        val_Entery.update()

def get_operator(op) :
    a = op.widget.cget('text')
    print(a)

    # if (a[0] == op) :
    #     if (a[0 + 1] == op ) :
    #         a = val_Entery.get()
    #         sign = v.set('')
    #         val_Entery.update()            

    if a[0 + 1] == op :
        a = op.get()
        a[0] = v.set+a('')
        val_Entery.update(a)
        
# Define size
win.geometry('200x200')
win.minsize(250,350)
win.maxsize(250,350)

# Define label
label = Label(text='CalcMaster')
label.place(x=10,y=20)

# Define Box-size.
v=StringVar()
val_Entery = Entry(textvariable=v)
val_Entery.place(x=60,y=50)

#CReate Buttons.
btn = Button(text = 'MC')
btn.place(x=10,y=80)

btn = Button(text = 'MR')
btn.place(x=50,y=80)

btn = Button(text = 'M+')
btn.place(x=90,y=80)

btn = Button(text = 'M-')
btn.place(x=130,y=80)

btn = Button(text = 'Ms')
btn.place(x=170,y=80)

btn = Button(text = 'M^')
btn.place(x=210,y=80)

# Create a button with text '%'
sign_percent = Button(text='%')
sign_percent.place(x=10, y=120, width=50.5)
sign_percent.bind('<Button-1>',onclick)

# Create a button with text 'CE'
sign_ce = Button(text='CE')
sign_ce.place(x=70.5, y=120, width=50.5)
sign_ce.bind('<Button-1>',clear_display)

# Create a button with text 'C'
sign_c = Button(text='C')
sign_c.place(x=130.5, y=120, width=50.5)
sign_c.bind('<Button-1>',clear_display)

# Create a button with text 'x'
sign_AFter_one_val_del = Button(text='x')
sign_AFter_one_val_del.place(x=190.5, y=120, width=50.5)
sign_AFter_one_val_del.bind('<Button-1>',last_value_Delete)

sign = Button(text='1/x')
sign.place(x=10,y=160,width=50.5)

sign = Button(text='x2')
sign.place(x=70.5,y=160,width=50.5)

sign = Button(text='x√2')
sign.place(x=130.5,y=160,width=50.5)

sign_divi = Button(text='/') 
sign_divi.place(x=190.5, y=160, width=50.5)
sign_divi.bind('<Button-1>', onclick,get_operator)

sign_Num = Button(text='7')  # Button-1 Name CReate varible
sign_Num.place(x=10,y=200,width=50.5)
sign_Num.bind('<Button-1>',onclick)

sign_Num = Button(text='8')
sign_Num.place(x=70.5,y=200,width=50.5)
sign_Num.bind('<Button-1>',onclick)

sign_Num = Button(text='9')
sign_Num.place(x=130.5,y=200,width=50.5)
sign_Num.bind('<Button-1>',onclick)

sign_multiply = Button(text='*')
sign_multiply.place(x=190.5, y=200, width=50.5)
sign_multiply.bind('<Button-1>', onclick,get_operator)

sign_Num = Button(text='4')
sign_Num.place(x=10,y=240,width=50.5)
sign_Num.bind('<Button-1>',onclick)

sign_Num = Button(text='5')
sign_Num.place(x=70.5,y=240,width=50.5)
sign_Num.bind('<Button-1>',onclick)

sign_Num = Button(text='6')
sign_Num.place(x=130.5,y=240,width=50.5)
sign_Num.bind('<Button-1>',onclick)

sign_sub = Button(text='-') 
sign_sub.place(x=190.5, y=240, width=50.5)
sign_sub.bind('<Button-1>', onclick,get_operator)

sign_Num = Button(text='1')
sign_Num.place(x=10,y=280,width=50.5)
sign_Num.bind('<Button-1>',onclick)

sign_Num = Button(text='2')
sign_Num.place(x=70.5,y=280,width=50.5)
sign_Num.bind('<Button-1>',onclick)

sign_Num = Button(text='3')
sign_Num.place(x=130.5,y=280,width=50.5)
sign_Num.bind('<Button-1>',onclick)

sign_add = Button(text='+')
sign_add.place(x=190.5,y=280,width=50.5)
sign_add.bind('<Button-1>',onclick,get_operator)

sign14 = Button(text='+/-')
sign14.place(x=10,y=320,width=50.5)
sign.bind('<Button-1>',onclick)

sign_Num = Button(text='0')
sign_Num.place(x=70.5,y=320,width=50.5)
sign_Num.bind('<Button-1>',onclick)

sign16 = Button(text='.')
sign16.place(x=130.5,y=320,width=50.5)
sign16.bind('<Button>',onclick)

sign17 = Button(text='=')
sign17.place(x=190.5,y=320,width=50.5)
sign17.bind('<Button-1>',onclick)

mainloop()  