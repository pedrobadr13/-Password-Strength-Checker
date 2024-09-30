import tkinter as tk
from tkinter import messagebox
import re

# Function to check password strength
def check_password_strength():
    password = entry.get()
    strength = password_strength_checker(password)
    messagebox.showinfo("Password Strength", strength)

# Password strength checker logic
def password_strength_checker(password):
    if len(password) < 8:
        return "Too short"
    if not re.search(r"[A-Z]", password):
        return "Missing uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Missing lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Missing digit"
    if not re.search(r"[!@#$%^&*]", password):
        return "Missing special character"
    return "Strong password"

# GUI setup
root = tk.Tk()
root.geometry("500x500")
root.title("Password Strength Checker")

label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry = tk.Entry(root, )
entry.pack(pady=10)
                                               # key word argumment command
button = tk.Button(root, text="Check Strength", command=check_password_strength)
button.pack(pady=10)

root.mainloop()


