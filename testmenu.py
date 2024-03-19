import tkinter as tk

def toggle_menu():
    if menu_frame.winfo_ismapped():
        menu_frame.grid_remove()
    else:
        menu_frame.grid(row=1, column=0, sticky="ew")

def option_selected(option):
    print("Option selected:", option)
    # 在這裡執行您希望的操作

# 創建主視窗
root = tk.Tk()
root.title("Dynamic Collapsible Menu")

# 創建主要框架
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# 創建選單按鈕
menu_button = tk.Button(main_frame, text="Menu", command=toggle_menu)
menu_button.grid(row=0, column=0)

# 創建選單框架
menu_frame = tk.Frame(main_frame)

# 創建選項按鈕
options = ["Option 1", "Option 2", "Option 3"]  # 可以根據需要添加更多選項
for i, option in enumerate(options):
    option_button = tk.Button(menu_frame, text=option, command=lambda opt=option: option_selected(opt))
    option_button.grid(row=i, column=0, sticky="ew")

root.mainloop()
