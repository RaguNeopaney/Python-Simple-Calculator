_author_ = "Ragu Neopaney"
_email_ = "neopanru@mail.uc.edu"
_credits_ = [
                # window size and look
                'https://www.geeksforgeeks.org/resizable-method-in-tkinter-python/'
                # window icon
                'https://www.delftstack.com/howto/python-tkinter/how-to-set-window-icon-in-tkinter/'
            ]

import tkinter
from tkinter import *

# set tkinter with our own variable to easy use
cal = tkinter.Tk()

# Put a label for our GUI calculator
cal.title('SIMPLE CALCULATOR')



# function for the calculator
def btnClick1():
    global operator
    operator = operator + '1'
    user_input.set(operator)
def btnClick2():
    global operator
    operator = operator + '2'
    user_input.set(operator)

def btnClick3():
    global operator
    operator = operator + '3'
    user_input.set(operator)

def btnClick4():
    global operator
    operator = operator + '4'
    user_input.set(operator)

def btnClick5():
    global operator
    operator = operator + '5'
    user_input.set(operator)

def btnClick6():
    global operator
    operator = operator + '6'
    user_input.set(operator)

def btnClick7():
    global operator
    operator = operator + '7'
    user_input.set(operator)

def btnClick8():
    global operator
    operator = operator + '8'
    user_input.set(operator)

def btnClick9():
    global operator
    operator = operator + '9'
    user_input.set(operator)

def btnClick0():
    global operator
    operator = operator + '0'
    user_input.set(operator)

def btn_plus():
    global op
    global operator
    global save_num
    save_num = int(operator)
    op = "+"
    operator = operator + '+'
    user_input.set(operator)

def btn_min():
    global op
    global operator
    global save_num
    save_num = int(operator)
    op = '-'
    operator = operator + '-'
    user_input.set(operator)
def btn_multi_tot():
    global op
    global operator
    global save_num
    save_num = int(operator)
    op = '*'
    operator = operator + '*'
    user_input.set(operator)
def btn_div_tot():
    global op
    global operator
    global save_num
    save_num = int(operator)
    op = '/'
    operator = operator + '/'
    user_input.set(operator)

def clear_btn():
    global operator
    global op
    global save_num
    save_num = 0
    operator = ''
    op = ''
    user_input.set(operator)

def equl_btn():
    global operator
    global save_num
    global op
    total = 0
    num_lst = operator.split(op)
    B = num_lst[1]
    if op == '+':
        total = save_num + int(B)
    elif op == '*':
        total = save_num * int(B)
    elif op == '/':
        total = save_num / int(B)
    elif op == '-':
        total = save_num - int(B)
    user_input.set(total)

op = ''
save_num = 0
operator = ''
# create a window look
cal.geometry('250x400+300+300')
cal.resizable(0,0)
# adding a icon to our window
cal.iconbitmap('icon.ico')
cal.configure(background='black')
# text input
user_input = StringVar()

# Display for calculation
display_label = Label(cal,textvariable = user_input, anchor= SE, font = ("Verdana", 15, "bold"))
display_label.pack(expand=True, fill = tkinter.BOTH)

# row of button 1
row_button1 = tkinter.Frame(cal, background = "Gray80")
row_button1.pack(expand= True, fill = tkinter.BOTH)

# row of button 2
row_button2 = tkinter.Frame(cal, background = "Gray80")
row_button2.pack(expand= True, fill = tkinter.BOTH)

# row of button 3
row_button3 = tkinter.Frame(cal, background = "Gray80")
row_button3.pack(expand= True, fill = tkinter.BOTH)

# row of button 4
row_button4 = tkinter.Frame(cal, background = "Gray80")
row_button4.pack(expand= True, fill = tkinter.BOTH)


# buttons for row one
btn1 = tkinter.Button(row_button1,text = '1', font = ("Verdana", 22), relief = GROOVE, command = btnClick1, border = 0,background = "Gray80")
btn1.pack(side = LEFT, expand =1, fill = BOTH)

btn2 = tkinter.Button(row_button1,text = '2', font = ("Verdana", 22), relief = GROOVE, command = btnClick2, border = 0,background = "Gray80")
btn2.pack(side = LEFT, expand =1, fill = BOTH)

btn3 = tkinter.Button(row_button1,text = '3', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = btnClick3)
btn3.pack(side = LEFT, expand =1, fill = BOTH)

btn_plus = tkinter.Button(row_button1,text = '+', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = btn_plus)
btn_plus.pack(side = LEFT, expand =1, fill = BOTH)

# ROW 2
btn4 = tkinter.Button(row_button2,text = '4', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = btnClick4)
btn4.pack(side = LEFT, expand =1, fill = BOTH)

btn5 = tkinter.Button(row_button2,text = '5', font = ("Verdana", 22),  relief = GROOVE, border = 0,background = "Gray80", command = btnClick5)
btn5.pack(side = LEFT, expand =1, fill = BOTH)

btn6 = tkinter.Button(row_button2,text = '6', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80",  command = btnClick6)
btn6.pack(side = LEFT, expand =1, fill = BOTH)

btn_minus = tkinter.Button(row_button2,text = '-', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = btn_min)
btn_minus.pack(side = LEFT, expand =1, fill = BOTH)

# Row 3
btn7 = tkinter.Button(row_button3,text = '7', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = btnClick7)
btn7.pack(side = LEFT, expand =1, fill = BOTH)

btn8 = tkinter.Button(row_button3,text = '8', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = btnClick8)
btn8.pack(side = LEFT, expand =1, fill = BOTH)

btn9 = tkinter.Button(row_button3,text = '9', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = btnClick9)
btn9.pack(side = LEFT, expand =1, fill = BOTH)

btn_multi = tkinter.Button(row_button3,text = '*', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = btn_multi_tot)
btn_multi.pack(side = LEFT, expand =1, fill = BOTH)

# row 4
btn_clr = tkinter.Button(row_button4,text = 'C', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = clear_btn)
btn_clr.pack(side = LEFT, expand =1, fill = BOTH)

btn0 = tkinter.Button(row_button4,text = '0', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = btnClick0)
btn0.pack(side = LEFT, expand =1, fill = BOTH)

btn_equal = tkinter.Button(row_button4,text = '=', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = equl_btn)
btn_equal.pack(side = LEFT, expand =1, fill = BOTH)

btn_div = tkinter.Button(row_button4,text = '/', font = ("Verdana", 22), relief = GROOVE, border = 0,background = "Gray80", command = btn_div_tot)
btn_div.pack(side = LEFT, expand =1, fill = BOTH)

# This will open the window
cal.mainloop()