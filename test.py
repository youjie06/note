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
        self.menu_frame = tk.Frame(self.root, bd=2, bg="#1e1f22")
        self.menu_frame.place(x=0, y=0, width=50, height=768)

        # Content Frame
        self.content_frame = tk.Frame(self.root, bd=1, bg="#3f4145")
        self.content_frame.place(x=50, y=0, width=850, height=768)
        self.calendar_app = CalendarFM(self.content_frame)

        # Information Frame
        self.information_frame = tk.Frame(self.root, bd=2, bg="#1e1f22")
        self.information_frame.place(x=900, y=0, width=300, height=768)

        # Define button info
        self.button_info = [("icon/calendar-day.png", "日歷　"), ("icon/calendar-pen.png", "記事本"),
                            ("icon/alarm-clock.png", "備忘錄"), ("icon/menu-burger.png", "繪畫板")]

        # Create menu buttons
        self.create_menu_buttons()  # Start with closed menu buttons

        # Button to expand/collapse menu
        self.menu_btn = tk.Button(self.menu_frame, text="☰",fg="#ffffff", command=self.toggle_menu)
        self.menu_btn.place(x=7, y=7, width=32, height=32)

    def create_menu_buttons(self):
        self.menu_buttons = []
        button_func = self.create_menu_buttons_expanded if self.menu_expanded else self.create_menu_buttons_closed
        button_func()

    def create_menu_buttons_closed(self):
        for i, (icon_path, button_text) in enumerate(self.button_info):
            button_icon = self.resize_image(icon_path, 32, 32)
            button = tk.Button(self.menu_frame, image=button_icon,fg="#ffffff",
                               command=lambda text=button_text: self.show_info(text))
            button.image = button_icon
            button.place(x=7, y=(i + 1) * 40 + 10, width=32, height=32, anchor="nw")
            self.menu_buttons.append(button)

    def create_menu_buttons_expanded(self):
        for i, (icon_path, button_text) in enumerate(self.button_info):
            button_icon = self.resize_image(icon_path, 32, 32)
            button = tk.Button(self.menu_frame, text=button_text, fg="#ffffff", compound=tk.LEFT,
                               image=button_icon, command=lambda text=button_text: self.show_info(text))
            button.image = button_icon
            button.place(x=7, y=(i + 1) * 40 + 10, width=80, height=32, anchor="nw")
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
