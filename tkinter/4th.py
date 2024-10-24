import tkinter as tk
from threading import Thread
import time

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Process Control Example")
        self.timer_running = False
        self.label = tk.Label(root, text="Timer: 0 seconds", font=("Arial", 14))
        self.label.pack(pady=20)
        
        self.start_button = tk.Button(root, text="Start Timer", command=self.start_timer)
        self.start_button.pack(side=tk.LEFT, padx=20)

        self.stop_button = tk.Button(root, text="Stop Timer", command=self.stop_timer)
        self.stop_button.pack(side=tk.RIGHT, padx=20)

        self.time_elapsed = 0

    def start_timer(self):
        if not self.timer_running:
            self.timer_running = True
            self.time_thread = Thread(target=self.run_timer)
            self.time_thread.start()

    def stop_timer(self):
        self.timer_running = False

    def run_timer(self):
        while self.timer_running:
            time.sleep(1)
            self.time_elapsed += 1
            self.update_label()

    def update_label(self):
        self.label.config(text=f"Timer: {self.time_elapsed} seconds")

# Create the main window
root = tk.Tk()
app = TimerApp(root)

# Run the application
root.mainloop()
