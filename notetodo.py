import tkinter
import random
import datetime
import time
from threading import Thread
from tkcalendar import DateEntry

root = tkinter.Tk()
root.configure(bg="#F0F0F0")
root.title("待辦事項")
root.geometry("800x600")

tasks = []
reminders = []

# Function to update the listbox with tasks
def update_listbox():
    clear_listbox()
    for task in tasks:
        lb_tasks.insert("end", task)

# Function to clear the listbox
def clear_listbox():
    lb_tasks.delete(0, "end")

# Function to add a task
def add_task():
    task = txt_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        lbl_display["text"] = "不能輸入空白"
    txt_input.delete(0, "end")

# Function to delete all tasks
def del_all_tasks():
    global tasks
    tasks = []
    update_listbox()

# Function to delete a selected task
def delete_one_task():
    task = lb_tasks.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()

# Function to set a reminder for a selected task
def set_reminder():
    task = lb_tasks.get("active")
    if task in tasks:
        reminder_time_str = f"{cal.get_date()} {hour_spinbox.get()}:{minute_spinbox.get()}:{second_spinbox.get()} {ampm_combobox.get()}"
        try:
            reminder_time = datetime.datetime.strptime(reminder_time_str, "%Y-%m-%d %I:%M:%S %p")
        except ValueError:
            lbl_display["text"] = "提醒時間格式不正確，請按照 YYYY-MM-DD hh:mm:ss AM/PM 格式輸入。"
            return
        current_time = datetime.datetime.now()
        if reminder_time <= current_time:
            lbl_display["text"] = "提醒時間必須晚於當前時間。"
            return
        reminders.append((reminder_time, task))
        lbl_display["text"] = "提醒設定成功！"
        lbl_display.config(bg="red", fg="white")  # 更改提示欄位顏色為紅底白字
        print(f"提醒時間設定 '{task}' at {reminder_time.strftime('%Y-%m-%d %I:%M:%S %p')}")
        # Start a new thread to monitor reminders
        thread = Thread(target=check_reminders)
        thread.start()

# Function to cancel reminder for a selected task
def cancel_reminder():
    task = lb_tasks.get("active")
    for reminder in reminders:
        reminder_time, reminder_task = reminder
        if reminder_task == task:
            reminders.remove(reminder)
            lbl_display["text"] = f"已取消 '{task}' 的提醒"
            lbl_display.config(bg="red", fg="white")  # 更改提示欄位顏色為紅底白字
            print(f"已取消 '{task}' 的提醒")
            break

# Function to check reminders
def check_reminders():
    while True:
        current_time = datetime.datetime.now()
        for reminder in reminders:
            reminder_time, task = reminder
            if current_time >= reminder_time:
                lbl_display["text"] = f"注意事項 '{task}'!"
                lbl_display.config(bg="red", fg="white")  # 更改提示欄位顏色為紅底白字
                print(f"注意事項 '{task}'!")
                reminders.remove(reminder)
        time.sleep(1)

# Function to close the application
def exit():
    root.destroy()

# Frame for the input section
input_frame = tkinter.Frame(root, bg="#F0F0F0")
input_frame.pack(pady=10, padx=10, fill="x")

# Entry field to add tasks
txt_input = tkinter.Entry(input_frame, width=30)
txt_input.pack(side="left", padx=5)

# Button to add tasks
btn_add_task = tkinter.Button(input_frame, text="增加待辦事項", fg="white", bg="#6CAE75", command=add_task)
btn_add_task.pack(side="left", padx=5)

# Button to delete all tasks
btn_del_all = tkinter.Button(input_frame, text="刪除全部", fg="white", bg="#EF5350", command=del_all_tasks)
btn_del_all.pack(side="left", padx=5)

# Frame for time selection
time_frame = tkinter.Frame(root, bg="#F0F0F0")
time_frame.pack(pady=5, padx=10, fill="x")

# Labels and Spinboxes for time selection
tkinter.Label(time_frame, text="時間:", bg="#F0F0F0").pack(side="left")
hour_spinbox = tkinter.Spinbox(time_frame, from_=1, to=12, width=2)
hour_spinbox.pack(side="left", padx=5)
hour_spinbox.delete(0, 'end')
hour_spinbox.insert(0, datetime.datetime.now().strftime("%I"))
tkinter.Label(time_frame, text=":", bg="#F0F0F0").pack(side="left")
minute_spinbox = tkinter.Spinbox(time_frame, from_=0, to=59, width=2)
minute_spinbox.pack(side="left", padx=5)
minute_spinbox.delete(0, 'end')
minute_spinbox.insert(0, datetime.datetime.now().strftime("%M"))
tkinter.Label(time_frame, text=":", bg="#F0F0F0").pack(side="left")
second_spinbox = tkinter.Spinbox(time_frame, from_=0, to=59, width=2)
second_spinbox.pack(side="left", padx=5)
second_spinbox.delete(0, 'end')
second_spinbox.insert(0, datetime.datetime.now().strftime("%S"))
ampm_combobox = tkinter.StringVar(root)
ampm_combobox.set(datetime.datetime.now().strftime("%p"))
ampm_optionmenu = tkinter.OptionMenu(time_frame, ampm_combobox, "AM", "PM")
ampm_optionmenu.pack(side="left", padx=5)

# DateEntry for selecting date
cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2, year=2024)
cal.pack(padx=10, pady=10)

# Button to set reminder
btn_reminder = tkinter.Button(root, text="設定提醒", fg="white", bg="#6CAE75", command=set_reminder)
btn_reminder.pack(pady=5, padx=10, fill="x")

# Button to cancel reminder
btn_cancel_reminder = tkinter.Button(root, text="取消提醒", fg="white", bg="#EF5350", command=cancel_reminder)
btn_cancel_reminder.pack(pady=5, padx=10, fill="x")

# Listbox to display tasks
lb_tasks = tkinter.Listbox(root, width=60, height=15)
lb_tasks.pack(pady=10, padx=10, fill="both", expand=True)

# Button to delete a selected task
btn_delete_one = tkinter.Button(root, text="刪除選定事項", fg="white", bg="#EF5350", command=delete_one_task)
btn_delete_one.pack(pady=5, padx=10, fill="x")

# Label to display reminders
lbl_display = tkinter.Label(root, text="", bg="red", fg="white", font=("Arial", 16))  # 更改文字顏色為白字
lbl_display.pack(pady=5, fill="x")

# Button to exit the application
btn_exit = tkinter.Button(root, text="關閉", fg="white", bg="#546E7A", command=exit)
btn_exit.pack(pady=5, padx=10, fill="x")

root.mainloop()
