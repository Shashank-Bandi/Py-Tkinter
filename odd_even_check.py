from tkinter import *

window = Tk()
e1_value=StringVar()
def check_even():
    t1.delete('1.0',END)
    if int(e1_value.get())%2==0:
        
        t1.insert(END,'Even')
    else:
                t1.insert(END,'Odd')


b1=Button(window,text='Check',command=check_even)
b1.grid(row=0,column=3)
t1=Text(window,height=1,width=20)
t1.grid(row=0,column=4)
l1=Label(window,text='Enter Number:')
l1.grid(row=0,column=1)
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=2)



window.mainloop()

