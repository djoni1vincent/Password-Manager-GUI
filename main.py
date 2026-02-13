import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def ganerete_pass():
    password_entry.delete(0, "end")

    password_list = []
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list += [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]

    random.shuffle(password_list)

    for char in password_list:
        password_entry.insert(0, char)
    pyperclip.copy(password_entry.get())

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_pass():
    website_out = website_entry.get()
    email_out = email_entry.get()
    password_out = password_entry.get()

    new_data = {
        website_out: {
            "email": email_out,
            "password": password_out,
        }
    }
    if len(website_out) < 1 or len(password_out) < 4 or len(email_out) < 6:
        messagebox.showerror(message="You must fill in all the fields")

    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
                data.update(new_data)
        except json.JSONDecodeError, FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            website_entry.delete(0, "end")
            password_entry.delete(0, "end")

def find_password():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        web = website_entry.get().title()
        print(data[web]["email"])

        if web in data:
            pyperclip.copy(data[web]["password"])
            popup = messagebox.showinfo(title="Information", message=f"These are the details: \nemail: {data[web]["email"]} "
                                  f"\npassword: {data[web]["password"]}")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(pady=50, padx=50)
window.maxsize(550, 400)
window.minsize(550, 400)

#canvas
logo = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, columnspan=2)

#labels
website_label = tk.Label(text="Website: ")
website_label.grid(row=1, column=0)
website_entry = tk.Entry(width=20)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

search_button = tk.Button(text="Search", width=24, command=find_password)
search_button.grid(row=1, column=2)

email = tk.Label(text="Email/Username: ")
email.grid(row=2, column=0)
email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@gmail.com")

password = tk.Label(text="Password: ")
password.grid(row=3, column=0)
password_entry = tk.Entry(width=20)
password_entry.grid(row=3, column=1,columnspan=1)

#buttons
button_generate = tk.Button(text="Generate Password", command=ganerete_pass)
button_generate.grid(row=3, column=2)

button_add = tk.Button(text="Add", width=36, command=save_pass)
button_add.grid(row=4, column=1, columnspan=2)


window.mainloop()
