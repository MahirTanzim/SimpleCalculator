from tkinter import *

root = Tk()
root.title("Simple Calculator")


# Number Entry Section
e = Entry(root, width=32, borderwidth=3)
# Positioning Entry Section
e.grid(row = 0, column = 0, columnspan = 3, padx=10, pady=10)

# Functions
def button_click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
    
def clear():
    e.delete(0, END)
    
def addition():
    first_number = e.get()
    global f_num
    global operation
    operation = "add"
    f_num = int(first_number)
    e.delete(0, END)

def multiplication():
    first_number = e.get()
    global f_num
    global operation
    operation = "mult"
    f_num = int(first_number)
    e.delete(0, END)

def substraction():
    first_number = e.get()
    global f_num
    global operation
    operation = "sub"
    f_num = int(first_number)
    e.delete(0, END)

def division():
    first_number = e.get()
    global f_num
    global operation
    operation = "div"
    f_num = int(first_number)
    e.delete(0, END)

def negation():
    first_number = e.get()
    neg = int(first_number)
    e.delete(0, END)
    e.insert(0, -1*neg)
    
def equal():
    second_number = e.get()
    e.delete(0, END)
    if operation == "add":
        e.insert(0, f_num + int(second_number))
    if operation == "mult":
        e.insert(0, f_num * int(second_number))
    if operation == "sub":
        e.insert(0, f_num - int(second_number))
    if operation == "div":
        e.insert(0, f_num / int(second_number))
    
    

# Buttons and their attributes.
button_1 = Button(root, text = '1', padx=30, pady=10, borderwidth=3, command=lambda: button_click(1))
button_2 = Button(root, text = '2', padx=30, pady=10, borderwidth=3, command=lambda: button_click(2))
button_3 = Button(root, text = '3', padx=30, pady=10, borderwidth=3, command=lambda: button_click(3))
button_4 = Button(root, text = '4', padx=30, pady=10, borderwidth=3, command=lambda: button_click(4))
button_5 = Button(root, text = '5', padx=30, pady=10, borderwidth=3, command=lambda: button_click(5))
button_6 = Button(root, text = '6', padx=30, pady=10, borderwidth=3, command=lambda: button_click(6))
button_7 = Button(root, text = '7', padx=30, pady=10, borderwidth=3, command=lambda: button_click(7))
button_8 = Button(root, text = '8', padx=30, pady=10, borderwidth=3, command=lambda: button_click(8))
button_9 = Button(root, text = '9', padx=30, pady=10, borderwidth=3, command=lambda: button_click(9))
button_0 = Button(root, text = '0', padx=30, pady=10, borderwidth=3, command=lambda: button_click(0))
button_add = Button(root, text = '+', padx=28, pady=10, borderwidth=3, command=addition)
button_mult = Button(root, text = 'x', padx=29, pady=10, borderwidth=3, command=multiplication)
button_sub = Button(root, text = '-', padx=30, pady=10, borderwidth=3, command=substraction)
button_div = Button(root, text = '/', padx=30, pady=10, borderwidth=3,command=division)
button_equal = Button(root, text = '=', padx=30, pady=10, borderwidth=3, command=equal)
button_clear = Button(root, text = 'Clear', padx=20, pady=10, borderwidth=3, command=clear)
button_neg = Button(root, text = "+/-", padx=25, pady=10, borderwidth=3, command=negation)


# Positioning the button on the screen
button_0.grid(row=4,column=0)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)

button_add.grid(row=4, column=3)
button_sub.grid(row=3, column=3)
button_mult.grid(row=2, column=3)
button_div.grid(row=1, column=3)
button_clear.grid(row=0, column=3)
button_equal.grid(row=4, column=2)
button_neg.grid(row=4, column=1)

#Display the project
root.mainloop()

