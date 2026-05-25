import os
from tkinter import *  # Import tkinter library to create GUI (Graphical User Interface)
from tkinter import filedialog, colorchooser, font  # Import filedialog, colorchooser, font
from tkinter.messagebox import *  # Importing message box
from tkinter.filedialog import *  # Importing fileddialog box



# Creating a function to change a color

def change_color():
    color = colorchooser.askcolor(title="pick a color...")
    text_area.config(fg=color[1])


# Creating a function to change font size

def change_font(* args):
    text_area.config(font=(font_name.get(), size_box.get()))



# Creating a function to open a new file

def new_file():
    window.title("Untitled")   # Seting the titel of the new file as untitled by default
    text_area.delete(1.0, END)


# Creating a function to open a existing file

def open_file():
    file = askopenfilename(defaultextension=".txt",
                           file=[("All Files", "*.*"),
                                 ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            text_area.delete(1.0, END)

            file = open(file, "r")

            text_area.insert(1.0, file.read())

        except Exception:
            print("couldn't read file")

        finally:
            file.close()


# Creating a function to save the file

def save_file():
    file = filedialog.asksaveasfilename(initialfile='unititled.txt',
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])

    if file is None:
        return

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, "w")

            file.write(text_area.get(1.0, END))

        except Exception:
            print("couldn't save file")

        finally:
            file.close()


# Creating a function to cut

def cut():
    text_area.event_generate("<<Cut>>")


# Creating a function to copy

def copy():
    text_area.event_generate("<<Copy>>")


# Creating a function to paste

def paste():
    text_area.event_generate("<<Paste>>")


# Creating a function to display about

def about():
    showinfo("About this program", "This is a program written by YOU!!!")



# Creating a function to close the window

def quit():
    window.destroy()



window = Tk()   # Creating a window
window.title("Text Editor")  # Setting title of the widow
file = None

icon = PhotoImage(file="texteditor icon.png")  # Converting png photo into a photo image
window.iconphoto(True,icon) # Setting icon of the program


# Adjusting height and width of the program

window_width = 500
window_height = 500
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))



# Setting font name

font_name = StringVar(window)
font_name.set("Arial")


# Setting font size

font_size = StringVar(window)
font_size.set("25")

# Getting font name and font size from the text area

text_area = Text(window, font=(font_name.get(), font_size.get()))

# Setting a scroller bar

scroll_bar = Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0,weight=1)
text_area.grid(sticky=N + E + S + W)

scroll_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scroll_bar.set)


# Creating a frame to display buttons

frame = Frame(window)
frame.grid()

# Creating colour picking button

color_button = Button(frame,text="color",command=change_color)
color_button.grid(row=0,column=0)


# Creating font name button

font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0,column=1)


# Creating font size box

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)


# Creating menu bar

menu_bar = Menu(window)
window.config(menu=menu_bar)

# Creating items of the menu bar file menu

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)



# Creating items of the menu bar edit menu

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)


# Creating items of the menu bar help menu

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)





window.mainloop() # Stop the closing of the window.


