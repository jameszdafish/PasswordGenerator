from tkinter import *
from tkinter import font
import random

generated_password = ""
stored_password = ""
possible_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                       "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
                       "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "1", "2",
                       "3", "4", "5", "6", "7", "8", "9", "0", "!", "#", "$", "%", "&", "'", '"', "(", ")", "*",
                       "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`",
                       "{", "|", "}", "~"]


def hide_text():
    global generated_password
    global stored_password
    if checked_var.get() == 1:
        stored_password = generated_password
        text_entry_box.delete(0, END)
        text_entry_box.insert(0, "************")
    else:
        text_entry_box.delete(0, END)
        text_entry_box.insert(0, stored_password)


def validate_entry(text):
    if len(text) <= 12:
        return True
    else:
        return False


def on_entry_change(*args):
    global generated_password
    generated_password = entry_var.get()


def generate_password():
    global generated_password
    text_entry_box.delete(0, END)
    stop_timer = 0
    while stop_timer < 12:
        character_decider = random.randint(1, 94)
        generated_password += possible_characters[character_decider]
        stop_timer += 1
    text_entry_box.insert(0, generated_password)


root = Tk()
root.title("Password Generator")
root.geometry("550x50")
root.resizable(False, False)

label_font = font.Font(family="Calibri", size=15)
button_font = font.Font(family="Calibri", size=10)

instructions_label = Label(text="Password:", font=label_font)
instructions_label.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")


# character limit
validate_entry_cmd = root.register(validate_entry)
entry_var = StringVar()
entry_var.trace("w", on_entry_change)
text_entry_box = Entry(relief="raised", font=label_font, textvariable=entry_var,
                       validate="key", validatecommand=(validate_entry_cmd, '%P'))
text_entry_box.grid(row=0, column=1, padx=1, pady=10, sticky="NSEW")


# hide text
checked_var = IntVar()
show_password_checkbox = Checkbutton(text="Show Password", relief="raised", variable=checked_var, command=hide_text)
show_password_checkbox.grid(row=0, column=2, padx=1, pady=1, sticky="NSEW")

generate_password_button = Button(text="Generate Password", font=button_font, command=generate_password)
generate_password_button.grid(row=0, column=3, padx=1, pady=1, sticky="NSEW")

root.mainloop()
