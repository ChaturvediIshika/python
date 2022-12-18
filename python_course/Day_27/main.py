from tkinter import *

def button_clicked():
    s=input.get()
    label["text"]=s

window=Tk()
window.title("my program")
window.minsize(500,500)

label=Label(text="i am label", font=("arial",24,"bold"))
label.grid(column=0,row=0)

button_1=Button(text="button 1", command=button_clicked)
button_1.grid(column=1,row=1)

button_2=Button(text="button 2")
button_2.grid(column=2,row=0)

input=Entry(width=10)
print(input.get())
input.grid(column=3,row=2)


window.mainloop()