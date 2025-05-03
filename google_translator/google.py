from tkinter import *
from tkinter import ttk

from googletrans import Translator, LANGUAGES

def translate_text(text="type",src="en", dest="hi"):
    text1=text
    src1=src
    dest1=dest
    trans=Translator()
    trans1 = trans.translate(text,src=src1,dest=dest1)
    return trans1

def dataget():
    s = combo_Sorce.get()
    d = combo_destination.get()
    msg = sorce_text.get(1.0, END)
    textget = translate_text(text=msg, src=s, dest=d)
    destination_text.delete(1.0, END)
    destination_text.insert(1.0, textget.text)



root = Tk()
root.title("Google Translator")
root.geometry("500x800")
root.config(bg="light blue")

lab_txt = Label(root, text = "Google Translator", font=("Arial", 30 ,"bold"), bg="light blue", fg="black")
lab_txt.place(x=20,y=40,height=50,width=500)


frame = Frame(root).pack(side=BOTTOM)

sorce = Label(root, text = "Source Text", font=("Arial", 20 ,"bold"), bg="light blue", fg="black")
sorce.place(x=120,y=100,height=20,width=300)

sorce_text = Text(frame, font=("Arial", 15), bg="white", fg="black", wrap=WORD)
sorce_text.place(x=10, y=130, height=200, width=480)

list_text = list(LANGUAGES.values())

combo_Sorce = ttk.Combobox(frame, values=list_text)
combo_Sorce.place(x=10, y=340, height=30, width=150)
combo_Sorce.set("Select Language")

button_change = Button(frame, text = "Translate", relief=RAISED, command=dataget)
button_change.place(x=180, y=340, height=30, width=100)

combo_destination = ttk.Combobox(frame, values=list_text)
combo_destination.place(x=300, y=340, height=30, width=150)
combo_destination.set("Select Language")


lab_txt = Label(root, text = "Destination Text", font=("Arial", 30 ,"bold"), bg="light blue", fg="black")
lab_txt.place(x=20,y=380,height=50,width=500)


destination_text = Text(frame, font=("Arial", 10), bg="white", fg="black", wrap=WORD)
destination_text.place(x=10, y=430, height=200, width=480)


root.mainloop()