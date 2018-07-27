"""----------------------------------------------------------------------------------------------------------------------------------------
                                        /////////////////////////////////////////////////////
                                        /                   **FRONT-END**                   /
                                        /                 **DOCUMENTATION**                 /
                                        /    Martin Batista - python progrmr  07/24/2018    /
                                        /////////////////////////////////////////////////////
FRONT-END: tKinter GUI
BACK-END: Sqlite3
*FEATURES/REQUIREMENTS*

A program that stores this book information:
Title, Author
Year, ISBN

User can:
.Show list of current record (listbox widget)
.Search current entry
.Add Entry
.Update Selected
.Delete Selected
.Close

Will be using grid method for the GUI.

Future scaling, revisioning:
Can create another function that clears the entry fields.
---------------------------------------------------------------------------------------------------------------------------------------------"""
from tkinter import *
import backend  # functions


# WRAPPER FUNCTIONS THAT CONNECT THE BUTTONS TO THE BACKEND FUNCTIONS...

# this function is called by simply selecting an entry or tuple from the listbox object...its not triggered by a button like the other wrapper functions...
# list1.bind('<<ListboxSelect>>',get_selected_row)...
def get_selected_row(event):      # note: the curselection() method returns tuples...
    try: # prevents IndexError exception from being thrown when user clicks an empty listbox...
        global selected_tuple # now selected_tuple is a global variable recognized throughout the code...
        index=list1.curselection()[0] # this trick will grab the first item with index 0 per tuple...otherwise the curselection() output will return tuples like this: (2,) (3,) etc...
        selected_tuple=list1.get(index) # returns tuple at selected index...                                                                                          # ^ index 0 of this single tuple...
    #    return selected_tuple
    #    print(event)
    #    print(type(event))
        # the following code will delete or purge the entry fields and will insert(), distribute the selected tuple into the respective entry fields thus displaying it to the user...
        e1.delete(0,END)
        e1.insert(END,selected_tuple[1]) # title has an index of [1], the id is the primary key and it has an index of [0]...
        e2.delete(0,END)
        e2.insert(END,selected_tuple[2]) # author has an index of [2]
        e3.delete(0,END)
        e3.insert(END,selected_tuple[3]) # year has an index of [3]
        e4.delete(0,END)
        e4.insert(END,selected_tuple[4]) # isbn has an index of [4]
    except IndexError:
        pass

#print(END)


# b1 button...text="View All"
def view_command():
    list1.delete(0,END) # prevents program from inserting duplicate entries over and over everytime you press View All button...
    for row in backend.view(): # view() method returns a list of tuples...
        list1.insert(END,row) # insert list of tuples into listbox object...

# b2=Button(window,text="Search Entry"
def search_command():
    list1.delete(0,END)
    for row in backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()): # stringVar objects getting strings from user entry...
        list1.insert(END,row) # insert the  found strings into the listbox object...

# b3=Button(window,text="Add Entry"
def add_command():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()) # insert new entry into database...
    list1.delete(0,END) # first clear the list...
    list1.insert(END,(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())) # then display the new entry to show the user's input...
    # note the tuple being used so that the new entry display's as a row and not multiple lines...

# b5=Button(window,text="Delete selected"
def delete_command(): # passing global variable selected_tuple[0]...
    backend.delete(selected_tuple[0]) # will delete the selected_tuple at index[0] for that single tuple returned...
    # now you won't get the TypeError: get_selected_row() missing 1 required positional argument: 'event' cuz you are not passing the event arugment to delete_command()...


def update_command(): # getting the updated data from the entry fields and updating the database...notice the get() methods...
    backend.update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(),isbn_text.get()) # will delete the selected_tuple at index[0] for that single tuple returned...
    print(selected_tuple[0],selected_tuple[1],selected_tuple[2],selected_tuple[3],selected_tuple[4])




window=Tk()  # all code goes after here...  Tk() not tk() ---> NameError: name 'tk' is not defined

window.wm_title("BookStore App - powered by Python")


# label objects and their x y coordinates...
l0=Label(window,text="Martin Batista Python Prgrmr - Guavadream Media Software")
l0.grid(row=0,column=0)

l1=Label(window,text="Title")
l1.grid(row=1,column=0)

l2=Label(window,text="Author")
l2.grid(row=1,column=2)

l3=Label(window,text="Year")
l3.grid(row=2,column=0)

l4=Label(window,text="ISBN")
l4.grid(row=2,column=2)

# entry objects and their x y coordinates...
title_text=StringVar() # object for user input...
e1=Entry(window,textvariable=title_text)
e1.grid(row=1,column=1)

author_text=StringVar() # object for user input...
e2=Entry(window,textvariable=author_text)
e2.grid(row=1,column=3)

year_text=StringVar() # object for user input...
e3=Entry(window,textvariable=year_text)
e3.grid(row=2,column=1)

isbn_text=StringVar() # object for user input...
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=2,column=3)


# list box object and its x y coordinates...
list1=Listbox(window, height=6,width=35)
list1.grid(row=3,column=0,rowspan=6,columnspan=2)

# scrollnbar object and its x y coordinates...
sb1=Scrollbar(window)
sb1.grid(row=3,column=2,rowspan=6)

list1.configure(yscrollcommand=sb1.set)  # tell the list object about the scrollbar object...
sb1.configure(command=list1.yview) # tell the scrollbar object about the list object...

# associating or binding the wrapper function: get_selected_row to the listbox object...so by selecting an item in the listbox, you call the get_selected_row() functon...
list1.bind('<<ListboxSelect>>',get_selected_row) # bind() method takes 2 arguments... an event type and a function that you want to bind to the event type...


# button objects and their x y coordinates...triggering their associated wrapper functions...
b1=Button(window,text="View All", width=12, command=view_command) # python would normally run or call this function if passed like this...view_command() with parentheses...
b1.grid(row=3,column=3)

b2=Button(window,text="Search Entry", width=12, command=search_command)  # this is why we don't use parentheses...Python/tkinter then knows to wait for button to call it...
b2.grid(row=4,column=3)

b3=Button(window,text="Add Entry", width=12, command=add_command)
b3.grid(row=5,column=3)

b4=Button(window,text="Update selected", width=12, command=update_command)
b4.grid(row=6,column=3)

b5=Button(window,text="Delete selected", width=12, command=delete_command)
b5.grid(row=7,column=3)

b6=Button(window,text="Close", width=12, command=window.destroy) # closes the app...
b6.grid(row=8,column=3)

window.mainloop()  # all code goes before here...


#------------------------------------------------------------------------------** Found Bug **------------------------------------------------------------------------------------
"""----------------------------------- This occurs when calling the get_selected_row() function by clicking into the listbox object...-------------------------------------------
DEBUGGING OUTPUT:
Exception in Tkinter callback
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/tkinter/__init__.py", line 1702, in __call__
    return self.func(*args)
  File "frontend.py", line 35, in get_selected_row
    index=list1.curselection()[0] # this trick will grab the first item with index 0 per tuple...otherwise the curselection() output will return tuples like this: (2,) (3,) etc...
IndexError: tuple index out of range

must write an IndexError Try block...

** To make an executable file run this ** This creates a single executable file...otherwise you get a bunch of support files that
are actually good for troubleshooting... include the --onefile parameter...
pyinstaller --onefile frontend.py
This command generates a terminal command line in the background of your GUI...to avoid this type in this other parameter called --windowed
pyinstaller --onefile --windowed frontend.py



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"""
