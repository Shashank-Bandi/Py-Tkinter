from tkinter import *


window=Tk()
e1_value=StringVar()
def convert():
    t1.delete('1.0',END)
    t2.delete('1.0',END)
    t3.delete('1.0',END)
    grams=float(e1_value.get())*1000
    pounds=float(e1_value.get())*2.20462
    ounces=float(e1_value.get())*35.274
    t1.insert(END,grams)
    t2.insert(END,pounds)
    t3.insert(END,ounces)





l1=Label(window,text="Enter Kg:")
l1.grid(row=0,column=1,rowspan=2)
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=2,rowspan=2)
b1=Button(window,text="Convert",command=convert)
b1.grid(row=0,column=3,rowspan=2)
t1=Text(window,height=1,width=20)
t1.grid(row=2,column=1)
t2=Text(window,height=1,width=20)
t2.grid(row=2,column=2)
t3=Text(window,height=1,width=20)
t3.grid(row=2,column=3)






window.mainloop()
