from tkinter import *
from functools import partial
import sqlite3


#Class for database storage
class DatabaseStorage(): 
    def __init__(self): 
        print("Database object created.")

    #creates the database table
    def creation(self): 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor() 
        c.execute("""CREATE TABLE complaints (
                id integer, 
                first text, 
                last text,
                email text,
                complaint text,
                upvotes integer )""")

        conn.commit() 
        conn.close() 

    #access the database, adds info to table, saves it
    def submit(self, first_name, last_name, email, complaint): 
        #connect to the database 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor()
        c.execute("INSERT INTO complaints VALUES (:id, :first, :last, :email, :complaint, :upvotes)", 
            {'id':hash(complaint),
             'first':first_name, 
             'last':last_name,
             'email':email,
             'complaint':complaint,
             'upvotes':0
            }    
        )
        conn.commit() 
        conn.close() 

    #access information from the database using dicts
    def query(self):
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor()
        c.execute("SELECT id, complaint, upvotes FROM complaints")
        records = c.fetchall()

        query_table = {} 
        for record in records:
            key = record[0]
            value = (record[1], record[2])
            query_table[key] = value 
        
        conn.commit()
        conn.close()
        
        return query_table

    #delete a specific complaint from the database
    def delete(self, complaint, deletion): 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor()
        c.execute("DELETE from complaints WHERE complaint="+deletion)
        conn.commit()
        conn.close 

    def add_vote(self, id):
        map = self.query()
        map[id] += 1 

test = DatabaseStorage()
#test.creation()
#test.submit("jabar","awad","jawad@wesleyan.edu","I hate it here", 1)
print(test.query())