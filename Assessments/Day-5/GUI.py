from tkinter import *
import pymysql


def sel():
    db = pymysql.connect("localhost", "root", "", "test")
    cursor = db.cursor()
    data = cursor.execute('''CREATE TABLE REGISTER(FIRST_NAME CHAR(20) NOT NULL, LAST_NAME CHAR(20))''')
    
    firstname = f_name.get()
    lastname = l_name.get()

    data = cursor.fetchall()
    for row in data:
        if row[0] == firstname:
            print("Valid Username")
            if row[1] == lastname:
                print('Logged In')
                break
        else:
            print("Invalid Username")
    db.commit()
    db.close()
def sel1():
    d={1:"Male",2:"Female"}
    selection = d[var.get()]
    print(d[var.get()])
    label.config(text = selection)

tkit = Tk()
f_name = StringVar()
T1 = Entry(tkit, text="First Name", textvariable=f_name)
T1.pack(side=TOP)
l_name = StringVar()
T2 = Entry(tkit, text="Last Name", textvariable=l_name)
T2.pack(side=TOP)
var = IntVar()
R1 = Radiobutton(tkit, text = "Male",
				variable = var, 
				value = 1,
                  command = sel1)

R1.pack()
R2 = Radiobutton(tkit, text = "Female", 
				variable = var, 
				value = 2,
                  command = sel1)
R2.pack()
B1 = Button(tkit,text='Submit',bd=10,command=sel1)
label = Label(tkit)
B1.pack(side=BOTTOM)
tkit.mainloop()


def sel():
	d={1:"Hello",2:"Good Morning",3:"AC"}
	selection = d[var.get()]
	label.config(text = selection)

root = Tk()
var = IntVar()#The Variable Classes (BooleanVar, DoubleVar, IntVar, StringVar)
R1 = Radiobutton(root, text = "Option 1",
				variable = var, 
				value = 1,
                  command = sel)


R2 = Radiobutton(root, text = "Option 2", 
				variable = var, 
				value = 2,
                  command = sel)