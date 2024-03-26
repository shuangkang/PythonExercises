import tkinter
import tkinter.messagebox


def main():
    flag = True

    # 修改标签上的文字
    def change_label_text():
        nonlocal flag
        flag = not flag
        color, msg = ('red', '炉石传说') \
            if flag else ('blue', '第八名')
        label.config(text=msg, fg=color)

    # 确认退出
    def confirm_to_quit():
        if tkinter.messagebox.askokcancel('提示', '要走吗'):
            top.quit()
    def cnm():
        if tkinter.messagebox.askokcancel('挨骂', '臭傻逼'):
            top.quit()


    top = tkinter.Tk()
    #窗口大小
    top.geometry('400x200')
    #主题
    top.title('小游戏')
    label = tkinter.Label(top, text='欢迎来到酒馆!', font='Arial -32', fg='blue')
    label.pack(expand=1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='修改', command=change_label_text)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='退出', command=confirm_to_quit)
    button2.pack(side='right')
    button3 = tkinter.Button(panel, text='挨骂', command=cnm)
    button3.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main()