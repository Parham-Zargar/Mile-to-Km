from tkinter import *

window = Tk()
window.minsize(width=250, height=150)
window.config(padx=50 ,pady=100)

# label 1
label1 = Label(text="Miles")
label1.grid(row=0, column=3)

# label 2
label2 = Label(text="Is equal to")
label2.grid(row=1, column=0)

# label 3
label3= Label(text="0")
label3.grid(row=1,column=1)

# label 4
label4 = Label(text="Km")
label4.grid(row=1,column=3)

# button
def calculate(*args):
    new_entry = round(int(entry.get()) * 1.6)
    label3.config(text=new_entry)


button = Button(text="Calculate" , command= calculate)
button.grid(row=3, column=1)
# entry
entry = Entry(width=10)
entry.grid(row=0,column=1)







window.mainloop()