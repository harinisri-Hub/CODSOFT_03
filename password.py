import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 0:
            raise ValueError("Password length must be positive")

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))

        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)

    except ValueError as ve:
        messagebox.showerror("Error", str(ve))

# Create the main window
root = tk.Tk()
root.title("Password Generator")

# Create and place the widgets
label_length = tk.Label(root, text="Enter desired password length:")
label_length.grid(row=0, column=0, padx=10, pady=10)

entry_length = tk.Entry(root)
entry_length.grid(row=0, column=1, padx=10, pady=10)

button_generate = tk.Button(root, text="Generate Password", command=generate_password)
button_generate.grid(row=1, column=0, columnspan=2, pady=10)

label_password = tk.Label(root, text="Generated Password:")
label_password.grid(row=2, column=0, padx=10, pady=10)

entry_password = tk.Entry(root)
entry_password.grid(row=2, column=1, padx=10, pady=10)

# Run the application
root.mainloop()
