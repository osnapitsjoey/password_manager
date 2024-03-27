from tkinter import *
from tkinter import messagebox
from random import choice, shuffle, randint
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_list = [choice(letters) for char in range(randint(8, 10))]
    password_list += [choice(symbols) for sym in range(randint(2, 4))]
    password_list += [choice(numbers) for num in range(randint(2, 4))]

    shuffle(password_list)

    password = "".join(password_list)
    pass_entry.insert(0, password)
    if len(pass_entry.get()) > 0:
        pass_entry.delete(0, END)
        pass_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website = website_entry.get().lower()
    email = email_user_entry.get()
    pass_made = pass_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": pass_made,
        }
    }

    if len(website) == 0 or len(pass_made) == 0 or len(email) == 0:
        messagebox.showwarning(
            title="oops", message="Please make sure to fill in all of the fields."
        )
    else:
        try:
            with open("passwords.json", mode="r") as password_file:
                data = json.load(password_file)

        except FileNotFoundError:
            with open("passwords.json", mode="w") as password_file:
                json.dump(new_data, password_file, indent=4)
        else:
            data.update(new_data)

            with open("passwords.json", mode="w") as password_file:
                json.dump(data, password_file, indent=4)
        finally:
            website_entry.delete(0, "end")
            pass_entry.delete(0, "end")


# ---------------------------Search For Password----------------------- #
def search():
    website = website_entry.get().lower()
    try:
        with open("passwords.json", mode="r") as search_file:
            data = json.load(search_file)
    except FileNotFoundError:
        messagebox.showwarning(
            title="Error", message="You do not have any saved passwords."
        )
    else:
        if website in data:
            show_email = data[website]["email"]
            show_pass = data[website]["password"]
            messagebox.showinfo(
                title=website.title(),
                message=f"Email: {show_email}\n\n" f"Password: {show_pass}",
            )
        else:
            messagebox.showwarning(
                title="oops", message="You do not have a password for this site saved."
            )


# ---------------------------- UI SETUP ------------------------------- #

# Main Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="#282A36")

# Canvas
canvas = Canvas(width=200, height=200, bg="#282A36", highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
bg_image = canvas.create_image(120, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:", bg="#282A36", fg="#d4483b", highlightthickness=0)
website_label.grid(column=0, row=1)

email_user_label = Label(
    text="Email/Username:", bg="#282A36", fg="#d4483b", highlightthickness=0
)
email_user_label.grid(column=0, row=2)

pass_label = Label(text="Password:", bg="#282A36", fg="#d4483b", highlightthickness=0)
pass_label.grid(column=0, row=3)

# Entries

website_entry = Entry(
    width=36,
    highlightcolor="#F1FA8C",
    bg="#44475A",
    fg="#F8F8F2",
    selectbackground="#6272A4",
)
website_entry.focus()
website_entry.grid(column=1, row=1, sticky=EW)

email_user_entry = Entry(
    width=21,
    highlightcolor="#F1FA8C",
    bg="#44475A",
    fg="#F8F8F2",
    selectbackground="#6272A4",
)
email_user_entry.insert(0, "testing@email.com")
email_user_entry.grid(column=1, row=2, columnspan=2, sticky=EW)

pass_entry = Entry(
    width=36,
    highlightcolor="#F1FA8C",
    bg="#44475A",
    fg="#F8F8F2",
    selectbackground="#6272A4",
)
pass_entry.grid(column=1, row=3, sticky=EW)

# Buttons

generate_button = Button(
    text="Generate Password",
    bg="#44475A",
    fg="#FFB86C",
    highlightthickness=0,
    activebackground="#44475A",
    command=generate_password,
)
generate_button.grid(column=2, row=3, sticky=EW)

search_button = Button(
    text="Search",
    bg="#44475A",
    fg="#FFB86C",
    highlightthickness=0,
    activebackground="#44475A",
    command=search,
)
search_button.grid(column=2, row=1, sticky=EW)

save_pass_button = Button(
    text="Add",
    width=52,
    command=save,
    bg="#44475A",
    fg="#FFB86C",
    highlightthickness=0,
    activebackground="#44475A",
)
save_pass_button.grid(column=1, row=4, columnspan=2, sticky=EW)

window.mainloop()
