from tkinter import *

win=Tk()

win.title("Simple Calculator")

e=Entry(win,width=40,borderwidth=10)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def fun(num):
    current=e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(num))

def clear():
    e.delete(0,END)

def add():
    global f_num
    f_num=int(e.get())
    global cal
    cal="ADD"
    e.delete(0,END)

def sub():
    global f_num
    f_num=int(e.get())
    global cal
    cal="sub"
    e.delete(0,END)

def multi():
    global f_num
    f_num=int(e.get())
    global cal
    cal="multi"
    e.delete(0,END)

def div():
    global f_num
    f_num=int(e.get())
    global cal
    cal="div"
    e.delete(0,END)

def equal():
    s_num=e.get()
    e.delete(0,END)
    if cal=="ADD":
        e.insert(0,f_num + int(s_num))
    elif cal=="sub":
        e.insert(0,f_num - int(s_num))
    elif cal=="multi":
        e.insert(0,f_num * int(s_num))
    elif cal=="div":
        e.insert(0,f_num / int(s_num))
    
    


   
button1=Button(win,text="1",command=lambda:fun(1),padx=40,pady=20)
button2=Button(win,text="2",command=lambda:fun(2),padx=40,pady=20)
button3=Button(win,text="3",command=lambda:fun(3),padx=40,pady=20)
button4=Button(win,text="4",command=lambda:fun(4),padx=40,pady=20)
button5=Button(win,text="5",command=lambda:fun(5),padx=40,pady=20)
button6=Button(win,text="6",command=lambda:fun(6),padx=40,pady=20)
button7=Button(win,text="7",command=lambda:fun(7),padx=40,pady=20)
button8=Button(win,text="8",command=lambda:fun(8),padx=40,pady=20)
button9=Button(win,text="9",command=lambda:fun(9),padx=40,pady=20)
button0=Button(win,text="0",command=lambda:fun(0),padx=40,pady=20)
buttonadd=Button(win,text="+",command=add,padx=40,pady=20)
buttonsub=Button(win,text="-",command=sub,padx=40,pady=20)
buttonmulti=Button(win,text="*",command=multi,padx=40,pady=20)
buttondiv=Button(win,text="/",command=div,padx=40,pady=20)
buttonclear=Button(win,text="Clear",command=clear,padx=40,pady=20)
buttonequal=Button(win,text="=",command=equal,padx=80,pady=20)

button1.grid(row=1,column=0,padx=2,pady=5)
button2.grid(row=1,column=1,padx=2,pady=5)
button3.grid(row=1,column=2,padx=2,pady=5)
button4.grid(row=2,column=0,padx=2,pady=5)
button5.grid(row=2,column=1,padx=2,pady=5)
button6.grid(row=2,column=2,padx=2,pady=5)
button7.grid(row=3,column=0,padx=2,pady=5)
button8.grid(row=3,column=1,padx=2,pady=5)
button9.grid(row=3,column=2,padx=2,pady=5)
button0.grid(row=4,column=0,padx=2,pady=5)
buttonadd.grid(row=4,column=1,padx=2,pady=5)
buttonsub.grid(row=4,column=2,padx=2,pady=5)
buttonmulti.grid(row=5,column=0,padx=2,pady=5)
buttondiv.grid(row=5,column=1,padx=2,pady=5)
buttonclear.grid(row=5,column=2,pady=5,padx=2)
buttonequal.grid(row=6,column=0,columnspan=3)



win.mainloop()