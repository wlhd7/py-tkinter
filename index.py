import tkinter as tk

'''创建窗口'''
root = tk.Tk()

'''设置窗口标题'''
root.title('my_gui')

'''开启窗口/主循环'''
root.mainloop()

'''设置窗口大小为宽300，高200'''
root.geometry('300x200')

'''获取显示器分辨率'''
display_resolution = root.maxsize()

'''窗口锁定缩放'''
root.resizable(width:False, height:False)

'''设置窗口图标'''
root.iconbitmap('u.ico')

'''设置窗口背景颜色'''
root.configure(bg='yellow')
root.configure(bg='#000000')

'''设置窗口透明都'''
root.attributes('-alpha', 1)  # 1 - 不透明, 0 - 全透明 

'''设置窗口置顶'''
root.attributes('-topmost', True)

'''设置窗口关闭时执行的函数'''
root.protocol('WM_DELETE_WINDOW', shutdown)
def shutdown():
  print('shutdown')
  root.destory()

'''销毁窗口/组件'''
root.destory()

'''标签组件'''
labl = tk.Label(root, text='a_label', font=('Arial', 26))
labl.pack()

'''填充布局'''
#默认布局
labl.pack()
#自定义布局
labl.place(x=100, y=100)
#网格布局
labl.grid(row=1, column=1)

'''输入框组件'''
enty = tk.Entry(root, width=15, font=26).place(x=200, y=200)

'''创建字符串变量'''
strng = tk.StringVar()
strng = set('placeholder')
enty = tk.Entry(root, textvariable=strng)
print(strng.get())

'''按钮组件'''
btn = tk.Button(root, text='a_button')

'''弹窗组件'''
from tkinter import messagebox
messagebox.showerror(title


'''设置窗口位置为距离显示器左边界100px，距离上边界200px'''
root.geometry('300x200+100+200')
