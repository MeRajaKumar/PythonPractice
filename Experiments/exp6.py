import tkinter as tk
import time
from threading import Thread

class ProcessControlApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Control with Tkinter")

        self.label = tk.Label(root, text="Process not running", font=("Arial", 14))
        self.label.pack(pady=20)

        self.start_button = tk.Button(root, text="Start Process", command=self.start_process)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(root, text="Stop Process", command=self.stop_process)
        self.stop_button.pack(side=tk.RIGHT, padx=20)

        self.process_running = False
        self.counter = 0

    def process_task(self):
        """This function will run as a background process."""
        while self.process_running:
            time.sleep(1)
            self.counter += 1
            self.update_label(f"Process running... {self.counter} seconds elapsed")

    def start_process(self):
        """Start the background process if not already running."""
        if not self.process_running:
            self.process_running = True
            self.update_label("Process started")
            self.process_thread = Thread(target=self.process_task)
            self.process_thread.start()

    def stop_process(self):
        """Stop the background process."""
        self.process_running = False
        self.update_label("Process stopped")

    def update_label(self, text):
        """Update the label text."""
        self.label.config(text=text)

root = tk.Tk()
app = ProcessControlApp(root)

root.mainloop()
