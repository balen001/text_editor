from cgitb import text
from distutils.util import change_root
from logging import exception
from pathlib import WindowsPath
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tokenize import String
from turtle import title, window_width
from tkinter import messagebox
import os.path

from tkinter import font
from unittest.result import failfast

openedFile = None


def change_color():
    color = colorchooser.askcolor(title = "Pick a color")

    text_area.config(fg = color[1])
    

def change_font(*args):
    text_area.config(font=(fontName.get(), fontSize.get()))





def openFile():
    global openedFile

    file = askopenfilename(defaultextension=".txt", file= [("All files", '*.*'), ("Text Documents", "*.txt")] )

    if file == "":
        return

    else:
        try:
            window.title(os.path.basename(file))

            text_area.delete(1.0, END)

            file = open(file, 'r')
            openedFile = file.name
            text_area.insert(1.0, file.read())
        except Exception:
            messagebox.showerror(title = "Can't read the file")

        finally:
            file.close()



def saveFile():
    global openedFile

    if openedFile is None:
        saveAsNewFile()
    else:
        try:
            file = open(openedFile, 'w')
            file.write(text_area.get(1.0, END))
        except Exception:
            messagebox.showerror(title = "Can't save the file")
        finally:
            file.close()


def saveAsNewFile():
    global openedFile
    file = filedialog.asksaveasfilename(initialfile="Untitled.txt",
                                        defaultextension= ".txt",
                                        filetypes=[("All files", "*.*"),
                                        ("Text Documents", "*.txt")])
    
    if file == "":
        return
        

    else:
        try:
            window.title(os.path.basename(file))
            file = open(file, 'w')  
            file.write(text_area.get(1.0, END)) 
            openedFile = file.name
        except Exception:

            messagebox.showerror(title = "Could not save the file!")
               
        

        finally:
            file.close()


def newWindow():
    pass


def newFile():
    global openedFile
    window.title("Untitled")
    text_area.delete(1.0, END)
    openedFile = None



def cut():
    text_area.event_generate("<<Cut>>")

def copy():
    text_area.event_generate("<<Copy>>")

def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo(title= "About this program", message="Developed by Balen Ahmed")


def quit():
    window.destroy()




window = Tk()

WIDTH = 500
HEIGHT = 500

screenWidth = window.winfo_screenwidth()
screenHeight = window.winfo_screenheight()

x = int((screenWidth/2) - (WIDTH/2))
y = int((screenHeight/2) - (HEIGHT/2))

window.geometry(f"{WIDTH}x{HEIGHT}+{x}+{y}")

fontName = StringVar(window)
fontName.set("Arial")

fontSize = StringVar(window)
fontSize.set("25")

text_area = Text(window, font=(fontName.get(), fontSize.get()))

scrollbar = Scrollbar(text_area)
window.grid_rowconfigure(0,weight=1)
window.grid_columnconfigure(0, weight= 1)
text_area.grid(sticky= N + S + E + W)
scrollbar.pack(side='right', fill= 'y')
text_area.config(yscrollcommand= scrollbar.set)


frame = Frame(window)
frame.grid()

textColor_button = Button(frame, text="Text color", command= change_color)
textColor_button.grid(row=0, column= 0)


fontOption = OptionMenu(frame, fontName, *font.families(), command= change_font )
fontOption.grid(row=0 , column= 1)


spinBox = Spinbox(frame, from_= 1, to= 100, textvariable= fontSize, command= change_font)
spinBox.grid(row=0, column = 2)


menuBar  = Menu(window )
window.config(menu= menuBar)


fileMenu = Menu(menuBar, tearoff=False )
menuBar.add_cascade(label= "File" , menu= fileMenu)


#Adding options

fileMenu.add_command(label= "New", command= newFile)
fileMenu.add_command(label= "New Window", command= newWindow)
fileMenu.add_command(label= "Open", command= openFile)
fileMenu.add_separator()
fileMenu.add_command(label= "Save", command= saveFile)
fileMenu.add_command(label= "Save As", command= saveAsNewFile)
fileMenu.add_separator()
fileMenu.add_command(label= "Exit", command= quit)




editMenu = Menu(menuBar, tearoff=False )
menuBar.add_cascade(label= "Edit" , menu= editMenu)

#Adding options
fileMenu.add_command(label= "Cut", command= cut)
fileMenu.add_command(label= "Copy", command= copy)
fileMenu.add_command(label= "Paste", command= paste)



helpMenu = Menu(menuBar, tearoff=False)
menuBar.add_cascade(label="Help", menu= helpMenu)

helpMenu.add_command(label= "About", command= about)


window.mainloop()




