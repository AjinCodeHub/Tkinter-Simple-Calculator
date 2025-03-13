import tkinter
from tkinter import*
window=Tk()
window.title('Calculator')
window.minsize(100,100)
window.maxsize(450,550)
window.geometry("400x500")
window.configure(background='gray90')

equation=''
def show (value):
    global equation
    if equation and equation[-1] in '+-*/' and value in '+-*/':
        # equation = equation[:-1] + value
        return 
    elif equation == '0' and value == '0':
        return
    else:
        equation += value
        e1.delete(0,END)
        e1.insert(END,equation)
    
def clear():
    global equation
    equation= ''
    e1.delete(0, END)

def backspace():
    global equation
    if equation:
        equation = equation[:-1]
        e1.delete(0, END)
        e1.insert(0, equation)

def calculate():
    global equation
    try:
        result = str(eval(equation))
        e1.delete(0, END)
        e1.insert(END, result)
        equation = result
    except Exception as e:
        e1.delete(0, END)
        e1.insert(END, 'Error')
        equation = ''



#ENTRY
e1=Entry(window,font=('Arial',25),justify='right')
e1.grid(row=0,column=0,padx=15,pady=10,ipadx=5,ipady=15,columnspan=5)

#BUTTONS
btn=Button(window,text='C',font='Arial',command=lambda: clear())
btn.grid(row=1,column=2,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='🡠',font='Arial',command=lambda:backspace())
btn.grid(row=1,column=3,ipadx=35,ipady=20,padx=2,pady=3)

btn=Button(window,text='7',font='Arial',command=lambda: show('7'))
btn.grid(row=2,column=0,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='8',font='Arial',command=lambda: show('8'))
btn.grid(row=2,column=1,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='9',font='Arial',command=lambda: show('9'))
btn.grid(row=2,column=2,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='/',font='Arial',command=lambda: show('/'))
btn.grid(row=2,column=3,ipadx=35,ipady=20,padx=2,pady=3)

btn=Button(window,text='4',font='Arial',command=lambda: show('4'))
btn.grid(row=3,column=0,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='5',font='Arial',command=lambda: show('5'))
btn.grid(row=3,column=1,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='6',font='Arial',command=lambda: show('6'))
btn.grid(row=3,column=2,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='*',font='Arial',command=lambda: show('*'))
btn.grid(row=3,column=3,ipadx=35,ipady=20,padx=2,pady=3)

btn=Button(window,text='1',font='Arial',command=lambda: show('1'))
btn.grid(row=4,column=0,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='2',font='Arial',command=lambda: show('2'))
btn.grid(row=4,column=1,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='3',font='Arial',command=lambda: show('3'))
btn.grid(row=4,column=2,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='-',font='Arial',command=lambda: show('-'))
btn.grid(row=4,column=3,ipadx=35,ipady=20,padx=2,pady=3)


btn=Button(window,text='0',font='Arial',command=lambda: show('0'))
btn.grid(row=5,column=1,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='•',font='Arial',command=lambda: show('.'))
btn.grid(row=5,column=0,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='+',font='Arial',command=lambda: show('+'))
btn.grid(row=5,column=2,ipadx=35,ipady=20,padx=2,pady=3)
btn=Button(window,text='=',font='Arial',command=calculate)
btn.grid(row=5,column=3,ipadx=35,ipady=20,padx=2,pady=3)



window.mainloop()