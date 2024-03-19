import calendar
import tkinter as tk

class CalendarApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Calendar GUI")

        self.year = tk.IntVar()
        self.month = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):
        # 年份选择
        year_label = tk.Label(self.master, text="Year:")
        year_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.year_entry = tk.Entry(self.master, textvariable=self.year)
        self.year_entry.grid(row=0, column=1, padx=5, pady=5)

        # 月份选择
        month_label = tk.Label(self.master, text="Month:")
        month_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.month_entry = tk.Entry(self.master, textvariable=self.month)
        self.month_entry.grid(row=1, column=1, padx=5, pady=5)

        # 星期标签
        weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        for i, day in enumerate(weekdays):
            padx = 10 if i == 0 else 5
            label_frame = tk.Frame(self.master, padx=padx, pady=5)
            label_frame.grid(row=2, column=i+1)
            label = tk.Label(label_frame, text=day)
            label.pack()

        # 创建日历网格
        self.create_calendar_grid()

        # 显示日历按钮
        show_button = tk.Button(self.master, text="Show Calendar", command=self.show_calendar)
        show_button.grid(row=10, column=0, columnspan=8, padx=5, pady=10)

    def create_calendar_grid(self):
        self.cells = []
        for i in range(6):
            row_cells = []
            for j in range(7):
                cell_label = tk.Label(self.master, text="", relief="ridge", width=6, height=2, borderwidth=1)
                cell_label.grid(row=i + 3, column=j+1, padx=5, pady=5)
                row_cells.append(cell_label)
            self.cells.append(row_cells)

    def show_calendar(self):
        year = self.year.get()
        month = self.month.get()

        # 设置周日为每周的第一天
        calendar.setfirstweekday(calendar.SUNDAY)

        print("Year:", year)
        print("Month:", month)

        cal = calendar.monthcalendar(year, month)

        for i in range(6):
            for j in range(7):
                if len(cal) > i and len(cal[i]) > j and cal[i][j] != 0:
                    self.cells[i][j].config(text=cal[i][j])
                else:
                    self.cells[i][j].config(text="")



def main():
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
