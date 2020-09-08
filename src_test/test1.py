import tkinter


# window = tk.Tk()

class tkCreat(object):
    # 初始化窗口名称和大小
    def __init__(self, master, title, size):
        # global window
        master.title(title)
        master.geometry(size)

    def aa(self, master):
        # global window
        canvas = tk.Canvas(master,height=700,width=1000,bg='green')
        # img:970*685
        image_file = tk.PhotoImage(file=r'g:\git\img\zhizi.gif')
        canvas.create_image(500,0,anchor='n',image=image_file)
        canvas.pack()
        # window.mainloop()
        # self.startWindow()
    
    def addButton(self, master, text, command):
        button = tk.Button(master, text=text, command=command)
        button.pack()

    # 开始运行
    # def startWindow(self):
    #     global window
    #     window.mainloop()

def test1():
    print('aaa')

if __name__ == "__main__":
    # master = tkCreat('111', '1080x900')
    # master.addButton('but',test1)
    # master.aa()
    # master.startWindow()

    ms = tk.Tk()
    t = tkCreat(ms, 'haha', '1080x900')
    t.aa(t)
    ms.mainloop()