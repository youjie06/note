import calendar
import tkinter as tk
from datetime import datetime, timedelta

class CalendarFM:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent, bg="#3f4145")
        self.frame.pack(pady=40)
        
        # Get current date
        now = datetime.now()
        self.year = tk.IntVar(value=now.year)  # Initialize year variable, set to current year
        self.month = tk.IntVar(value=now.month)  # Initialize month variable, set to current month
        self.day = tk.IntVar(value=(now + timedelta(days=1)).day)  # Initialize date variable, set to tomorrow's date
        self.calendar_frame = None
        # Initialize interface
        self.create_widgets()

    def create_widgets(self):
        # Year and month layout
        year_month_frame = tk.Frame(self.frame, bg="#3f4145")
        year_month_frame.grid(row=0, column=0, columnspan=7, pady=(0, 10))

        # Year selection
        year_label = tk.Label(year_month_frame, text="Year:", font=(16), bg="#3f4145", fg="#ffffff")
        year_label.grid(row=0, column=0, padx=5, pady=5, sticky="ne")

        self.year_spinbox = tk.Spinbox(year_month_frame, from_=1900, to=2100, textvariable=self.year, command=self.update_calendar)
        self.year_spinbox.grid(row=0, column=1, padx=5, pady=5)

        # Month selection
        month_label = tk.Label(year_month_frame, text="Month:", font=(16), bg="#3f4145", fg="#ffffff")
        month_label.grid(row=0, column=2, padx=5, pady=5, sticky="ne")

        self.month_spinbox = tk.Spinbox(year_month_frame, from_=1, to=12, textvariable=self.month, command=self.update_calendar)
        self.month_spinbox.grid(row=0, column=3, padx=5, pady=5)

        # Create week label and date grid layout
        self.calendar_frame = tk.Frame(self.frame, bg="#3f4145")
        self.calendar_frame.grid(row=1, column=0, columnspan=7, sticky="n")
        
        # Create week label
        weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        for i, day in enumerate(weekdays):
            label = tk.Label(self.calendar_frame, text=day, bg="#3f4145", fg="#ffffff" ,font=('Helvetica', 12))
            label.grid(row=0, column=i, padx=0, pady=0)

        # Create date grid
        self.calendar_grid = []
        self.create_calendar_grid(self.calendar_frame)


    def create_calendar_grid(self, frame):
        # Clear existing date grid
        for row in self.calendar_grid:
            for label in row:
                label.destroy()
            self.calendar_grid.clear()

        # Get calendar for selected date
        year = self.year.get()
        month = self.month.get()
        cal = calendar.monthcalendar(year, month)
        mycalendar = [[0 for i in range(8)] for j in range(7)]
        for i,week in enumerate(cal):
            for j,day in enumerate(week):
                if day != 0:
                    weekday = (calendar.weekday(year, month, day) + 1) % 7
                    if weekday == 0:
                        i+=1
                        mycalendar[i][weekday] = day
                        break
                    else:          
                        mycalendar[i][weekday] = day

        cnt = 0                
        for i in range(7):
            for j in range(7):
                if mycalendar[i][j] == 0:
                    cnt+=1
            mycalendar[i][7]=cnt
            cnt=0
            if mycalendar[0][7] == 7:
                 del mycalendar[0]
                 mycalendar.append([0] * len(mycalendar[0]))
                 
            
        for i in range(6):
            row_labels = []  # Initialize list of labels for each row
            for j in range(7):
                if mycalendar[i][j] != 0:
                    cell_label = tk.Button(frame, text=mycalendar[i][j], bg="#3f4145", fg="#ffffff", activebackground="#4c4e52", activeforeground="#ffffff", relief="ridge", width=10, height=5, bd=1,font=('Helvetica', 12))
                    cell_label.grid(row=i+1, column=j, padx=0, pady=0)
                    row_labels.append(cell_label)
                else:
                    if mycalendar[i][7]!=7:
                        cell_label = tk.Button(frame, text="", bg="#3f4145", fg="#ffffff", activebackground="#4c4e52", activeforeground="#ffffff", relief="ridge", width=10, height=5, bd=1,font=('Helvetica', 12))
                        cell_label.grid(row=i+1, column=j, padx=0, pady=0)
                        row_labels.append(cell_label)
                j+=1
            i+=1
            
        self.calendar_grid.append(row_labels)


    def update_calendar(self):  # Update date grid
        for row in self.calendar_grid:
            for button in row:
                button.destroy()

        # Create week label
        weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
        for i, day in enumerate(weekdays):
            label = tk.Label(self.calendar_frame, text=day, bg="#3f4145", fg="#ffffff",font=('Helvetica', 12))
            label.grid(row=0, column=i, padx=0, pady=0)

        # Create date grid
        self.calendar_grid = []
        calendar_frame = self.calendar_frame
        self.create_calendar_grid(calendar_frame)
        calendar_frame.grid(row=1, column=0, columnspan=7)
