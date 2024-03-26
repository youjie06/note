import tkinter as tk
from tkinter import PhotoImage
from notecalendarFM import CalendarApp

class NoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Note")
        self.root.geometry("1200x768")
      
        
        # Menu Frame
        self.menu_frame = tk.Frame(self.root,bg="lightgray")
        self.menu_frame.place(relx=0, rely=0, relwidth=0.04, relheight=1)
        self.menu_btn=tk.Button(self.menu_frame)
        self.menu_btn.place(x=7,y=7,width=32,height=32)
        self.menu_btn_fm=tk.Frame(self.menu_frame,bg="lightgray",bd=0)
        self.menu_btn_fm.pack(pady=50)
        # Expandable menu buttons
        self.button1 = tk.Button(self.menu_btn_fm, text="Button 1", width=3, height=3)
        self.button1.grid(row=0, column=0)

        self.button2 = tk.Button(self.menu_btn_fm, text="Button 2", width=3, height=3)
        self.button2.grid(row=1, column=0)

        self.button3 = tk.Button(self.menu_btn_fm, text="Button 3", width=3, height=3)
        self.button3.grid(row=2, column=0)

        self.button4 = tk.Button(self.menu_btn_fm, text="Button 4", width=3, height=3)
        self.button4.grid(row=3, column=0)

        self.button5 = tk.Button(self.menu_btn_fm, text="Button 5", width=3, height=3)
        self.button5.grid(row=4, column=0)

        # Content Frame
        self.content_frame = tk.Frame(self.root,bd=1,bg="#ffffff")
        self.content_frame.place(relx=0.04, rely=0, relwidth=0.67, relheight=1)
        self.calendar_app = CalendarApp(self.content_frame)

        # Information Frame
        self.information_frame = tk.Frame(self.root, bg="lightgreen")
        self.information_frame.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

        # Expand/Collapse button for Information Frame
        # self.info_button = tk.Button(self.information_frame, text="Info", command=self.expand_collapse)
        # self.info_button.pack()

    # def expand_collapse(self):
    #     # Toggle visibility of Information Frame
    #     if self.information_frame.winfo_width() > 1:
    #         self.information_frame.place_forget()
    #     else:
    #         self.information_frame.place(relx=0.7, rely=0, relwidth=0.3, relheight=1)

if __name__ == "__main__":
    root = tk.Tk()
    app = NoteApp(root)
    root.mainloop()
