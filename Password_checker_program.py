import tkinter as tk
import re

def update_strength(*args):
    password = password_var.get()
    feedback = ""
    strength = 0

    if len(password) >= 8:
        strength += 1
    else:
        feedback += "Password must be at least 8 characters long.\n"

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback += "Add at least one uppercase letter.\n"

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        feedback += "Add at least one lowercase letter.\n"

    if re.search(r'\d', password):
        strength += 1
    else:
        feedback += "Add at least one number.\n"

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1
    else:
        feedback += "Add at least one special character.\n"

    if strength == 5:
        result.set("Strong Password")
    elif 3 <= strength < 5:
        result.set("Medium Strength Password")
    else:
        result.set("Weak Password")

    feedback_text.set(feedback.strip())

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x300")

tk.Label(root, text="Enter Password:", font=('Arial', 12)).pack(pady=10)

password_var = tk.StringVar()
password_var.trace_add('write', update_strength)

entry = tk.Entry(root, textvariable=password_var, width=30, show="*", font=('Arial', 12))
entry.pack()

result = tk.StringVar()
tk.Label(root, textvariable=result, font=('Arial', 12, 'bold')).pack(pady=5)

feedback_text = tk.StringVar()
tk.Label(root, textvariable=feedback_text, font=('Arial', 10), fg="red", wraplength=350, justify="left").pack(pady=5)

root.mainloop()
