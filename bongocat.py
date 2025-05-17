import tkinter as tk
from PIL import ImageTk, Image
from pynput import keyboard
import threading
import sys
import os

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class BongoCatApp:
    def __init__(self, root):
        self.root = root
        root.withdraw()

        self.top = tk.Toplevel(root)
        self.top.overrideredirect(True)
        self.top.config(bg="white")
        self.top.geometry("200x150")

        # Load images using resource_path
        self.idle_img = ImageTk.PhotoImage(Image.open(resource_path("Images/cat_idle.png")))
        self.left_img = ImageTk.PhotoImage(Image.open(resource_path("Images/cat_left.png")))
        self.right_img = ImageTk.PhotoImage(Image.open(resource_path("Images/cat_right.png")))

        self.keypress_count = 0
        self.counter_label = tk.Label(self.top, text="Key Presses: 0", font=("Helvetica", 12), bg="white", fg="black")
        self.counter_label.pack()

        self.label = tk.Label(self.top, image=self.idle_img, bg="white")
        self.label.pack()

        self.left_turn = True

        listener_thread = threading.Thread(target=self.start_listener, daemon=True)
        listener_thread.start()

        self.top.after(0, self.place_window_bottom_right)
        self.keep_on_top()

    def place_window_bottom_right(self):
        self.top.update_idletasks()
        width = self.top.winfo_width()
        height = self.top.winfo_height()
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x = screen_width - width
        y = screen_height - height
        self.top.geometry(f"{width}x{height}+{x}+{y}")

    def start_listener(self):
        def on_press(key):
            self.root.after(0, self.hit_animation)

        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def hit_animation(self):
        self.label.config(image=self.left_img if self.left_turn else self.right_img)
        self.keypress_count += 1
        self.counter_label.config(text=f"Key Presses: {self.keypress_count}")
        self.left_turn = not self.left_turn
        self.top.after(50, lambda: self.label.config(image=self.idle_img))

    def keep_on_top(self):
        self.top.attributes("-topmost", True)
        self.top.after(1000, self.keep_on_top)

if __name__ == "__main__":
    root = tk.Tk()
    app = BongoCatApp(root)
    root.mainloop()