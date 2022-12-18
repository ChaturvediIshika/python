from tkinter import *

def miles_to_km():
    m=input_miles.get()
    k=int(m)*1.609
    r=round(k,3)
    calculate.config(text=r)

window=Tk()
window.title("Mile To Km Converter")
window.config(padx=75,pady=75)

input_miles=Entry(width=10)
input_miles.get()
input_miles.grid(column=1,row=0)

miles=Label(text="Miles")
miles.grid(column=2,row=0)

equal=Label(text="is equal to")
equal.grid(column=0,row=1)

calculate=Label(text="0")
calculate.grid(column=1,row=1)

kms=Label(text="Kms")
kms.grid(column=2,row=1)

button=Button(text="calculate",command=miles_to_km)
button.grid(column=1,row=2)

window.mainloop()