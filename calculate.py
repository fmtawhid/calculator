from tkinter import *
x=Tk()

#entry section

mentry=Entry(x, width=40,borderwidth=10)
mentry.grid(row=0,column=0,columnspan=3, padx=10,pady=10)
mentry.focus_set()

#function area

def button_click(number):
    mentry.insert(0,number)


#Button Section

btn_1 = Button(x, text='1', padx=40,pady=20, command= lambda: button_click(1))
btn_2 = Button(x, text='2', padx=40,pady=20, command= lambda: button_click(2))
btn_3 = Button(x, text='3', padx=40,pady=20, command= lambda: button_click(3))
btn_4 = Button(x, text='4', padx=40,pady=20, command= lambda: button_click(4))
btn_5 = Button(x, text='5', padx=40,pady=20, command= lambda: button_click(5))
btn_6 = Button(x, text='6', padx=40,pady=20, command= lambda: button_click(6))
btn_7 = Button(x, text='7', padx=40,pady=20, command= lambda: button_click(7))
btn_8 = Button(x, text='8', padx=40,pady=20, command= lambda: button_click(8))
btn_9 = Button(x, text='9', padx=40,pady=20, command= lambda: button_click(9))
btn_0 = Button(x, text='0', padx=40,pady=20, command= lambda: button_click(0))

button_add=Button(x,text='+',padx=70,pady=20,command=button_click)
button_equal=Button(x,text='=',padx=91,pady=20,command=button_click)
button_clear=Button(x,text='c',padx=39,pady=20,command=button_click)

#button show
btn_1.grid(row=1,column=0)
btn_2.grid(row=1,column=1)
btn_3.grid(row=1,column=2)


btn_4.grid(row=2,column=0)
btn_5.grid(row=2,column=1)
btn_6.grid(row=2,column=2)


btn_7.grid(row=3,column=0)
btn_8.grid(row=3,column=1)
btn_9.grid(row=3,column=2)


btn_0.grid(row=4,column=0)

button_add.grid(row=5,column=0)
button_equal.grid(row=5,column=1)
button_clear.grid(row=4,column=1)



x.mainloop()
