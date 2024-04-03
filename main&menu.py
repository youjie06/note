import tkinter as tk    #pip install tk
from PIL import Image, ImageTk  #pip install pillow
from notecalendarFM import CalendarFM

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note")
        self.root.geometry("1200x768")
        self.menu_expanded = False
      
        # Menu Frame
        self.menu_frame = tk.Frame(self.root, bd=2, bg="#2d2f32")
        self.menu_frame.place(x=0, y=0, width=50, height=768)

        # Content Frame
        self.content_frame = tk.Frame(self.root, bd=1, bg="#3f4145")
        self.content_frame.place(x=50, y=0, width=850, height=768)
        self.calendar_app = CalendarFM(self.content_frame)
        self.content_frame.grid_rowconfigure(0, weight=1)  # 添加 row 的 resize 能力
        self.content_frame.grid_columnconfigure(0, weight=1)  # 添加 column 的 resize 能力

        # Information Frame
        self.information_frame = tk.Frame(self.root, bd=2, bg="#3c3e42")
        self.information_frame.place(x=900, y=0, width=300, height=768)

        # Define button info
        self.button_info = [("icon/daily-calendar (1).png", " 日歷　"), ("icon/edit.png", " 記事本"),
                            ("icon/list-check.png", " 備忘錄")]
        self.menu_icon_path = "icon/menu-burger.png"
        # Create menu buttons
        self.create_menu_buttons()  # Start with closed menu buttons

        # Menu Button
        self.menu_icon = self.resize_image(self.menu_icon_path, 20, 20)
        self.menu_btn = tk.Button(self.menu_frame,fg="#000000", image=self.menu_icon, bd=0, cursor="hand2", command=self.toggle_menu)
        self.menu_btn.image = self.menu_icon
        self.menu_btn.place(x=7, y=7, width=32, height=32)

    def create_menu_buttons(self):
        self.menu_buttons = []
        button_func = self.create_menu_buttons_expanded if self.menu_expanded else self.create_menu_buttons_closed
        button_func()

    def create_menu_buttons_closed(self):
        for i, (icon_path, button_text) in enumerate(self.button_info):
            button_icon = self.resize_image(icon_path, 20, 20)
            button = tk.Button(self.menu_frame, image=button_icon, fg="#000000", bd=0,
                               cursor="hand2", command=lambda text=button_text: self.show_info(text))
            button.image = button_icon
            button.place(x=7, y=(i + 1) * 40 + 10, width=32, height=32, anchor="nw")
            self.menu_buttons.append(button)

    def create_menu_buttons_expanded(self):
        for i, (icon_path, button_text) in enumerate(self.button_info):
            button_icon = self.resize_image(icon_path, 20, 20)
            button = tk.Button(self.menu_frame, text=button_text, fg="#000000", bd=0, compound=tk.LEFT, font=('宋體', 11 , 'bold'),
                               cursor="hand2", image=button_icon, command=lambda text=button_text: self.show_info(text))
            button.image = button_icon
            button.place(x=7, y=(i + 1) * 40 + 10, width=90, height=32, anchor="nw")
            self.menu_buttons.append(button)

    def toggle_menu(self):
        if self.menu_expanded:
            # Hide menu buttons
            for button in self.menu_buttons:
                button.destroy()
            # Restore default frame proportions
            self.menu_frame.place(x=0, y=0, width=50, height=768)
            self.content_frame.place(x=50, y=0, width=850, height=768)
            self.information_frame.place(x=900, y=0, width=300, height=768)
            self.menu_expanded = False
        else:
            # Adjust frame proportions
            self.menu_frame.place(x=0, y=0, width=120, height=768)
            self.content_frame.place(x=120, y=0, width=780, height=768)
            self.menu_expanded = True
        # Recreate menu buttons
        self.create_menu_buttons()

    def show_info(self, button_text):
        # You can implement the functionality to show detailed information based on the button clicked
        print(f"Button clicked: {button_text}")

    def resize_image(self, image_path, width, height):
        image = Image.open(image_path)
        image = image.resize((width, height), Image.LANCZOS)
        return ImageTk.PhotoImage(image)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
