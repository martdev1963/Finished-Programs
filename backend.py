
import sqlite3

class Database:

    # --------------------------------------------------------------------------** FUNCTION DEFINITIONS **------------------------------------------------------------------------------------------

    # database connection function... path of the databse file is sent to the db parameter...
    def __init__(self, db):  # constructer... self refers to the Database class object instance being passed to __init__() when the frontend.py script runs...
        self.conn=sqlite3.connect(db) #  database connection object...
        self.cur=self.conn.cursor() # cursor object...  now cur is an attribute of the self object (Database class object: database) its no longer an object all its own...
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)") # sql statement...
        self.conn.commit()
#        conn.close()

   #  self refers to the Database class object instance, database...
    def insert(self, title, author, year, isbn):
        #conn=sqlite3.connect("books.db")
        #cur=conn.cursor()                                    # note the tuple passed as a second argument to the execute function...
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)",(title,author,year,isbn)) # sql statement... # NULL is for the id which is the primary key...it is auto incremented by python...
        self.conn.commit()
#        conn.close()


    def view(self):
        #conn=sqlite3.connect("books.db")
        #cur=conn.cursor()
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
#        self.conn.close()
        return rows


    def search(self, title="", author="", year="", isbn=""):
        #conn=sqlite3.connect("books.db")
        #cur=conn.cursor()
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn)) # implementing an OR search...
        rows=self.cur.fetchall()
#        conn.close()
        return rows


    def delete(self, id):
        #conn=sqlite3.connect("books.db")
        #cur=conn.cursor()                                    # note the tuple passed as a second argument to the execute function...
        self.cur.execute("DELETE FROM book WHERE id=?", (id,)) # sql statement... # NULL is for the id which is the primary key...it is auto incremented by python...
        self.conn.commit()
#        conn.close()


    def update(self, id,title,author,year,isbn):
        #conn=sqlite3.connect("books.db")
        #cur=conn.cursor()                                    # note the tuple passed as a second argument to the execute function...
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id)) # note how the tuple parameters follow suit with the order of the sql statement
        self.conn.commit()
#        conn.close()

    def __del__(self):
        self.conn.close()  # the script closes when it reaches this line of code...
        # hence thats why its last...
    # -------------------------------------------------------------------------** FUNCTION CALLS FOR UNIT TESTING **-----------------------------------------------------------------------------
    # python -m pip install -U pip
    # function call to connection object...
    #insert("The Sun","Sally Gremaude",2000,98734456745647)
    #print(search(author="Samuel Ericke"))
    #delete(4)
    #update(3,"The Moon","Samuel Ericke",2016,8765544332233)
    #print(view())
