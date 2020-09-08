import tkinter as tk

# 第一步，实例化object，建立窗口window
window = tk.Tk()

# 第二步，给窗口的可视化命名
window.title('My Window')

# 第三步，设定窗口大小（长*宽）
window.geometry('500x300')

# 第四步，在图形界面上设定标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
l = tk.Label(window, textvariable=var, bg='green', font=('Arial', 12), width=30, height=2)
# 说明：bg背景，font字体，width长，height高；长和高是字符的长和高，height=2就是标签有2个字符这么高

# 第五步，放置标签
l.pack()    # label内容content区域放置位置，自动调节尺寸
# 放置label的方法有：1、l.pack()    2、l.place()

# 定义函数，供button使用
on_hit = False
def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
        print(var.get())
    else:
        on_hit = False
        var.set('')
        print(var)

b = tk.Button(window,text='him me', command=hit_me)
b.pack()

# 第六步，主窗口循环提示
window.mainloop()
# 注意，loop因为是循环的意思，window.mainloop就会让window不断的刷新，如果没有mainloop,就是一个静态的window,传入进去的值就不会有循环，mainloop就相当于一个很大的while循环，有个while，每点击一次就会更新一次，所以我们必须要有循环
# 所有的窗口文件都必须有类似的mainloop函数，mainloop是窗口文件的关键的关键。