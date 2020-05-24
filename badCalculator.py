from tkinter import *
import math
import tkinter.font as font
import random

equationText = ""

def addToEquation(character, equationBox):
    global equationText
    equationText = equationText + str(character)
    equationBox.set(equationText)

def clearEquation(equationBox):
    global equationText
    equationText = ""
    equationBox.set("Enter an equation")

def evaluate(equationBox):
    global equationText
    try:
        result = str(eval(equationText))
        answer(result, equationBox)
    except Exception as e:
        print(e)
        equationBox.set("Not a valid equation")
        expression = ""

def answer(result, equationBox):
    global equationText
    prefix = getRandomLine("prefixes.txt")
    result = prefix + result
    equationBox.set(result)
    equationText = ""

def getRandomLine(fileName):
    lines = []                          
    with open (fileName, 'rt') as myfile: 
        for aLine in myfile:            
            lines.append(aLine)
    line = random.randint(1, len(lines))
    return lines[line-1]

def main():
        window = Tk()
        window.title("Bad Calculator")
        window.geometry("500x600")
        equationBox = StringVar()
        input_field = Entry(window, textvariable = equationBox)
        input_field['font'] = font.Font(size=16)
        input_field.grid(columnspan=4, sticky=N+S+E+W)
        equationBox.set("Enter an equation")
        for i in range(10):
            button = Button(window, text=(i+1)%10, fg='white', bg='coral', bd=1,
                command=lambda j=i+1: addToEquation(j%10, equationBox))
            button['font'] = font.Font(size=24)
            button.grid(row=math.floor(i/3)+1, column=i%3, sticky=N+S+E+W)
        plus = Button(window, text='+', fg='white', bg='firebrick', bd=1, command=lambda: addToEquation('+', equationBox))
        plus['font'] = font.Font(size=24)
        plus.grid(row=1, column=3, sticky=N+S+E+W)
        minus = Button(window, text='-', fg='white', bg='firebrick', bd=1, command=lambda: addToEquation('-', equationBox))
        minus['font'] = font.Font(size=24)
        minus.grid(row=2, column=3, sticky=N+S+E+W)
        multiply = Button(window, text='*', fg='white', bg='firebrick', bd=1, command=lambda:  addToEquation('*', equationBox))
        multiply['font'] = font.Font(size=24)
        multiply.grid(row=3, column=3, sticky=N+S+E+W)
        divide = Button(window, text='÷', fg='white', bg='firebrick', bd=1, command=lambda: addToEquation('/', equationBox))
        divide['font'] = font.Font(size=24)
        divide.grid(row=4, column=3, sticky=N+S+E+W)
        equal = Button(window, text='=', fg='white', bg='firebrick', bd=1, command=lambda: evaluate(equationBox))
        equal['font'] = font.Font(size=24)
        equal.grid(row=4, column=2, sticky=N+S+E+W)
        clear = Button(window, text='Clear', fg='white', bg='firebrick', bd=1, command=lambda: clearEquation(equationBox))
        clear['font'] = font.Font(size=12)
        clear.grid(row=4, column=1, sticky=N+S+E+W)

        window.grid_columnconfigure(0,weight=1)
        window.grid_columnconfigure(1,weight=1)
        window.grid_columnconfigure(2,weight=1)
        window.grid_columnconfigure(3,weight=1)
        window.grid_rowconfigure(0,weight=1)
        window.grid_rowconfigure(1,weight=1)
        window.grid_rowconfigure(2,weight=1)
        window.grid_rowconfigure(3,weight=1)
        window.grid_rowconfigure(4,weight=1)


        window.mainloop()


#if __name__ == '__main__':
main()