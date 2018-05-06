from tkinter import *
#####Window Declaration############
window=Tk()
#####TextVariables#################
e_title_value=StringVar()

e_author_value=StringVar()

e_year_value=StringVar()

e_isbn_value=StringVar()
####Labels and Entry Fields########
l_title=Label(window,text="Title")
l_title.grid(row=1,column=0)
e_title=Entry(window,textvariable=e_title_value)
e_title.grid(row=1,column=1)


l_author=Label(window,text="Author")
l_author.grid(row=1,column=2)
e_author=Entry(window,textvariable=e_author_value)
e_author.grid(row=1,column=3)

l_year=Label(window,text="Year")
l_year.grid(row=2,column=0)
e_year=Entry(window,textvariable=e_year_value)
e_year.grid(row=2,column=1)
l_isbn=Label(window,text="ISBN")
l_isbn.grid(row=2,column=2)
e_isbn=Entry(window,textvariable=e_isbn_value)
e_isbn.grid(row=2,column=3)
#######ListBox####################
display=Listbox(window,height=6,width=35)
display.grid(row=4,column=0,rowspan=6,columnspan=2)
#######ScrollBar##################
sb1=Scrollbar(window)
sb1.grid(row=4,column=2,rowspan=6)

display.configure(yscrollcommand=sb1.set)
sb1.configure(command=display.yview)

#####Buttons Declarations#########

b_va=Button(window,text="View All",width=12)#,command=view_all)
b_va.grid(row=4,column=3)
b_se=Button(window,text="Search Entry",width=12)#,command=search_entry)
b_se.grid(row=5,column=3)
b_ae=Button(window,text="Add Entry",width=12)#,command=add_entry)
b_ae.grid(row=6,column=3)
b_u=Button(window,text="Update Selected",width=12)#,command=update)
b_u.grid(row=7,column=3)
b_d=Button(window,text="Delete Selected",width=12)#,command=delete)
b_d.grid(row=8,column=3)
b_c=Button(window,text="Close",width=12)#,command=close)
b_c.grid(row=9,column=3)










window.mainloop()
