from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500 , height=300)
window.config(padx=30,pady=30)

my_label = Label(text = "I am a  Label ", font = ("Arial",24,"bold"))
# my_label.config(text ="new text")
# my_label.pack(side = "top")
# my_label.place(x=0,y=0)
my_label.grid(column=0 , row = 0)




#button
# def button_clicked():
#     my_label.config(text = "i got clicked ")

button  = Button(text = "click me ")
button.grid(column=1 , row = 1)

button2  = Button(text = "click me first ")
button2.grid(column=2 , row = 0)

# Entry

input = Entry(width=10)
input.grid(column=3, row = 2)


window.mainloop()
