import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Username Label and Input
username_label = tk.Label(root, text="Username:", font=("Arial", 14))

username_entry = tk.Entry(root, width=30)

# Password Label and Input
password_label = tk.Label(root, text="Password:", font=("Arial", 14))

password_entry = tk.Entry(root, width=30, show="*")  # show="*" hides the password input

# Login Button
login_button = tk.Button(root, text="Login", font=("Arial", 14))

# Start the Tkinter event loop
root.mainloop()
