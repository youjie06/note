import calendar  # 導入calendar模塊，用於處理日曆相關功能
import tkinter as tk  # 導入tkinter模塊，用於構建GUI介面
from datetime import datetime, timedelta  # 導入datetime模塊，用於處理日期和時間

class CalendarFM:
    def __init__(self, parent):
        self.parent = parent
        self.frame = tk.Frame(self.parent, bg="#3f4145", padx=20, pady=20)
        self.frame.place(width=850, height=768)
        # self.master = master  # 設置主視窗
        # self.master.title("Calendar GUI")  # 設置主視窗標題
        # self.master.configure(bg="white")  # 設置主視窗背景顏色為白色
        
        # 獲取當前日期
        now = datetime.now()
        self.year = tk.IntVar(value=now.year)  # 初始化年份變數，設置為當前年份
        self.month = tk.IntVar(value=now.month)  # 初始化月份變數，設置為當前月份
        self.day = tk.IntVar(value=(now + timedelta(days=1)).day)  # 初始化日期變數，設置為明天的日期
        self.calendar_frame = None
        # 初始化介面
        self.create_widgets()

    def create_widgets(self):
        # 年份和月份布局
        year_month_frame = tk.Frame(self.frame, bg="#3f4145")  # 在主框架中創建一個白色背景的子框架
        year_month_frame.grid(row=0, column=0, columnspan=7, pady=(0, 10))  # 將子框架放置到主框架中，設置在第一行，跨越7列，設置上邊距

        # 年份選擇
        year_label = tk.Label(year_month_frame, text="Year:", bg="#3f4145", fg="#ffffff")  # 在年份和月份框架中創建一個白色背景的標籤，顯示"Year:"
        year_label.grid(row=0, column=0, padx=5, pady=5, sticky="ne")  # 將年份標籤放置到年份和月份框架中，設置在第一行第一列，設置左右邊距，設置上下邊距，設置靠右對齊

        self.year_spinbox = tk.Spinbox(year_month_frame, from_=1900, to=2100, textvariable=self.year, command=self.update_calendar)  # 在年份和月份框架中創建一個可選擇年份的控件，設置可選擇的年份範圍為1900年至2100年，並綁定年份變數，設置選擇年份後的回調函數為update_calendar
        self.year_spinbox.grid(row=0, column=1, padx=5, pady=5)  # 將年份控件放置到年份和月份框架中，設置在第一行第二列，設置左右邊距，設置上下邊距

        # 月份選擇
        month_label = tk.Label(year_month_frame, text="Month:", bg="#3f4145", fg="#ffffff")  # 在年份和月份框架中創建一個白色背景的標籤，顯示"Month:"
        month_label.grid(row=0, column=2, padx=5, pady=5, sticky="ne")  # 將月份標籤放置到年份和月份框架中，設置在第一行第三列，設置左右邊距，設置上下邊距，設置靠右對齊

        self.month_spinbox = tk.Spinbox(year_month_frame, from_=1, to=12, textvariable=self.month, command=self.update_calendar)  # 在年份和月份框架中創建一個可選擇月份的控件，設置可選擇的月份範圍為1月至12月，並綁定月份變數，設置選擇月份後的回調函數為update_calendar
        self.month_spinbox.grid(row=0, column=3, padx=5, pady=5)  # 將月份控件放置到年份和月份框架中，設置在第一行第四列，設置左右邊距，設置上下邊距

        # 創建星期標籤和日期網格的佈局
        self.calendar_frame = tk.Frame(self.frame, bg="#3f4145")  # 在主框架中創建一個白色背景的
        self.calendar_frame.grid(row=1, column=0, columnspan=7, sticky="n")  # 將日曆框架放置到主框架中，跨越7列，並填滿水平方向和垂直方向

        # 創建星期標籤
        weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']  # 定義星期的標籤列表
        for i, day in enumerate(weekdays):  # 遍歷星期標籤列表
            label = tk.Label(self.calendar_frame, text=day, bg="#3f4145", fg="#ffffff")  # 創建一個白色背景的標籤，顯示星期名稱
            label.grid(row=0, column=i, padx=0, pady=0)  # 將星期標籤放置到日曆框架中，設置在第一行，第i列，設置左右邊距，設置上下邊距

        # 創建日期網格
        self.calendar_grid = []  # 初始化日期網格列表
        self.create_calendar_grid(self.calendar_frame)  # 創建日期網格


    def create_calendar_grid(self, frame):
        # 清除原有的日期網格
        for row in self.calendar_grid:
            for label in row:
                label.destroy()  # 銷毀日期網格中的所有標籤
            self.calendar_grid.clear()  # 清空日期網格列表

        # 獲取所選日期的月曆
        year = self.year.get()  # 獲取選擇的年份
        month = self.month.get()  # 獲取選擇的月份
        cal = calendar.monthcalendar(year, month)  # 獲取指定年份和月份的月曆列表
        
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
            if mycalendar[0][7] == 7:#當0*7格是7時
                 del mycalendar[0]#刪除第零列
                 mycalendar.append([0] * len(mycalendar[0]))#在最後一列新增八個值為零
                 
            #print(mycalendar)     
            
        for i in range(6):
            row_labels = []  # 初始化每行的標籤列表
            for j in range(7):
                if mycalendar[i][j] != 0:#列內的有效日期不等於零
                    cell_label = tk.Button(frame, text=mycalendar[i][j], bg="#3f4145", fg="#ffffff", activebackground="#4c4e52", activeforeground="#ffffff", relief="ridge", width=6, height=2, bd=1)  # 創建一個白色背景的標籤，顯示該日期，設置邊框樣式
                    cell_label.grid(row=i+1, column=j, padx=0, pady=0)  # 將日期標籤放置到日曆框架中的指定位置，設置左右邊距，設置上下邊距
                    row_labels.append(cell_label)  # 將日期標籤添加到該行的標籤列表中
                else:#列內的有效日期日期等於零
                    if mycalendar[i][7]!=7:#列內的有效日期不等於七
                        cell_label = tk.Button(frame, text="", bg="#3f4145", fg="#ffffff", activebackground="#4c4e52", activeforeground="#ffffff", relief="ridge", width=6, height=2, bd=1)  # 創建一個白色背景的標籤，不顯示任何內容，設置邊框樣式
                        cell_label.grid(row=i+1, column=j, padx=0, pady=0)  # 將日期標籤放置到日曆框架中的指定位置，設置左右邊距，設置上下邊距
                        row_labels.append(cell_label)  # 將日期標籤添加到該行的標籤列表中
                j+=1
            i+=1
            
        self.calendar_grid.append(row_labels)  # 將該行的標籤列表添加到日期網格列表中
        # 顯示月曆

    def update_calendar(self):  # 更新日期網格
        for row in self.calendar_grid:  # 遍歷日期網格列表的每一行
            for button in row:  # 遍歷每一行中的標籤
                button.destroy()

        # 創建星期標籤
        weekdays = ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']  # 定義一個星期列表
        for i, day in enumerate(weekdays):
            label = tk.Label(self.calendar_frame, text=day, bg="#3f4145", fg="#ffffff")  # 在日曆框架中創建一個白色背景的標籤，顯示星期名稱
            label.grid(row=0, column=i, padx=0, pady=0)  # 將星期標籤放置到日曆框架中，設置在第一行，依次排列，設置左右邊距，設置上下邊距

        # 創建日期網格
        self.calendar_grid = []  # 初始化日期網格列表
        calendar_frame = self.calendar_frame  # 獲取日曆框架
        self.create_calendar_grid(calendar_frame)  # 創建日期網格，並放置到日曆框架中
        calendar_frame.grid(row=1, column=0, columnspan=7)  # 將日曆框架放置到主框架中，設置在第二行，跨越7列self.frame.pack(fill=tk.BOTH, expand=True)