import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

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
    print(len(website_out), len(password_out), len(email_out))

    if len(website_out) < 1 or len(password_out) < 4 or len(email_out) < 6:
        messagebox.showerror(message="You must fill in all the fields")

    else:
        popup = messagebox.askokcancel(title="Information", message=f"These are the details: \nwebsite: {website_out}\nemail: {email_out} "
                                            f"\npassword: {password_out}, \nIs it okay to save?")
        if popup:
            with open("data.txt", "a") as data:
                data.write(f"{website_out} | {email_out} | {password_out} \n")

            website_entry.delete(0, "end")
            password_entry.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.config(pady=50, padx=50)
window.maxsize(530, 400)
window.minsize(530, 400)

#canvas
logo = tk.PhotoImage(file="logo.png")
canvas = tk.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, columnspan=2)

#labels
website = tk.Label(text="Website: ")
website.grid(row=1, column=0)
website_entry = tk.Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email = tk.Label(text="Email/Username: ")
email.grid(row=2, column=0)
email_entry = tk.Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "djoni7vincent@gmail.com")

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
