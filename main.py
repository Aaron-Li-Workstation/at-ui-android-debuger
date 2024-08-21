# -*- coding: UTF-8 -*-
#print("""
#Android UI Debugger
#
#Version:Alpha 0.0.1
#made by Aaron Li. 
#""")
#导库
from urllib import request
import tkinter
from tkinter import messagebox
import zipfile
import os
import subprocess
from tkinter import filedialog



#下载与环境准备
if os.path.isfile("./at-android-ui-debuger/tools.zip_files/platform-tools/adb.exe"):
    print("Path already installed.")
else:
    print("Downloading Platform Tools(https://googledownloads.cn/android/repository/platform-tools-latest-windows.zip)")
    file_name = "./at-android-ui-debuger/tools.zip"
    os.system("md at-android-ui-debuger")
    url = 'https://googledownloads.cn/android/repository/platform-tools-latest-windows.zip'
    request.urlretrieve(url,file_name)
    
    zip_file = zipfile.ZipFile(file_name)
    if os.path.isdir(file_name + "_files"):
        pass
    else:
        os.mkdir(file_name + "_files")
    for names in zip_file.namelist():
        zip_file.extract(names,file_name + "_files/")
    zip_file.close()

work = {"work-dict":".\\at-android-ui-debuger\\tools.zip_files","adb-path":".\\at-android-ui-debuger\\tools.zip_files\\platform-tools\\adb.exe"}
subprocess.run(str(work["adb-path"]+" start-server"))

#定义功能
def show_connected_devices():
    p = subprocess.Popen(str(work["adb-path"]+" devices"),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             encoding='gb2312'
                             )
    tkinter.messagebox.showinfo("查看已正确连接的Droid设备",p.communicate()[0])
def add_apk():
    path = filedialog.askopenfilename()
    if path != "":
        p = subprocess.Popen(str(work["adb-path"]+" install "+path),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             encoding='gb2312'
                             )
        tkinter.messagebox.showinfo("向Droid添加APK包",p.communicate()[0])
    else:
        tkinter.messagebox.showerror("向Droid添加APK包","操作取消")

def remove_apk():
    result = tkinter.simpledialog.askstring(title="向Droid移除APK包",prompt="请输入包名：")
    print(result)
    if result == "None":
        tkinter.messagebox.showerror("向Droid移除APK包","操作取消")
    else:
        p = subprocess.Popen(str(work["adb-path"]+" uninstall "+str(result)),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             encoding='gb2312'
                             )
        tkinter.messagebox.showinfo("向Droid移除APK包",p.communicate()[0])

def askname():
      result = tkinter.simpledialog.askstring(title = '信息',prompt='请输入：',initialvalue = '初始值')
      print(result)
    
#tkinter
tk = tkinter.Tk()
tk.geometry("600x400")
tk.title("Android可视化调试软件")

#添加控件
title_text = tkinter.Label(tk,text="Android可视化调试软件 主页",font=("宋体",33),fg="black").grid()
btn_show_devices = tkinter.Button(tk,text="查看以正确连接的Droid设备",width=60,font=("宋体",15),fg="grey",command=show_connected_devices).grid()
btn_add_apk = tkinter.Button(tk,text="向Droid添加APK包",width = 60,font=("宋体",15),fg="grey",command=add_apk).grid()
btn_remove = tkinter.Button(tk,text="向Droid移除包",width=60,font=("宋体",15),fg="grey",command=remove_apk).grid()

#进入循环
tk.mainloop()

subprocess.Popen("taskkill -f -im adb.exe",
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.STDOUT,
                             encoding='gb2312'
                             )
