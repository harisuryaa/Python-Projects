from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for char in range(nr_letters)]

    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]
    password_list = password_numbers+  password_symbols+password_letters

    random.shuffle(password_list)

    password = "".join(password_list)

    password_name.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def find_password():
    web_search = web_name.get()
    try:

        with open("data.json") as file:
            data = json.load(file)
            easy_data = data[web_search]
            value= [easy_data[i] for i in easy_data]
            messagebox.showinfo(title=web_search, message=f'email: {value[0]}\n Password: {value[1]}')
    except:
        messagebox.showinfo(title="hello",message=f"No details for {web_search} ")

def save():
    website_id = web_name.get()
    email_id = mail_name.get()
    password_id = password_name.get()
    new_data = {
        website_id : {
            "email": email_id,
            "password": password_id
        }
    }
    if len(website_id)==0 or len(password_id)==0:
        messagebox.showinfo(title="Oops", message="please dont leave any feilds empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except :
            with open("data.json", "a") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        web_name.delete(0, END)
        password_name.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200,height=200)
photo = PhotoImage(file="logo.png")
canvas.create_image(100,100, image =photo)
canvas.grid(column=1,row=0)

#website
website = Label(text="Website: ")
website.grid(column=0,row=1)
web_name = Entry(width=21)
web_name.grid(column=1,row=1)
web_name.focus()
#email
email = Label(text="Email/Username: ")
email.grid(column=0,row=2)
mail_name = Entry(width=35)
mail_name.grid(column=1,row=2,columnspan=2)
mail_name.insert(0,"hari@gmail.com")
#password
password_l = Label(text="Password: ")
password_l.grid(column=0,row=3)
password_name = Entry(width=21)
password_name.grid(column=1,row=3)
generate_pass=Button(text="Generate Password", command=password_gen)
generate_pass.grid(column=2,row=3)
add = Button(text="Add",width=36,command=save)
add.grid(column=1,row=4,columnspan=2)
#search
search = Button(text="Search",width=10,command=find_password)
search.grid(column=2,row=1)






window.mainloop()