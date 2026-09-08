from tkinter import *

from main import button

window = Tk()
window.title("Mile to Km converter")
window.minsize(width=500 , height=300)
window.config(padx=20,pady=20)
#Entries
entry = Entry(width=20)
entry.grid(column = 1, row =0)

my_label1 = Label(text = "Miles", font = ("Arial",24,"bold"))
my_label2 = Label(text = "is equal to ", font = ("Arial",24,"bold"))
my_label3 =  Label(text = " 0 ", font = ("Arial",24,"bold"))
my_label4 =  Label(text = " km ", font = ("Arial",24,"bold"))


my_label1.grid(column = 2, row =0 )
my_label2.grid(column = 0, row =1 )
my_label3.grid(column = 1, row =1 )
my_label4.grid(column = 2, row =1 )


def converter():
    km = round(float(entry.get())  * 1.60934  , 2)

    my_label3.config(text=km)

button = Button(text="Calculate" ,command=converter)
button.grid(column = 1, row =2 )

window.mainloop()

