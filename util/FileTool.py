from datetime import datetime
import os,sys

time_now_msg = datetime.now()
time_now = time_now_msg.strftime("%Y{y}%m{m}%d").format(y='-', m='-')


class FileTool:
    def __init__(self):
        pass
        
    # def __wr_erro(self):
    #     import traceback
    #     # 写入异常日志
    #     erro = traceback.format_exc()
    #     erro_path = r'g:\git\log\{}_erro.txt'.format(time_now)
    #     if os.path.exists(erro_path):
    #         with open(erro_path,'a', encoding='utf-8') as f:
    #             f.write(erro)
    #             f.write('\r'+str(time_now_msg)+'\r'+'-------------------------\r')
    #     else:
    #         with open(erro_path,'w', encoding='utf-8') as f:
    #             f.write(erro)
    #             f.write('\r'+str(time_now_msg)+'\r'+'-------------------------\r')    

    def del_dir_shutil(self,dir_path):
        import shutil
        # 此方法可以直接删除非空文件夹，无法在回收站找回
        shutil.rmtree(dir_path)

    def del_dir_os(self,dir_path):
        # 删除文件夹
        os.remove(dir_path)

    def del_file(self,fil_path):
        # 删除文件
        if not os.path.exists(fil_path):
            print("文件不存在或已删除")
        else:
            os.remove(fil_path)

    def creat_file(self,fil_path):
        # 创建文件，判断是否存在
        if os.path.exists(fil_path):
            y = input('文件已存在，是否覆盖为空文件(y/n):')
            if y == 'y':
                open(fil_path, 'w')
                print('覆盖成功')
            elif y == 'n':
                pass
            else:
                print('请输入y或n')
        else:
            open(fil_path,"w")

    # def creat_dir(self,dir_path):
    #     # 创建文件夹
    #     try:
    #         os.mkdir(dir_path+time_now)
    #     except FileExistsError:
    #         # 文件夹已存在
    #         self.__wr_erro()
    #         print("文件夹已存在，无法重复创建")
    #     except FileNotFoundError:
    #         # 目录不存在，创建多级目录
    #         os.makedirs(dir_path+time_now)
        # except :
        #     # 其他异常
        #     self.__wr_erro()

if __name__ == "__main__":
    dir_path = 'C:/Users/Administrator/Desktop/测试数据表/test/aa'
    dir_path2 = 'C:/Users/Administrator/Desktop/测试数据表/test/bb'
    fil_path = 'C:/Users/Administrator/Desktop/测试数据表/test/aa.txt'
    fil_path2 = 'C:/Users/Administrator/Desktop/测试数据表/test/bb.txt'
    path = 'C:/Users/Administrator/Desktop/测试数据表/test/1/'

    # creat_file(fil_path)
    # del_file(fil_path)
    # del_dir_shutil
    # print(os.path.exists(fil_path))
    # a = datetime.date(2020,8,25)
    # ft = FileTool()
    # ft.creat_report()
    # ft.creat_dir(path)
    # ft.creat_file('C:/Users/Administrator/Desktop/测试数据表/test/aa.txt')
    # os.mkdir("C:/Users/Administrator/Desktop/测试数据表/test/2020年08月25日")

    sys.path.append('g:\\git\\util')
    print(sys.path)