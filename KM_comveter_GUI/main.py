from tkinter import *

window = Tk()
window.title("My first GUI program")
window.minsize(200,200)
window.config(padx=50, pady=50)

km_converter = Label(text="0")
km_converter.grid(column=1,row=1)

#miles
mile=Label(text="Miles")
mile.grid(column=2, row=0)
#equal to
equal_to = Label(text="Is equal to: ")
equal_to.grid(column=0, row=1)
#km
km = Label(text="KM")
km.grid(column=2,row=1)

def press_button():
    km_converter.config(text="0")
    new_input = int(get_input.get())
    converted = round(new_input*1.60934,2)
    km_converter.config(text=converted)


cal_button= Button(text="click me", command=press_button)
cal_button.grid(column=2, row=1)


get_input = Entry()
get_input.grid(column=1, row=0)



window.mainloop()
