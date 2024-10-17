import tkinter as tk

# Function to clear placeholders if clicked on input field
def on_entry_click(event, entry, placeholder_text):
    if entry.get() == placeholder_text:
        entry.delete(0, "end")  # delete all the text in the entry
        entry.config(fg="black")  # set the text color to black

# Function to reset placeholder if the field is empty after losing focus
def on_focusout(event, entry, placeholder_text):
    if entry.get() == '':
        entry.insert(0, placeholder_text)
        entry.config(fg="grey")

# Function for login button
def login():
    print("Login successful!")

# Function for reset button
def reset():
    username_entry.delete(0, 'end')
    password_entry.delete(0, 'end')
    # Reset the placeholders
    username_entry.insert(0, "Enter Username")
    username_entry.config(fg="grey")
    password_entry.insert(0, "Enter Password")
    password_entry.config(fg="grey")

# Create the main window
root = tk.Tk()
root.title("Login Form")

# Create username entry with placeholder
username_entry = tk.Entry(root, fg="grey")
username_entry.insert(0, "Enter Username")
username_entry.bind('<FocusIn>', lambda event: on_entry_click(event, username_entry, "Enter Username"))
username_entry.bind('<FocusOut>', lambda event: on_focusout(event, username_entry, "Enter Username"))
username_entry.pack(pady=10)

# Create password entry with placeholder
password_entry = tk.Entry(root, fg="grey", show="")
password_entry.insert(0, "Enter Password")
password_entry.bind('<FocusIn>', lambda event: on_entry_click(event, password_entry, "Enter Password"))
password_entry.bind('<FocusOut>', lambda event: on_focusout(event, password_entry, "Enter Password"))
password_entry.pack(pady=10)

# Create the login button
login_button = tk.Button(root, text="Login", command=login)
login_button.pack(pady=5)

# Create the reset button
reset_button = tk.Button(root, text="Reset", command=reset)
reset_button.pack(pady=5)

# Run the GUI main loop
root.mainloop()
