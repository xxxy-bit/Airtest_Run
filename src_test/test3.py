import traceback, os
from datetime import datetime
import tkinter

time_now_msg = datetime.now()
time_now = time_now_msg.strftime("%Y{y}%m{m}%d").format(y='-', m='-')

def err_test():
    # 写入异常日志
    erro = traceback.format_exc()
    # erro_path = r'g:\git\log\{}_erro.txt'.format(time_now)
    erro_path = r'log\{}_erro.txt'.format(time_now)
    if os.path.exists(erro_path):
        with open(erro_path,'a', encoding='utf-8') as f:
            f.write(erro)
            f.write('\r'+str(time_now_msg)+'\r'+'-------------------------\r')
    else:
        with open(erro_path,'w', encoding='utf-8') as f:
            f.write(erro)
            f.write('\r'+str(time_now_msg)+'\r'+'-------------------------\r')    

# a = os.path.exists(r'C:\Users\Administrator\Desktop\测试数据表\test\b')
# print(a)
# with open(r'log/11.txt', 'w', encoding='utf-8') as f:
#     f.write('aaaa')
# os.makedirs(r'log\b')
