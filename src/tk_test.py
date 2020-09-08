import tkinter as tk

window = tk.Tk()
class tkCreat(object):
    # 初始化窗口名称和大小
    def __init__(self,title,size):
        global window
        window.title(title)
        window.geometry(size)

    # 创建画布图片
    def addCanvas(self,width,height,img_file):
        global window
        canvas = tk.Canvas(window, width=width, height=height, bg='green')

        # image_file = tk.PhotoImage(file=img_file)
        # canvas.create_image(500, 0, anchor='n', image=image_file)

        image_file = tk.PhotoImage(file=img_file)
        canvas.create_image(500,0,anchor='nw',image=image_file)

        canvas.pack()

    # 开始运行
    def startWindow(self):
        global window
        window.mainloop()

    def addButton(self,text,command):
        button = tk.Button(window, text=text, command=command)
        button.pack()

    def addLabel(self):
        pass

if __name__ == "__main__":
    tkc = tkCreat('你编程是真的6','1280x860')
    # tkc.addCanvas(1000,800,r'g:\git\img\zhizi.gif')
    tkc.addCanvas(1000, 700, r'g:\git\img\zhizi.gif')
    # tkc.addButton('测试',test1)
    # tkc.addButton('退出',exit)
    tkc.startWindow()
    # t = ts()
    # t.aa()