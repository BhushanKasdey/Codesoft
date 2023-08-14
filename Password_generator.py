import string
import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        plen = int(length_entry.get())
        if plen <= 0:
            messagebox.showerror("Error", "Please enter a positive length.")
        else:
            s1 = string.ascii_uppercase
            s2 = string.ascii_lowercase
            s3 = string.digits
            s4 = string.punctuation
            s = []
            s.extend(list(s1))
            s.extend(list(s2))
            s.extend(list(s3))
            s.extend(list(s4))
            random.shuffle(s)
            generated_password = "".join(s[:plen])
            password_label.config(text="Generated password: " + generated_password)
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")

length_label = tk.Label(root, text="Enter the desired length of the password:")
length_entry = tk.Entry(root)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
password_label = tk.Label(root,fg="blue", text="Generated password:")

length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button.grid(row=1, columnspan=2, padx=10, pady=10)
password_label.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
