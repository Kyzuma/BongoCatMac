import tkinter as tk
from PIL import ImageTk, Image
from pynput import keyboard
import threading
import sys
import os

# Function to get the resource path for images
# This is necessary for PyInstaller to work correctly
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class BongoCatApp:
    def __init__(self, root):
        
        self.root = root
        # Hides the main window
        root.withdraw()

        # List of characters
        # You can add more characters here
        # Make sure to have the corresponding images in the Images folder
        # For example, if you add "NewCharacter", you should have Images/NewCharacter/idle.png and Images/NewCharacter/hit1.png, etc.
        self.characters = ["Bongo Cat", "Cup", "Monokuma", "Grookey", "Scorbunny", "Sobble", "Yuumi", "Lucio", "Mercy", "Moira", "Zenyatta"]
        self.character = tk.StringVar(value=self.characters[0])

        # Create a top-level window
        # This window will be used to display the character and handle key presses
        self.top = tk.Toplevel(root)
        # Hide the title bar
        self.top.overrideredirect(True)
        self.top.config(bg="white")
        self.top.geometry("220x220")

        # Dropdown
        self.dropdown = tk.OptionMenu(self.top, self.character, *self.characters, command=self.on_character_change)
        self.dropdown.config(
            font=("Helvetica", 10),
            bg="white", fg="black",
            activebackground="white", activeforeground="black",
            highlightthickness=0, bd=0
        )
        self.dropdown["menu"].config(bg="white", fg="black", bd=0, activebackground="lightgray")
        self.dropdown.pack(pady=(5, 0))

        self.keypress_count = 0
        self.counter_label = tk.Label(self.top, text="Key Presses: 0", font=("Helvetica", 12), bg="white", fg="black")
        self.counter_label.pack()

        self.label = tk.Label(self.top, bg="white")
        self.label.pack()

        self.idle_img = None
        self.hit_imgs = []

        self.load_character_images()

        listener_thread = threading.Thread(target=self.start_listener, daemon=True)
        listener_thread.start()

        self.top.after(0, self.place_window_bottom_right)
        self.keep_on_top()

        # Enable window dragging
        self.offset_x = 0
        self.offset_y = 0
        self.top.bind("<Button-1>", self.click_window)
        self.top.bind("<B1-Motion>", self.drag_window)

    # Load character images
    def load_character_images(self):
        # Load idle image
        self.idle_img = ImageTk.PhotoImage(Image.open(resource_path(f"Images/{self.character.get()}/idle.png")))
        # Set initial image to idle
        self.label.config(image=self.idle_img)

        # Load hit frames (hit1.png, hit2.png, ...)
        self.hit_imgs = []
        i = 1
        while True:
            try:
                img = ImageTk.PhotoImage(Image.open(resource_path(f"Images/{self.character.get()}/hit{i}.png")))
                self.hit_imgs.append(img)
                i += 1
            except Exception:
                break
        self.hit_index = 0  # start from the first hit image

    # Change character
    # This function is called when the character is changed in the dropdown
    def on_character_change(self, *_):
        self.load_character_images()

    def start_listener(self):
        def on_press(key):
            self.root.after(0, self.hit_animation)
        with keyboard.Listener(on_press=on_press) as listener:
            listener.join()

    def hit_animation(self):
        if not self.hit_imgs:
            return  # fallback if no hit images

        # Show the next hit frame
        img = self.hit_imgs[self.hit_index]
        self.label.config(image=img)

        # Update index for next press
        # Loop back to the first image if we reach the end
        self.hit_index = (self.hit_index + 1) % len(self.hit_imgs)

        # Increment counter
        self.keypress_count += 1
        self.counter_label.config(text=f"Key Presses: {self.keypress_count}")

        # Switch back to idle after 50ms
        self.top.after(50, lambda: self.label.config(image=self.idle_img))

    # Keep the window on top
    def keep_on_top(self):
        self.top.attributes("-topmost", True)
        self.top.after(1000, self.keep_on_top)

    # Place the window at the bottom right corner of the screen
    def place_window_bottom_right(self):
        self.top.update_idletasks()
        width = self.top.winfo_width()
        height = self.top.winfo_height()
        screen_width = self.top.winfo_screenwidth()
        screen_height = self.top.winfo_screenheight()
        x = screen_width - width
        y = screen_height - height
        self.top.geometry(f"{width}x{height}+{x}+{y}")

    def click_window(self, event):
        self.offset_x = event.x
        self.offset_y = event.y

    def drag_window(self, event):
        x = self.top.winfo_pointerx() - self.offset_x
        y = self.top.winfo_pointery() - self.offset_y
        self.top.geometry(f"+{x}+{y}")

if __name__ == "__main__":
    root = tk.Tk()
    app = BongoCatApp(root)
    root.mainloop()