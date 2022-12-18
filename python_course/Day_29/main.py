from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

def search_password():
    w=website_entry.get()
    try:
        with open("password.json",mode="r") as data:
            file=json.load(data)
            messagebox.showinfo(title=w,message=f'email= {file[w]["email"]}\npassword= {file[w]["password"]}')
    except KeyError:
        messagebox.showinfo(title="ERROR",message="No details for the website exists.")
    except FileNotFoundError:
        messagebox.showinfo(title="ERROR",message="NO data file found.")



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters=[random.choice(letters) for _ in range(nr_letters)]
    password_numbers=[random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols=[random.choice(symbols) for _ in range(nr_symbols)]

    password_list=password_letters+password_numbers+password_symbols
    random.shuffle(password_list)

    password="".join(password_list)
    pyperclip.copy(password)

    password_entry.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    w=website_entry.get()
    e=email_entry.get()
    p=password_entry.get()
    new_data={
        w:{
            "email":e,
            "password":p
        }
    }

    if len(w)==0 or len(p)==0:
        messagebox.showinfo(title="Oops!!",message="Please don't leave any entries empty.")
    else:
        b=messagebox.askokcancel(title=w,message=f"These are the details entered:\nEmail:{e}\nPassword:{p}\nIs it ok to add?")
        if b:
            try:
                with open("password.json",mode="r") as data:
                    file=json.load(data)
            except FileNotFoundError:
                with open("password.json",mode="w") as data:
                    json.dump(obj=new_data, fp=data,indent=4)
            else:
                file.update(new_data)
                with open("password.json",mode="w") as data:
                    json.dump(file, data,indent=4)
            finally:
                website_entry.delete(0,END)
                password_entry.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
photo=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=photo)
canvas.grid(column=1,row=0)

website=Label(text="Website:")
website.grid(column=0,row=1)

email=Label(text="email/Username:")
email.grid(column=0,row=2)

password=Label(text="Password:")
password.grid(column=0,row=3)

website_entry=Entry(width=40)
website_entry.get()
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

email_entry=Entry(width=50)
email_entry.get()
email_entry.grid(column=1,row=2,columnspan=2)
email_entry.insert(0, "cishika104@gmail.com")

password_entry=Entry(width=25)
password_entry.get()
password_entry.grid(column=1,row=3)

generate=Button(text="GENERATE PASSWORD",command=generate_password)
generate.grid(column=2,row=3)

add=Button(text="ADD",width=36, command=save_password)
add.grid(column=1,row=4,columnspan=2)

search=Button(text="SEARCH",command=search_password)
search.grid(column=2,row=1)


window.mainloop()
