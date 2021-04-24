
from functools import partial
import sqlite3

#Class for database storage
class DatabaseStorage(): 
    def __init__(self): 
        self.first_name = "" 
        self.last_name = "" 
        self.email = "" 
        self.complaint = "" 

    def submit(self): 
        #connect to the database 
        conn = sqlite3.connect("WesComplain_library_info.db")
        c=conn.cursor 
        c.execute("INSERT INTO complaints VALUES (:first, :last, :email, :complaint)", 
            {'first':self.first_name, 
             'last':self.last_name,
             'email':self.email,
             'complaint':self.complaint
            }    
        )
        conn.commit() 
        conn.close() 