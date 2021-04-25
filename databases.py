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
                upvotes integer,
                typeof)""")

        conn.commit() 
        conn.close() 

    #access the database, adds info to table, saves it
    def submit(self, first_name, last_name, email, complaint, typeof): 
        #connect to the database 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor()
        c.execute("INSERT INTO complaints VALUES (:id, :first, :last, :email, :complaint, :typeof, :upvotes)", 
            {'id':hash(complaint),
             'first':first_name, 
             'last':last_name,
             'email':email,
             'complaint':complaint,
             'typeof':typeof,
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
    def delete(self, deletion): 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor()
        c.execute("DELETE from complaints WHERE id="+str(deletion))
        conn.commit()
        conn.close()

    #accumulation function that adds 1 to the upvote counter
    def add_vote(self, compar):
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor()
        c.execute("UPDATE complaints SET upvotes = upvotes + 1 WHERE id =" + str(compar))

        conn.commit()
        conn.close() 

test = DatabaseStorage()

#creating the database if it does not already exist
try: 
    test.creation() 
except sqlite3.OperationalError:
    pass
 

#test.submit("jabar","awad","jawad@wesleyan.edu","I hate it here", 1)
#print(test.query())
#test.add_vote(2196838585774839428)
#print(test.query())
#test.delete(2196838585774839428)
#print(test.query())

print(test.query())