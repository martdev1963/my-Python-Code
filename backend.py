"""------------------------------------------------------------------------------------------------------------------------------------
                                    /////////////////////////////////////////////////////
                                    /                   **BACK-END**                    /
                                    /                 **DOCUMENTATION**                 /
                                    /    Martin Batista - python progrmr  07/24/2018    /
                                    /////////////////////////////////////////////////////
-------------------------------------------------------------------------------------------------------------------------------------"""

import sqlite3


# ------------------------------------------------** FUNCTION DEFINITIONS **----------------------------------------------------

# database connection function...
def connect():
    conn=sqlite3.connect("books.db") #  database connection object...
    cur=conn.cursor() # cursor object...
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)") # sql statement...
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()                                    # note the tuple passed as a second argument to the execute function...
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn)) # sql statement... # NULL is for the id which is the primary key...it is auto incremented by python...
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows


def search(title="", author="", year="", isbn=""):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn)) # implementing an OR search...
    rows=cur.fetchall()
    conn.close()
    return rows


def delete(id):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()                                    # note the tuple passed as a second argument to the execute function...
    cur.execute("DELETE FROM book WHERE id=?", (id,)) # sql statement... # NULL is for the id which is the primary key...it is auto incremented by python...
    conn.commit()
    conn.close()


def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books.db")
    cur=conn.cursor()                                    # note the tuple passed as a second argument to the execute function...
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id)) # note how the tuple parameters follow suit with the order of the sql statement
    conn.commit()
    conn.close()




# --------------------------------------------------** FUNCTION CALLS FOR UNIT TESTING **------------------------------------------------------------

# function call to connection object...
#connect()
#insert("The Sun","Sally Gremaude",2000,98734456745647)
#print(search(author="Samuel Ericke"))
#delete(4)
#update(3,"The Moon","Samuel Ericke",2016,8765544332233)
#print(view())
