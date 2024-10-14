# import tkinter as tk


# root = tk.Tk()
# root.title("First Tkinter Window")
# #Label
# label = tk.Label(root, text="Hello, this is a label!", font=("Arial", 16), justify=("left"))
# label.pack(side="left", anchor="nw")
# #textbox
# textbox = tk.Text(root, height=5, width=40)
# textbox.pack(side="left", anchor="nw")
# textbox.insert(tk.END, "Type your text here...")

# root.mainloop()


import tkinter as tk

root = tk.Tk()
root.title("First Tkinter Window")

# Label
label = tk.Label(root, text="Hello, this is a label!", font=("Arial", 16))
label.pack(anchor="nw")  # Pack the label to the top-left (northwest) corner

# Textbox
textbox = tk.Text(root, height=5, width=40)
textbox.pack(anchor="nw")  # Pack the textbox below the label
textbox.insert(tk.END, "Type your text here...")

root.mainloop()

