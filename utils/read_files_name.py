import os

win_dir = r"E:\公司相关\产品素材"
current_dir = win_dir.replace('\\', '/')
temp = os.listdir(current_dir)
for i in temp:
    print(i)
print("===================================")
print("共", len(temp), "个文件")
