'''
Version:v0.2
author:xy
'''

import sys, os
rel_path = os.path.abspath('.')
sys.path.append(rel_path)

import tkinter, tkinter.messagebox
from datetime import datetime

time_now_msg = datetime.now()
time_now = time_now_msg.strftime("%Y{y}%m{m}%d").format(y='-', m='-')

def __wr_erro():
    import traceback
    # 写入异常日志
    erro = traceback.format_exc()
    # erro_path = r'g:\git\log\{}_erro.txt'.format(time_now)
    erro_path = rel_path+r'\log\{}_erro.txt'.format(time_now)
    if os.path.exists(erro_path):
        with open(erro_path,'a', encoding='utf-8') as f:
            f.write(erro)
            f.write('\r'+str(time_now_msg)+'\r'+'-------------------------\r')
    else:
        with open(erro_path,'w', encoding='utf-8') as f:
            f.write(erro)
            f.write('\r'+str(time_now_msg)+'\r'+'-------------------------\r')

# 实例化窗口
master = tkinter.Tk()
master.title()

# 窗口居中
pc_width = master.winfo_screenwidth()
pc_height = master.winfo_screenheight()
master_width = 970
master_height = 900
x = (pc_width-master_width) / 2
y = (pc_height-master_height) /2
master.geometry('%dx%d+%d+%d' %(master_width, master_height, x, y))

# 创建画布导入图片
canvas = tkinter.Canvas(master, height=685, width=970)
# zhizi.gif(img:970*685)
image_file = tkinter.PhotoImage(file=rel_path+r'\img\zhizi.gif')
image = canvas.create_image(485, 0, anchor='n', image=image_file)
canvas.pack()

# 运行用例
def op_testCase():
    os.startfile(rel_path+r'\testCase_run\go.bat')
bt_op_testCase = tkinter.Button(master, text='运行用例', command=op_testCase).place(x=300, y=690)

# 生成报告
def creat_report():
    os.startfile(rel_path+r'\testCase_run\re.bat')
bt_cr_report = tkinter.Button(master, text='生成报告', command=creat_report).place(x=300, y=730)

# 创建报告目录
cr_report_dir_name = rel_path+r'\testCase_report'
def cr_report_dir(dir):
    try:
        os.mkdir(dir)
        tkinter.messagebox.showinfo(title='', message='创建成功')
    except FileExistsError:
        __wr_erro()
        tkinter.messagebox.showerror(title='错误', message='文件夹已存在，无法重复创建')
    except FileNotFoundError:
        # 目录不存在，创建多级目录
        os.makedirs(dir_path+time_now)
        tkinter.messagebox.showinfo(title='', message='创建成功')
    except:
        __wr_erro()
        tkinter.messagebox.showerror(title='错误', message='创建文件夹失败，请联系管理员')
bt_cr_report_dir = tkinter.Button(master, text='创建报告目录', command=lambda : cr_report_dir(cr_report_dir_name)).place(x=300, y=770)

# 打开报告目录
def op_report_dir():
    os.startfile(rel_path+r'\testCase_report')
bt_op_report = tkinter.Button(master, text='打开报告目录', command=op_report_dir).place(x=300, y=810)

# 清空报告目录
del_report_dir_name = rel_path+r'\testCase_report'
def del_report_dir(dir):
    import shutil
    shutil.rmtree(dir)
    os.mkdir(dir)
    tkinter.messagebox.showinfo(title='', message='清空完成')
bt_del_report_dir = tkinter.Button(master, text='清空报告目录', command=lambda : del_report_dir(del_report_dir_name)).place(x=450, y=770)

# 退出
bt_exit = tkinter.Button(master, text='退出', command=exit).place(x=300, y=850)

# 主窗口循环显示
master.mainloop()