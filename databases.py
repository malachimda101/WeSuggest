
from functools import partial
import sqlite3

#Class for database storage
class DatabaseStorage(): 
    def __init__(self): 
        self.first_name = "" 
        self.last_name = "" 
        self.email = "" 
        self.complaint = "" 
        self.id = ""
        self.num_upvotes= ""

    def submit(self): 
        #connect to the database 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor 
        c.execute("INSERT INTO complaints VALUES (:id, :first, :last, :email, :complaint, :upvotes)", 
            {'id':self.id,
             'first':self.first_name, 
             'last':self.last_name,
             'email':self.email,
             'complaint':self.complaint,
             'upvotes':self.num_upvotes
            }    
        )
        conn.commit() 
        conn.close() 

    def query(self):
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor 
        c.execute("SELECT * oid FROM complaints")
        records = c.fetchall 

        query_table = {} 
        for record in records:
            key = record[0]
            value = (record[4], record[5])
            query_table[key] = value 
        
        conn.commit()
        conn.close()
        
        return query_table

    def delete(self, deletion): 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor
        c.execute("DELETE from complaints WHERE self.complaint="+deletion)
        conn.commit()
        conn.close 
