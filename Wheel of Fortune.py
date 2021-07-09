import tkinter as tk
import tkinter.messagebox

window1 = tk.Tk()
window1.title("运气仪")
window1.geometry("700x300")

ans = tk.StringVar()
gue = tk.StringVar()
con = tk.StringVar()
count = 0

st = tk.Label(window1, textvariable = con, bg = "white", font = ("SimHei",25), width = 70)    #状态栏
st.pack()
an = tk.Entry(window1, textvariable = ans, show = "*", bg = "green", font = ("Arial", 30), width = 30)    #输入栏甲
an.pack()
gu = tk.Entry(window1, textvariable = gue, show = None, bg = 'yellow', font = ("arial", 30), width = 30)    #输入栏乙
gu.pack()

def hit_me():
    global count
    if str(an.get()) == str(gu.get()):
        con.set("")
        tkinter.messagebox.showinfo(title="Hi!", message = "猜对了！")
        count = 0
    else:
        count = count + 1
        if count % 2 == 1:
            con.set("哈哈！你猜错了！"+"error："+str(count)+"次")
        else:
            con.set("哈哈！你又猜错了！"+"error："+str(count)+"次")
        gue.set("")

b = tk.Button(window1, text = "提交", font = ("", 20), width = 20, command = hit_me)
b.pack()
window1.mainloop()
