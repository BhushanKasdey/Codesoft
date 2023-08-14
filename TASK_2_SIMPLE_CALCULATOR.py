from tkinter import *

first_number = second_number = operator = None

def get_digit(digit):
    current = result_label['text']
    new = current + str(digit)
    result_label.config(text=new)

def get_operator(op):
    global first_number, operator
    first_number = int(result_label['text'])
    operator = op
    result_label.config(text='')

def get_result():
    global first_number, second_number, operator

    second_number = int(result_label['text'])

    if operator == '+':
        result_label.config(text=str(first_number + second_number))
    elif operator == '-':
        result_label.config(text=str(first_number - second_number))
    elif operator == '*':
        result_label.config(text=str(first_number * second_number))
    else:
        if second_number == 0:
            result_label.config(text='Error')
        else:
            result_label.config(text=str(first_number / second_number))

def clear():
    result_label.config(text='')

root = Tk()
root.title("Calculator")
root.geometry("280x380")
root.resizable(0, 0)
root.configure(background='black')

result_label = Label(root, text='', bg='black', fg='white')
result_label.grid(row=0, column=0, columnspan=4, pady=(50, 35), sticky='w')
result_label.config(font=('Arial', 30, 'bold'))

buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

row_val = 1
col_val = 0
for button in buttons:
    btn = Button(root, text=button, bg='green', fg='white', width=5, height=2)
    btn.grid(row=row_val, column=col_val)
    btn.config(font=('Arial', 14))
    if button in {'+', '-', '*', '/'}:
        btn.config(bg='grey')
        btn.config(command=lambda op=button: get_operator(op))
    elif button == '=':
        btn.config(command=get_result)
    elif button == 'C':
        btn.config(bg='grey', command=clear)
    else:
        btn.config(command=lambda digit=button: get_digit(digit))
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
