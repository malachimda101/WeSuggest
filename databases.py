from functools import partial
import sqlite3

class DatabaseStorage(): 
    def __init__(self): 
        self.first_name = "" 
        self.last_name = "" 
        self.email = "" 
        self.complaint = "" 

