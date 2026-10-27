from tkinter import *
import math


w = Tk()

a = PhotoImage(file = 'C:\\Users\\ntvu0\\Pictures\\PICS\\Calculator project.png')

w.geometry('700x500')
w.title('Calculator')
w.iconphoto(True, a)

num_list = [7,8,9,4,5,6,1,2,3,0]


for j in range(len(num_list)):
    num_list[j] = str(num_list[j])
operation_list = ['+', '-', '*', '/', '//', '%']


label = Label(w, text = '', pady = 20)
label.grid(row = 0, column=0, columnspan = 5)

allclear_button = Button(w, text = ('AC'), font=('Arial', 20), command = lambda:label.config(text = ''))
allclear_button.grid(row = 2, column =  4)

clear_button = Button(w, text = 'C', font=('Arial', 20), command =  lambda:label.config(text = label.cget('text')[:-1]))
clear_button.grid(row = 2, column =5)

ppi_button = Button(w, text = 'π', font=('Arial',20),command = lambda:label.config(text = label.cget('text') + 'π'))
ppi_button.grid(row = 5, column = 1)

def nums_button():
    for i, num in enumerate(num_list):
        
        button = Button(w, text = num, font=('Arial', 20),command = lambda i=i:label.config(text = label.cget('text')+ num_list[i]))
        button.grid(row = i//3 + 2, column =i%3 )


nums_button()

def operate_button():
    for j, op in enumerate(operation_list):
        
        button_op = Button(w, text = op, font=('Arial', 20),command = lambda j=j:label.config(text = label.cget('text')+ operation_list[j]))
        button_op.grid(row=j//2 + 3, column = j%2 + 4)

operate_button()

def evaluation():
    try:
        expr = label.cget('text')
        tempo = expr
        while 'π' in tempo:
            pos = tempo.index('π')
            
            before = tempo[pos -1 ] if pos > 0 else ''
            after = tempo[pos + 1] if (pos +1) < len(tempo) else ''

            if before.isdigit() and after.isdigit() :
                tempo = tempo[:pos ] + '*math.pi*' + tempo[pos +1:]

            elif before.isdigit():
                tempo = tempo[:pos ] + '*math.pi' + tempo[pos +1:]

            elif after.isdigit():
                tempo = tempo[:pos ] + 'math.pi*' + tempo[pos +1:]

            else:
                tempo = tempo[:pos ] + 'math.pi' + tempo[pos +1:]


        result = eval(tempo)
        label.config(text =str(result))
    except(SyntaxError, ZeroDivisionError):
        label.config(text = 'Error')

equal_button = Button(w, text = '=', font=('Arial', 20), command = evaluation)
equal_button.grid(row=5, column =6)

dot_button = Button(w, text='.', font=('Arial', 20), command=lambda:label.config(text =label.cget('text') + '.'))
dot_button.grid(row = 5, column =2)

def square_root():
    try:
        value = float(label.cget('text'))
        label.config(text = str(math.sqrt(value)))
    except ValueError:
         label.config(text = '√ must come after the number')

squrt_button = Button(w, text = '√', font=('Arial', 20), command = square_root)
squrt_button.grid(row= 2, column = 3)


w.mainloop()