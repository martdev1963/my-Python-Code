from tkinter import *
#import tkinter as tk

#window = tk.Tk() # this works

# main window...All code goes in between these lines...window = Tk()  and window.mainloop()
window = Tk() # this works too.

# function that converts km to mi...
#def km_to_miles():
    #print(e1_value.get()) # the get() method of the StringVar object...
#    miles=float(e1_value.get())*1.6
#    t1.insert(END,miles) # place this value after the last entry...

# FUNCTION DEFINITION...
# function that converts from metric to SAE standard...
def kilogram_to_grams_pounds_ounces():
    # conversion formulae...
    grams=float(kilogram_entry_value.get())*1000
    pounds=float(kilogram_entry_value.get())*2.20462
    ounces=float(kilogram_entry_value.get())*35.274

    grams_display.delete("1.0", END)
    grams_display.insert(END,grams)
    pounds_display.delete("1.0", END)
    pounds_display.insert(END,pounds)
    ounces_display.delete("1.0", END)
    ounces_display.insert(END,ounces)

# widgets (widgets go within the main window)
#b1=Button(window,text="Execute",command=km_to_miles) # parameters, separated by commas...You just pass the function name without the function()

# BUTTON WIDGET... clicking the button will invoke function callback...
b1=Button(window,text="Execute",command=kilogram_to_grams_pounds_ounces) # parameters, separated by commas...You just pass the function name without the function()
#b1.pack()
# alternative way for .pack()

# button coordinate location on window object...
b1.grid(row=1,column=0)


# instantiate StringVar object for user entry...
kilogram_entry_value=StringVar()


# ENTRY WIDGET...

# label for entry user input widget...though its a separate widget for the label alone.
e_label=Label(window,text="Kg")
e_label.grid(row=0,column=0)

entry_kilogram=Entry(window,textvariable=kilogram_entry_value) # passing StringVar object so it can be displayed as user input...
entry_kilogram.grid(row=0,column=1) # entry widget coordinate....

#e1_value=StringVar() # instantiate a StringVar object...
#e1=Entry(window,textvariable=e1_value) # e1_value for the user input...
#e1.grid(row=0,column=1)

# OUTPUT WIDGETS...and their coordinates on the window object...
# this displays the output result in the text field widget t1
#t1=Text(window,height=1,width=20)
#t1.grid(row=0,column=2)

grams_display=Text(window,height=1,width=20)
grams_display.grid(row=0,column=2)

pounds_display=Text(window,height=1,width=20)
pounds_display.grid(row=0,column=3)

ounces_display=Text(window,height=1,width=20)
ounces_display.grid(row=0,column=4)



window.mainloop() # all code goes before this line...




"""
OUTPUT:
miles=e1_value.get()*1.6
TypeError: can't multiply sequence by non-int of type 'float'...solution: miles=float(e1_value.get())*1.6...convert user input string to float...
"""


"""
Traceback (most recent call last):
  File "script1.py", line 2, in <module>
    import Tkinter as tk
ModuleNotFoundError: No module named 'Tkinter'

for code interspection, do this:

invoke the python interactive shell...
    ipython

from tkinter import *

Button?
"""
