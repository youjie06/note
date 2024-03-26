import tkinter as tk
from notecalendarFM import CalendarApp

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note")
        self.root.geometry("1200x768")

        # Default proportions for internal frames
        self.default_proportions = {"menu": 1, "content": 6, "info": 3}
        
        # Menu Frame
        self.menu_frame = tk.Frame(self.root, bg="lightgray")
        self.menu_frame.place(x=0, y=0, width=50, height=768)

        # Button to expand/collapse menu
        self.menu_expanded = False
        self.menu_btn = tk.Button(self.menu_frame, text="☰", command=self.toggle_menu)
        self.menu_btn.place(x=7, y=7, width=32, height=32)

        # Content Frame
        self.content_frame = tk.Frame(self.root, bd=1, bg="#ffffff")
        self.content_frame.place(x=50, y=0, width=850, height=768)

        # Information Frame
        self.information_frame = tk.Frame(self.root, bg="lightgreen")
        self.information_frame.place(x=900, y=0, width=300, height=768)

        # Initially hide menu buttons
        self.menu_buttons = []
        for i, button_text in enumerate(["日歷", "記事本", "備忘錄", "繪畫板"]):
            button = tk.Button(self.menu_frame, text=button_text, command=lambda text=button_text: self.show_info(text))
            button.place(x=7, y=(i + 1) * 40, width=32, height=32, anchor="nw")
            self.menu_buttons.append(button)

    def toggle_menu(self):
        if self.menu_expanded:
            # Hide menu buttons
            for button in self.menu_buttons:
                button.place_forget()
                button.place(x=7, y=self.menu_buttons.index(button) * 40 + 40, width=32, height=32)
            # Restore default frame proportions
            self.menu_frame.place(x=0, y=0, width=50, height=768)
            self.content_frame.place(x=50, y=0, width=850, height=768)
            self.information_frame.place(x=900, y=0, width=300, height=768)
            self.menu_expanded = False
        else:
            # Show menu buttons
            for button in self.menu_buttons:
                button.place(x=7, y=self.menu_buttons.index(button) * 40 + 40, width=60, height=32)
            # Adjust frame proportions
            self.menu_frame.place(x=0, y=0, width=120, height=768)
            self.content_frame.place(x=120, y=0, width=780, height=768)
            #self.information_frame.place_forget()  # Hide information frame when menu is expanded
            self.menu_expanded = True

    def show_info(self, button_text):
        # You can implement the functionality to show detailed information based on the button clicked
        print(f"Button clicked: {button_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
