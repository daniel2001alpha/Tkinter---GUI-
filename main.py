from tkinter import *
from tkinter import ttk
from db import Database
from tkinter import messagebox


db=Database()
root=Tk()
root.title("Employee Management System")
sysWidth=root.winfo_screenwidth()
sysHeight=root.winfo_screenheight()
root.geometry(f"%dx%d+%d+%d"%(sysWidth,sysHeight,0,0))
root.config(bg="#2c3e50")
root.state("zoomed")

name=StringVar()
age=IntVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()




#Enteries Frame

eFrame=Frame(root,bg="#535c68")
eFrame.pack(side=TOP,fill=X)

title=Label(eFrame,text="Employee Management System",font=("calibric",18,"bold"),bg="#535c68",fg="white")
title.grid(row=0,columnspan=2,padx=10,pady=20)

lblName=Label(eFrame,text="Name",font=("calibric",16),bg="#535c68",fg="white")
lblName.grid(row=1,column=0,padx=10,pady=10,sticky="W")

txtName=Entry(eFrame,textvariable=name,font=("calibric",16),width=30)
txtName.grid(row=1,column=1)

lblAge=Label(eFrame,text="Age",font=("calibric",16),bg="#535c68",fg="white")
lblAge.grid(row=1,column=2,padx=10,pady=10,sticky="W")

txtAge=Entry(eFrame,textvariable=age,font=("calibric",16),width=30)
txtAge.grid(row=1,column=3)

lblDoj=Label(eFrame,text="Date Of Joining",font=("calibric",16),bg="#535c68",fg="white")
lblDoj.grid(row=2,column=0,padx=10,pady=10,sticky="W")

txtDoj=Entry(eFrame,textvariable=doj,font=("calibric",16),width=30)
txtDoj.grid(row=2,column=1)

lblEmail=Label(eFrame,text="Email",font=("calibric",16),bg="#535c68",fg="white")
lblEmail.grid(row=2,column=2,padx=10,pady=10,sticky="W")

txtEmail=Entry(eFrame,textvariable=email,font=("calibric",16),width=30)
txtEmail.grid(row=2,column=3)

lblGender=Label(eFrame,text="Gender",font=("calibric",16),bg="#535c68",fg="white")
lblGender.grid(row=3,column=0,padx=10,pady=10,sticky="W")

comboGender=ttk.Combobox(eFrame,font=("calibric",16),width=28,textvariable=gender,state="readonly")
comboGender['values']=('Male','Female','Transgender')
comboGender.grid(row=3,column=1)

lblContact=Label(eFrame,text="Contact",font=("calibric",16),bg="#535c68",fg="white")
lblContact.grid(row=3,column=2,padx=10,pady=10,sticky="W")

txtContact=Entry(eFrame,textvariable=contact,font=("calibric",16),width=30)
txtContact.grid(row=3,column=3)

lblAddress=Label(eFrame,text="Address",font=("calibric",16),bg="#535c68",fg="white")
lblAddress.grid(row=4,column=0,padx=10,pady=10,sticky="W")

txtAddress=Text(eFrame,font=("calibric",16),width=85,height=3)
txtAddress.grid(row=5,columnspan=4,padx=10)

#Button Frame
def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    txtAddress.delete(1.0, END)
    txtAddress.insert(END, row[7])


def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)

def add_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtDoj.get()=="" or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error In Input","Please Fill All The Details")
    print(txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),txtAddress.get(1.0,END))
    db.insert(txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),txtAddress.get(1.0,END))
    messagebox.showinfo("Success","Record Added")
    clear_employee()
    displayAll()
def update_employee():
    if txtName.get()=="" or txtAge.get()=="" or txtEmail.get()=="" or comboGender.get()=="" or txtContact.get()=="" or txtDoj.get()=="" or txtAddress.get(1.0,END)=="":
        messagebox.showerror("Error In Input","Please Fill All The Details")
    print(txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),txtAddress.get(1.0,END))
    db.update(txtName.get(),txtAge.get(),txtDoj.get(),txtEmail.get(),comboGender.get(),txtContact.get(),txtAddress.get(1.0,END),row[0])
    messagebox.showinfo("Success","Record Updated")
    clear_employee()
    displayAll()
def delete_employee():
    db.delete(row[0])
    clear_employee()
    displayAll()

def clear_employee():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAddress.delete(1.0,END)
    



btnFrame=Frame(eFrame,bg="#535c68")
btnFrame.grid(row=6,column=0,columnspan=4,padx=10,pady=20,sticky="W")

btnAdd=Button(btnFrame,command=add_employee,text="Add Details",width=14,font=("calibric",16,"bold"),bg="#16a885",fg="white",activeforeground="#16a885",bd=0).grid(row=0,column=0,padx=10)

btnUpdate=Button(btnFrame,command=update_employee,text="Update Details",width=14,font=("calibric",16,"bold"),bg="#2988b9",fg="white",activeforeground="#2988b9",bd=0).grid(row=0,column=1,padx=10)

btnDelete=Button(btnFrame,command=delete_employee,text="Delete Details",width=14,font=("calibric",16,"bold"),bg="#c8392b",fg="white",activeforeground="#c8392b",bd=0).grid(row=0,column=2,padx=10)

btnClear=Button(btnFrame,command=clear_employee,text="Clear Details",width=14,font=("calibric",16,"bold"),bg="#f39c12",fg="white",activeforeground="#f39c12",bd=0).grid(row=0,column=3,padx=10)



#table view
treeFrame=Frame(root,bg="#ecf0f1")
treeFrame.place(x=0,y=420,height=500,width=1366)

style=ttk.Style()
style.configure('mystyle.Treeview',rowheight=30,font=('calibric',15))
style.configure('mystyle.Treeview.Heading',font=('calibric',15))


tv=ttk.Treeview(treeFrame,column=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=5)
tv.heading("2",text="Name")
tv.heading("3",text="Age")
tv.column("3",width=5)
tv.heading("4",text="D.O.B")
tv.column("4",width=10)
tv.heading("5",text="Email")
tv.heading("6",text="Gender")
tv.column("6",width=7)
tv.heading("7",text="Contact")
tv.heading("8",text="Address")
tv['show']='headings'
tv.pack(fill=X)

tv.bind("<ButtonRelease-1>",getData)

displayAll()
displayAll()
root.mainloop()
