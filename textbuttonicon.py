import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Button Example")
        self.geometry("400x200")

        # Create a frame
        frame = ttk.Frame(self)
        frame.pack(padx=20, pady=20)

        # Resize function
        def resize_image(image_path, width, height):
            image = Image.open(image_path)
            image = image.resize((width, height), Image.LANCZOS)  # 使用 Image.LANCZOS 縮放方法
            return ImageTk.PhotoImage(image)

        # Button 1 - 日歷
        button1_icon = resize_image("icon/calendar-day.png", 32, 32)
        button1 = ttk.Button(frame, text="日歷", compound=tk.LEFT, image=button1_icon)
        button1.image = button1_icon
        button1.pack(pady=5, fill=tk.X)

        # Button 2 - 記事本
        button2_icon = resize_image("icon/calendar-pen.png", 32, 32)
        button2 = ttk.Button(frame, text="記事本", compound=tk.LEFT, image=button2_icon)
        button2.image = button2_icon
        button2.pack(pady=5, fill=tk.X)

        # Button 3 - 備忘錄
        button3_icon = resize_image("icon/alarm-clock.png", 32, 32)
        button3 = ttk.Button(frame, text="備忘錄", compound=tk.LEFT, image=button3_icon)
        button3.image = button3_icon
        button3.pack(pady=5, fill=tk.X)

        # Button 4 - 繪畫板
        button4_icon = resize_image("icon/menu-burger.png", 32, 32)
        button4 = ttk.Button(frame, text="繪畫板", compound=tk.LEFT, image=button4_icon)
        button4.image = button4_icon
        button4.pack(pady=5, fill=tk.X)

if __name__ == "__main__":
    app = App()
    app.mainloop()
