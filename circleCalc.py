from tkinter import *
from dark_title_bar import *

w = Tk()
w.geometry('500x250')
w.title('circleCalc')
w.configure(bg='#242424')
w.resizable(False, False)
w.iconbitmap('icon.ico')
dark_title_bar(w)

lbl = Label(w, text='Radius', bg='#242424', foreground='white')
lbl.pack(pady=10)

e = Entry(w, text='Enter:', bg='#242424', foreground='white')
e.pack(pady=10)

def sub():
    l1.configure(text= 'Circumfrence: ' + f'{int(2)*int(22)/int(7)*int(str(e.get()))}')
    l2.configure(text= 'Area: ' + f'{int(22)/int(7)*int(str(e.get()))*int(str(e.get()))}')
    
l1 = Label(w, text= '', bg='#242424', foreground='white')
l1.pack(pady=8)
l2 = Label(w, text= '', bg='#242424', foreground='white')
l2.pack(pady=3)

btn = Button(w, text='Submit', bg='#242424', foreground='white', command=sub)
btn.pack(pady=3)

w.mainloop()