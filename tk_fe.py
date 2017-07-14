from tkinter import *
import backend


def get_selected_row(event):
    global selected_tuple
    index=r_list.curselection()[0]
    selected_tuple=r_list.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0, END)
    e2.insert(END,selected_tuple[2])
    e3.delete(0, END)
    e3.insert(END,selected_tuple[3])
    e4.delete(0, END)
    e4.insert(END,selected_tuple[4])
    e5.delete(0, END)
    e5.insert(END,selected_tuple[5])
    e6.delete(0, END)
    e6.insert(END,selected_tuple[6])
    e7.delete(0, END)
    e7.insert(END,selected_tuple[7])



def view_command():
    r_list.delete(0,END)
    for row in backend.view():
        r_list.insert(END,row)

def search_command():
    r_list.delete(0,END)
    for row in backend.search(name_text.get(),date_text.get(),sex_text.get(),ster_text.get(),adopted_text.get(),
                              owner_text.get(),adress_text.get()):
        r_list.insert(END,row)

def add_command():
    backend.insert(name_text.get(),date_text.get(),sex_text.get(),ster_text.get(),adopted_text.get(),
                   owner_text.get(),adress_text.get())
    r_list.delete(0,END)
    r_list.insert(END,(name_text.get(),date_text.get(),sex_text.get(),ster_text.get(),
                       adopted_text.get(),owner_text.get(),adress_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])

def update_command():
    backend.update(selected_tuple[0],name_text.get(),date_text.get(),sex_text.get(),
                   ster_text.get(),adopted_text.get(),owner_text.get(),adress_text.get())


window=Tk()

window.wm_title("Rabbitry")

l1=Label(window,text="Name")
l1.grid(row=0,column=0)

l2=Label(window,text="Date of birth")
l2.grid(row=1,column=0)

l3=Label(window,text="Sex")
l3.grid(row=2,column=0)

l4=Label(window,text="Sterilisation")
l4.grid(row=3,column=0)

l5=Label(window,text="Adopted")
l5.grid(row=4,column=0)

l6=Label(window,text="Owner")
l6.grid(row=5,column=0)

l7=Label(window,text="Adress")
l7.grid(row=6,column=0)

name_text=StringVar()
e1=Entry(window,textvariable=name_text)
e1.grid(row=0,column=1)

date_text=StringVar()
e2=Entry(window,textvariable=date_text)
e2.grid(row=1,column=1)

sex_text=StringVar()
e3=Entry(window,textvariable=sex_text)
e3.grid(row=2,column=1)

ster_text=StringVar()
e4=Entry(window,textvariable=ster_text)
e4.grid(row=3,column=1)

adopted_text=StringVar()
e5=Entry(window,textvariable=adopted_text)
e5.grid(row=4,column=1)

owner_text=StringVar()
e6=Entry(window,textvariable=owner_text)
e6.grid(row=5,column=1)

adress_text=StringVar()
e7=Entry(window,textvariable=adress_text)
e7.grid(row=6,column=1)

r_list=Listbox(window,height=25, width=45)
r_list.grid(row=2,column=3,rowspan=8,columnspan=2)

scroll_bar=Scrollbar(window)
scroll_bar.grid(row=1,column=5,rowspan=8)

r_list.config(yscrollcommand=scroll_bar.set)
scroll_bar.configure(command=r_list.yview)

r_list.bind('<<ListboxSelect>>',get_selected_row)
b1=Button(window, text="View all",width=10,command=view_command)
b1.grid(row=0,column=3)

b2=Button(window, text="Search",width=10,command=search_command)
b2.grid(row=0,column=4)

b3=Button(window, text="Add",width=10,command=add_command)
b3.grid(row=1,column=3)

b4=Button(window, text="Update selected",width=10,command=update_command)
b4.grid(row=1,column=4)

b5=Button(window, text="Delete selected",width=10,command=delete_command)
b5.grid(row=10,column=3)

b6=Button(window, text="Close",width=10,command=window.destroy)
b6.grid(row=10,column=4)

window.mainloop()
