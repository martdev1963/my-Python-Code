from tkinter import *
#import tkinter as tk

#window = tk.Tk() # this works

# main window...All code goes in between these lines...window = Tk()  and window.mainloop()
window = Tk() # this works too.

# function that converts km to mi...
def km_to_miles():
    #print(e1_value.get()) # the get() method of the StringVar object...
    miles=float(e1_value.get())*1.6
    t1.insert(END,miles) # place this value after the last entry...

# widgets (widgets go within the main window)
b1=Button(window,text="Execute",command=km_to_miles) # parameters, separated by commas...You just pass the function name without the function()
#b1.pack()
# alternative way for .pack()
b1.grid(row=0,column=0)

e1_value=StringVar() # instantiate a StringVar object...
e1=Entry(window,textvariable=e1_value) # e1_value for the user input...
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=2)




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
