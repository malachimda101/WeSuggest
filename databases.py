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
        c.execute("CREATE TABLE complaints (id integer, first text, last text, email text, complaint text, typeof text, upvotes integer)")

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

    #access the database, adds info to table, saves it
    def submit(self, first_name, last_name, email, complaint, typeof): 
        #connect to the database 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor()

        query_table = self.query()
        for key in query_table:
            a_tuple = query_table[key]
            if a_tuple[0] == complaint:

                self.add_vote(key)

                conn.commit()
                conn.close() 
                return 
            
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
        
    #delete a specific complaint from the database
    def delete(self, deletion_list): 
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor()

        for deletion in deletion_list:
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

    #function to delete entire table
    def delete_all(self):
        conn = sqlite3.connect("WesSuggest_library_info.db")
        c = conn.cursor()
        c.execute("DELETE from complaints")
        conn.commit()
        conn.close()

    #function to return the complaint with the most upvotes, returns a list of multiple complaints if they are equal in count
    def highest_upvotes(self):
        import math 
        highest_count = -math.inf 
        highest = []
        query_table = self.query()

        for id in query_table: 
            a_tuple = query_table[id]
            if a_tuple[1] >= highest_count: 
                highest_count = a_tuple[1]
                highest.append(a_tuple[0])

        return highest 


test = DatabaseStorage()

#creating the database if it does not already exist
try: 
    test.creation() 
except sqlite3.OperationalError:
    pass
 

print(test.query())
#test.submit("jabar","awad","jawad@wesleyan.edu","I wish there was soap in my bathroom!", "Administrative")
#print(test.query())

#test.add_vote(-276299198530829792)
#print(test.query())

#test.delete(2196838585774839428)
#print(test.query())

#print(test.query())
#test.delete_all()

#test.submit("jabar","awad","jawad@wesleyan.edu","I hate it here", "Administrative")

#print(test.query())

#print(test.highest_upvotes())