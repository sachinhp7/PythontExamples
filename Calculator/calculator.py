# Import tkinter library to create GUI (Graphical User Interface)
from tkinter import *


# Creating a function to take inputs from the user

def button_press(num):

    global equation_text

    equation_text = equation_text + str(num)
    equation_label.set(equation_text)


# Create a function to do the calculation using eval() function

def equals():

    global equation_text

    try:

        # This eval() function gives the value when string math expression was given
        total = str(eval(equation_text))

        equation_label.set(total)

        equation_text = total

    except SyntaxError:     # Display if a syntax error occur
        equation_label.set("syntax error")

        equation_text = ""

    except ZeroDivisionError:  # Display if an invalid arithmetic operation occur

        equation_label.set("arithmetic error")

        equation_text = ""


# Create a function to remove the enterd values

def clear():

    global equation_text

    equation_label.set("")

    equation_text = ""


window = Tk()     # Create the window to display the calculator

icon = PhotoImage(file="calculator.png")   # Convert icon photo into PhotoImage
window.iconphoto(True, icon)   # Setting the icon image

window.title("Calculator")   # Setting the Title

window.geometry("500x600")  # Setting Size of the window

equation_text = ""    # Variable to store user inputs

# The label is converting user inputs to a string variable
equation_label = StringVar()


# A label to display user inputs

label = Label(window,
              textvariable=equation_label,
              font=("consolas", 20),
              bg="#C0D5D7",
              width=24,
              height=2)
label.pack()


# A frame to hold the keys of the calculator

frame = Frame(window)
frame.pack()


button1 = Button(frame,           # Creating  Button of the keypad
                 text=1,
                 height=4,
                 width=9,
                 font=35,
                 bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press(1))

button1.grid(row=0, column=0)     # Displaying buttton in the grid


button2 = Button(frame,             # Creating  Button  of the keypad
                 text=2,
                 height=4,
                 width=9,
                 font=35,
                 bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press(2))

button2.grid(row=0, column=1)                 # Displaying buttton in the grid


button3 = Button(frame,                # Creating  Button of the keypad
                 text=3,
                 height=4,
                 width=9,
                 font=35,
                 bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press(3))

button3.grid(row=0, column=2)          # Displaying buttton in the grid


button4 = Button(frame,                      # Creating  Button of the keypad
                 text=4,
                 height=4,
                 width=9,
                 font=35,
                 bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press(4))

# Displaying buttton in the grid
button4.grid(row=1, column=0)


button5 = Button(frame,                        # Creating  Button of the keypad
                 text=5,
                 height=4,
                 width=9,
                 font=35,
                 bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press(5))

button5.grid(row=1, column=1)             # Displaying buttton in the grid


button6 = Button(frame,               # Creating  Button of the keypad
                 text=6,
                 height=4,
                 width=9,
                 font=35,
                 bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press(6))

button6.grid(row=1, column=2)           # Displaying buttton in the grid


button7 = Button(frame,                  # Creating  Button of the keypad
                 text=7,
                 height=4,
                 width=9,
                 font=35,
                 bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press(7))

button7.grid(row=2, column=0)


button8 = Button(frame,                     # Creating  Button of the keypad
                 text=8,
                 height=4,
                 width=9,
                 font=35,
                bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press(8))

button8.grid(row=2, column=1)              # Displaying buttton in the grid


button9 = Button(frame,                         # Creating  Button of the keypad
                 text=9,
                 height=4,
                 width=9,
                 font=35,
                 bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press(9))

button9.grid(row=2, column=2)            # Displaying buttton in the grid


button0 = Button(frame,                   # Creating  Button of the keypad
                 text=0,
                 height=4,
                 width=9,
                 font=35,
                 bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press(0))

button0.grid(row=3, column=0)             # Displaying buttton in the grid


plus = Button(frame,                    # Creating  Button of the keypad
              text='+',
              height=4,
              width=9,
              font=35,
              bg="#00002E",
              fg='#07E1F5',
              command=lambda: button_press('+'))

plus.grid(row=0, column=3)                 # Displaying buttton in the grid


minus = Button(frame,             # Creating  Button of the keypad
               text='-',
               height=4,
               width=9,
               font=35,
               bg="#00002E",
               fg='#07E1F5',
               command=lambda: button_press('-'))

minus.grid(row=1, column=3)           # Displaying buttton in the grid


multiply = Button(frame,                 # Creating  Button of the keypad
                  text='*',
                  height=4,
                  width=9,
                  font=35,
                  bg="#00002E",
                  fg='#07E1F5',
                  command=lambda: button_press('*'))

multiply.grid(row=2, column=3)               # Displaying buttton in the grid


divide = Button(frame,            # Creating  Button of the keypad
                text='/',
                height=4,
                width=9,
                font=35,
                bg="#00002E",
                fg='#07E1F5',
                command=lambda: button_press('/'))

divide.grid(row=3, column=3)              # Displaying buttton in the grid


equal = Button(frame,             # Creating  Button of the keypad
               text='=',
               height=4,
               width=9,
               font=35,
               bg="#00002E",
               fg='#07E1F5',
               command=equals)

equal.grid(row=3, column=2)           # Displaying buttton in the grid


decimal = Button(frame,                    # Creating  Button of the keypad
                 text='.',
                 height=4,
                 width=9,
                 font=35,
                 bg="#00002E",
                 fg='#07E1F5',
                 command=lambda: button_press('.'))

decimal.grid(row=3, column=1)            # Displaying buttton in the grid

clear = Button(window,                          # Creating  Button of the keypad
               text='clear',
               height=4,
               width=12,
               font=35,
               bg="#00002E",
               fg='#07E1F5',
               command=clear)

clear.pack()                                    # Calling clear function

window.mainloop()          # Stop closing of the window
