import tkinter as tk    #pip install tk
from PIL import Image, ImageTk  #pip install pillow
from notecalendarFM import CalendarApp

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note")
        self.root.geometry("1200x768")
      
        
        # Default proportions for internal frames
        #self.default_proportions = {"menu": 1, "content": 6, "info": 3}
        
        # Menu Frame
        #self.menu_fm = tk.Frame(self.root, bg="lightgray")
        #self.menu_fm.place(x=0, y=0, width=50, height=768)
        self.openmenu_frame = tk.Frame(self.root, bg="lightgray")
        self.openmenu_frame.place(x=0, y=0, width=50, height=768)
        self.menu_btn = tk.Button(self.openmenu_frame, text="☰", command=self.toggle_menu)
        self.menu_btn.place(x=7, y=7, width=32, height=32)
        self.openbtn_fm = tk.Frame(self.openmenu_frame, bg="lightgray")
        self.openbtn_fm.place(x=7, y=50, width=50, height=768)
        self.closemenu_frame = tk.Frame(self.root, bg="lightgray")
        self.closemenu_frame.place(x=7, y=50, width=50, height=768)

        self.closebtn_fm = tk.Frame(self.closemenu_frame, bg="lightgray")
        self.closebtn_fm.place(x=7, y=50, width=50, height=768)

        self.menu_expanded = False
        
        # Load icons
        Calendar_icon = ImageTk.PhotoImage(Image.open("icon/calendar-day.png"), width=32, height=32)
        Text_icon = ImageTk.PhotoImage(Image.open("icon/calendar-pen.png"), width=32, height=32)
        Todo_icon = ImageTk.PhotoImage(Image.open("icon/alarm-clock.png"), width=32, height=32)
        
        #openbtn_fm
        Calendar_openbtn = tk.Button(self.openbtn_fm, image=Calendar_icon, compound=tk.LEFT, text="日曆", command=lambda: self.show_info("日曆"))
        Calendar_openbtn.place(x=7, y=7, width=32, height=32, anchor="nw")
        Text_openbtn = tk.Button(self.openbtn_fm, image=Text_icon, compound=tk.LEFT, text="備忘錄", command=lambda: self.show_info("備忘錄"))
        Text_openbtn.place(x=7, y=100, width=32, height=32, anchor="nw")
        Todo_openbtn = tk.Button(self.openbtn_fm, image=Todo_icon, compound=tk.LEFT, text="代辦事項", command=lambda: self.show_info("代辦事項"))
        Todo_openbtn.place(x=7, y=150, width=32, height=32, anchor="nw")

        #closebtn_fm
        Calendar_closebtn = tk.Button(self.closebtn_fm, image=Calendar_icon, command=lambda: self.show_info("日曆"))
        Calendar_closebtn.place(x=7, y=7, width=32, height=32, anchor="nw")
        Text_closebtn = tk.Button(self.closebtn_fm, image=Text_icon, command=lambda: self.show_info("備忘錄"))
        Text_closebtn.place(x=7, y=100, width=32, height=32, anchor="nw")
        Todo_closebtn = tk.Button(self.closebtn_fm, image=Todo_icon, command=lambda: self.show_info("代辦事項"))
        Todo_closebtn.place(x=7, y=150, width=32, height=32, anchor="nw")

        
        # Content Frame
        self.content_frame = tk.Frame(self.root, bd=1, bg="#ffffff")
        self.content_frame.place(x=50, y=0, width=850, height=768)
        self.calendar_app = CalendarApp(self.content_frame)

        # Information Frame
        self.information_frame = tk.Frame(self.root, bg="lightgreen")
        self.information_frame.place(x=900, y=0, width=300, height=768)

        

        
        # Initially hide menu buttons
        # self.menu_buttons = []
        # for i, button_text in enumerate(["日歷", "記事本", "備忘錄", "繪畫板"]):
        #     button = tk.Button(self.menu_frame,text=button_text,
        #         image=self.icons[button_text],  # Set image for the button
        #         compound=tk.LEFT,  # Align image and text
        #         command=lambda text=button_text: self.show_info(text)
        #     )
        #     button.place(x=7, y=(i + 1) * 40 + 10, width=32, height=32, anchor="nw")  # Adjust width for icon
        #     self.menu_buttons.append(button)

    def toggle_menu(self):
        if self.menu_expanded:
            # Restore default frame proportions
            self.closemenu_frame = tk.Frame(self.root, bg="lightgray")
            self.closemenu_frame.place(x=0, y=0, width=50, height=768)
            self.menu_btn = tk.Button(self.closemenu_frame, text="☰", command=self.toggle_menu)
            self.menu_btn.place(x=7, y=7, width=32, height=32)
            self.closebtn_fm = tk.Frame(self.closemenu_frame, bg="lightgray")
            self.closebtn_fm.place(x=7, y=20, width=50, height=768)
            self.content_frame.place(x=50, y=0, width=850, height=768)
            self.information_frame.place(x=900, y=0, width=300, height=768)
            # Load icons
            Calendar_icon = ImageTk.PhotoImage(Image.open("icon/calendar-day.png"))
            Text_icon = ImageTk.PhotoImage(Image.open("icon/calendar-pen.png"))
            Todo_icon = ImageTk.PhotoImage(Image.open("icon/alarm-clock.png"))
            #openbtn_fm
            Calendar_openbtn = tk.Button(self.openbtn_fm, image=Calendar_icon, compound=tk.LEFT, text="日曆", command=lambda: self.show_info("日曆"))
            Calendar_openbtn.place(x=7, y=50, width=32, height=32, anchor="nw")
            Text_openbtn = tk.Button(self.openbtn_fm, image=Text_icon, compound=tk.LEFT, text="備忘錄", command=lambda: self.show_info("備忘錄"))
            Text_openbtn.place(x=7, y=100, width=32, height=32, anchor="nw")
            Todo_openbtn = tk.Button(self.openbtn_fm, image=Todo_icon, compound=tk.LEFT, text="代辦事項", command=lambda: self.show_info("代辦事項"))
            Todo_openbtn.place(x=7, y=150, width=32, height=32, anchor="nw")

            self.menu_expanded = False
        else:
            # Adjust frame proportions
            self.openmenu_frame = tk.Frame(self.root, bg="lightgray")
            self.openmenu_frame.place(x=0, y=0, width=120, height=768)
            self.menu_btn = tk.Button(self.openmenu_frame, text="☰", command=self.toggle_menu)
            self.menu_btn.place(x=7, y=7, width=32, height=32)
            self.openbtn_fm = tk.Frame(self.openmenu_frame, bg="lightgray")
            self.openbtn_fm.place(x=7, y=20, width=50, height=768)
            self.content_frame.place(x=120, y=0, width=780, height=768)
            # Load icons
            Calendar_icon = ImageTk.PhotoImage(Image.open("icon/calendar-day.png"))
            Text_icon = ImageTk.PhotoImage(Image.open("icon/calendar-pen.png"))
            Todo_icon = ImageTk.PhotoImage(Image.open("icon/alarm-clock.png"))
            #closebtn_fm
            Calendar_closebtn = tk.Button(self.closebtn_fm, image=Calendar_icon, command=lambda: self.show_info("日曆"))
            Calendar_closebtn.place(x=7, y=50, width=32, height=32, anchor="nw")
            Text_closebtn = tk.Button(self.closebtn_fm, image=Text_icon, command=lambda: self.show_info("備忘錄"))
            Text_closebtn.place(x=7, y=100, width=32, height=32, anchor="nw")
            Todo_closebtn = tk.Button(self.closebtn_fm, image=Todo_icon, command=lambda: self.show_info("代辦事項"))
            Todo_closebtn.place(x=7, y=150, width=32, height=32, anchor="nw")
            #self.information_frame.place_forget()  # Hide information frame when menu is expanded
            self.menu_expanded = True

    def show_info(self, button_text):
        # You can implement the functionality to show detailed information based on the button clicked
        print(f"Button clicked: {button_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
