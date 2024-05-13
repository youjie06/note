import os
import shutil
import subprocess

# 1. 要打包的程式文件
source_files = ["notecalendarFM.py", "notetextFM.py", "notetodoFM.py", "tasks.txt"]

# 2. 設置 pyinstaller 參數
options = [
    "--onefile",             # 打包為單一執行檔
    "--noconsole",           # 不顯示命令提示視窗
]

# 3. 創建暫存目錄
temp_dir = "temp"
if os.path.exists(temp_dir):
    shutil.rmtree(temp_dir)
os.makedirs(temp_dir)

# 4. 複製程式文件到暫存目錄
for file in source_files:
    shutil.copy(file, temp_dir)

# 5. 執行 pyinstaller 打包
subprocess.run(["pyinstaller"] + options + [f"--distpath={os.path.join(os.getcwd(), 'dist')}"] + [os.path.join(temp_dir, "notecalendarFM.py")])

# 6. 刪除暫存目錄
shutil.rmtree(temp_dir)

print("打包完成")