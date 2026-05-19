# mport tkinter for create the GUI (Graphical User Interface)
from tkinter import *

from time import *  # Import time libarary to do the calculations


# Creating function to display date and time


def update():
    # obtaing time in hours, minuite, second and am or pm
    time_string = strftime("%I:%M:%S %p")
    # asigning the time and date to the label
    time_label.config(text=time_string)

    day_string = strftime("%A")  # obtaing day of the week
    # assigning the obatined value to the label
    day_label.config(text=day_string)

    date_string = strftime("%B %d, %Y")  # obtaining month date and year
    # assigning the obtained month date and year
    date_label.config(text=date_string)

    window.after(1000, update)  # auto update after 1000 secs


window = Tk()

window.title("Clock")  # adding title

icon = PhotoImage(file="clock.png")   # convert a png image to a photo image
window.iconphoto(True, icon)  # setting icon

window.resizable(False, False)  # Disableing resize options

# createing a lable to display time

time_label = Label(window,
                   font=("Arial", 50),
                   fg="#00FF00",
                   bg="black"
                   )
time_label.pack()


# creating a label to display date of the week

day_label = Label(window,
                  font=("Ink Free", 50),
                  )
day_label.pack()


# creating a label to display month, date and year

date_label = Label(window,
                   font=("Ink Free", 25),
                   )
date_label.pack()

update()  # Calling the function update()


window.mainloop()  # Stop closing of the window
