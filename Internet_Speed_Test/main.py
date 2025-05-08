#internet speed test with gui

from tkinter import *
import speedtest

#design GUI

sp = Tk()
sp.title("Internet Speed Tester")                # for the title
sp.geometry("500x500")                           # for the area
sp.config(bg = "light green")                    #for the color

lab = Label(sp,text="Internet Speed Test", font = ("Time New roman", 30, "bold"),bg="light green", fg = "green")

lab.place(x=55,y=40)                             #for the place in GUI
sp.mainloop()                                    # this for the view window

