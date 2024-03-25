import random
import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', 'sbsbsb!') \
            if flag else ('blue', '你是sb!')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        x = abs(random.randint(0,top.winfo_screenwidth()) - 700)
        y = abs(random.randint(0,top.winfo_screenheight()) - 400)

        top.geometry(f"320x200+{x}+{y}")
        # if tkinter.messagebox.askokcancel('温馨提示', '确定要退出吗?'):
        #     top.geometry(f"480x320+{x}+{y}")
        #     # top.quit()

    # 创建顶层窗口
    top = tkinter.Tk()
    # 设置窗口大小
    top.geometry('320x200')
    # 设置窗口标题
    top.title('Test')
    # 创建标签对象并添加到顶层窗口
    label = tkinter.Label(top, text='Hello, world!', font='Arial -32', fg='red')
    label.pack(expand=1)
    # 创建一个装按钮的容器
    panel = tkinter.Frame(top)
    # 创建按钮对象 指定添加到哪个容器中 通过command参数绑定事件回调函数
    button1 = tkinter.Button(panel, text='点击', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)

    # top.withdraw()
    button2.pack(side='right')
    panel.pack(side='bottom')
    # 开启主事件循环
    tkinter.mainloop()


if __name__ == '__main__':
    main()
