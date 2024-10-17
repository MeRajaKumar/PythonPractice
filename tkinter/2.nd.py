import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Username Label and Input
username_label = tk.Label(root, text="Username:", font=("Arial", 14))
username_label.grid(row=0, column=0, padx=10, pady=10)

username_entry = tk.Entry(root, width=30)
username_entry.grid(row=0, column=1, padx=10, pady=10)
username_entry.insert(tk.END, "Type your text here...")

# Password Label and Input
password_label = tk.Label(root, text="Password:", font=("Arial", 14))
password_label.grid(row=1, column=0, padx=10, pady=10)

password_entry = tk.Entry(root, width=30, show="*")  # show="*" hides the password input
password_entry.grid(row=1, column=1, padx=10, pady=10)
password_entry.insert(tk.END, "Type your text here...")

# Login Button
login_button = tk.Button(root, text="Login", font=("Arial", 14))
login_button.grid(row=2, column=0, padx=10, pady=20)
login_button = tk.Button(root, text="Reset", font=("Arial", 14))
login_button.grid(row=2, column=1, padx=0, pady=0)

# Start the Tkinter event loop
root.mainloop()
