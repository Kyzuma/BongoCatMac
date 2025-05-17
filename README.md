
# 🐾 Bongo Cat Keypress Widget (macOS Compatible)

Inspired by the adorable **Bongo Cat** app on Steam, this lightweight Python-based version brings the same delightful experience to **macOS** — and even tracks your keypresses!

## 🎯 Features

- 🐱 Bongo Cat that bops left and right with every keypress  
- ⌨️ Tracks and displays total number of keypresses  
- 🖼️ Custom images for idle, left tap, and right tap animations
- 💻 Designed to work seamlessly on **macOS**

## 🧰 Tech Stack

- `tkinter` – for GUI interface  
- `Pillow (PIL)` – for image processing  
- `pynput` – for global keyboard event listening  
- `threading` – to run background keyboard listener without freezing the GUI

## 📸 Preview

<img src="Images/preview.gif" alt="Bongo Cat in action" width="150" />

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/yourusername/bongo-cat-mac.git
cd bongo-cat-mac
```

### 2. Install Dependencies
Make sure you have Python 3 installed, then run:
```bash
pip3 install -r requirements.txt
```

### 3. Add Your Images

Add your own images in the `Images/` folder!

You can design your own or find free Bongo Cat sprites online.

### 4. Run the App
```bash
python bongocat.py
```

## ⚙️ Customization

- **Widget size:** Set to `200x150`, but you can change it in this line:
  ```python
  self.top.geometry("200x150")
  ```
- **Placement:** Automatically anchored to bottom-right, but customizable in `place_window_bottom_right()`.

## 🖥️ Packaging with PyInstaller

To create a standalone app, use PyInstaller:

```bash
pyinstaller --onefile --windowed --name "Bongo Cat" --add-data "Images:Images" --icon=icon.icns bongocat.py
```

- `--name` names the Application
- `--windowed` hides the terminal on macOS/Windows.  
- `--add-data` bundles the Images folder (colon `:` on macOS/Linux, semicolon `;` on Windows).

After building, find your app inside the dist/ folder.

⚠️ Note for macOS users: After building, you might need to grant Input Monitoring permission to your app for key tracking to work (see below).

## 🙋 FAQ

**Q: How do I make the icon show on my app?**  
A: Provide a properly formatted `.icns` (macOS) or `.ico` (Windows) file and add `--icon=iconfile` when running PyInstaller.

## ✨ Acknowledgements

- Original idea inspired by [Bongo Cat on Steam](https://store.steampowered.com/app/3419430/Bongo_Cat/)  
- Sprite credit: https://imgur.com/a/bongo-cat-diy-0o31WpY

