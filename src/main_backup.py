'''
Version:v0.2
author:xy
'''

import sys, os
# 根目录
rel_path = os.path.abspath('.')
sys.path.append(rel_path)

import tkinter, tkinter.messagebox
from datetime import datetime

time_now_msg = datetime.now()
time_now = time_now_msg.strftime("%Y{y}%m{m}%d").format(y='-', m='-')

# 用例文件夹
case_path_dir = os.path.abspath(r'.\testCase')
# 报告文件夹
report_path_dir = os.path.abspath(r'.\testCase_report')
# 用例与报告运行文件夹
caseRun_path_dir = os.path.abspath(r'.\testCase_run')

def __wr_erro():
    import traceback
    # 写入异常日志
    erro = traceback.format_exc()
    # erro_path = r'g:\git\log\{}_erro.txt'.format(time_now)
    erro_path = rel_path+r'\log\{}_erro.txt'.format(time_now)
    if os.path.exists(erro_path):
        # 错误日志已创建
        with open(erro_path,'a', encoding='utf-8') as f:
            f.write(erro)
            f.write('\r'+str(time_now_msg)+'\r'+'-------------------------\r')
    else:
        # 错误日志未创建
        with open(erro_path,'w', encoding='utf-8') as f:
            f.write(erro)
            f.write('\r'+str(time_now_msg)+'\r'+'-------------------------\r')

# 实例化窗口
master = tkinter.Tk()
master.title('大家好，这位是我老婆')

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

# 生成用例Run
def reCr_testCase_run(case_path_dir, report_path_dir):
    # 遍历获取用例文件夹
    files = []
    for a, b, c in os.walk(case_path_dir):
        files.append(str(a))
    run_text = []
    for i in files:
        # 生成报告文件夹名称
        report_name = str(i[len(case_path_dir)+1:-4:])
        if(report_name != ''):
            run_text.append(str(r'airtest run "{}" --device Android://127.0.0.1:5037/YLSKL7Z9HET47TJB --log {}\{}'.format(i, report_path_dir, report_name)))
    # 生成用例运行文件
    with open(caseRun_path_dir+r'\testCase.bat', 'w', encoding='utf-8') as f:
        for i in run_text:
            f.write(i + '\n')
bt_reCr_testCase_run = tkinter.Button(master, text='1.生成用例bat', command=lambda : reCr_testCase_run(case_path_dir, report_path_dir)).place(x=180, y=690)

# 运行用例
def op_testCase():
    os.startfile(rel_path+r'\testCase_run\go.bat')
bt_op_testCase = tkinter.Button(master, text='2.运行用例', command=op_testCase).place(x=330, y=690)

# 打开用例目录
def op_testCase_dir():
    os.startfile(case_path_dir)
bt_op_testCase_dir = tkinter.Button(master,text='打开用例目录', command=op_testCase_dir).place(x=480, y=690)

# 生成报告Run
def reCr_testRepo_run(case_path_dir, report_path_dir):
    files = []
    for a, b, c in os.walk(case_path_dir):
        files.append(str(a))
    repo_text = []
    for i in files:
        # 生成报告文件夹名称
        report_name = str(i[len(case_path_dir)+1:-4:])
        if(report_name != ''):
            repo_text.append(str(r'airtest report "{}" --log_root {}\{} --outfile {}\{}\log.html --lang zh'.format(i, report_path_dir, report_name, report_path_dir, report_name)))
    # 生成用例运行文件
    with open(caseRun_path_dir+r'\testRepo.bat', 'w', encoding='utf-8') as f:
        for i in repo_text:
            f.write(i + '\n')
bt_reCr_testRepo_run = tkinter.Button(master, text='3.生成报告bat', command=lambda : reCr_testRepo_run(case_path_dir, report_path_dir)).place(x=180, y=730)

# 生成报告
def creat_report():
    os.startfile(caseRun_path_dir+r'\re.bat')
bt_cr_report = tkinter.Button(master, text='4.生成报告', command=creat_report).place(x=330, y=730)

# 打开报告目录
def op_report_dir():
    os.startfile(report_path_dir)
bt_op_report = tkinter.Button(master, text='打开报告目录', command=op_report_dir).place(x=480, y=730)

# 清空报告目录
def del_report_dir(dir):
    import shutil
    shutil.rmtree(dir)
    os.mkdir(dir)
    tkinter.messagebox.showinfo(title='', message='清空完成')
bt_del_report_dir = tkinter.Button(master, text='清空报告目录', command=lambda : del_report_dir(report_path_dir)).place(x=630, y=730)

'''
# 创建报告目录
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
bt_cr_report_dir = tkinter.Button(master, text='创建报告目录', command=lambda : cr_report_dir(report_path_dir)).place(x=300, y=770)
'''

# 退出
bt_exit = tkinter.Button(master, text='退出', command=exit).place(x=180, y=770)

# 主窗口循环显示
master.mainloop()