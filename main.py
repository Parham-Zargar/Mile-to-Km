import tkinter

window = tkinter.Tk()
window.title("My_first_GUI")
window.minsize(width=500, height=300)
def button_got_clicked():
    new_text = input.get()
    label.config(text=new_text)


# Create label
label = tkinter.Label(text="Helle everyone !\nI'm here.", font=("Arial", 24, 'bold'))
label.grid(column=0 , row=0)

# Create Buttons

button = tkinter.Button(text="click me", command=button_got_clicked)
button.grid(column=1, row=1)
new_button = tkinter.Button(text="New Button")
new_button.grid(column=2, row=0)
# Entry

input = tkinter.Entry(width= 10)
input.get()
input.grid(column=4, row= 3)







window.mainloop()
