#Lonely:(Hasif Ahmed and no one else) 
#SoftDev1 pd8
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def createtable(filename, tablename,header):
    #creating the initial exec statement: declaring table name, columns and column definitions -------
    
    #--------------------------------------------------------------------------------------------------

    #executing row statements--------------------------------------------------------------------------
    with open(filename) as csvfile:
        readfile = csv.DictReader(csvfile)
        reader = csv.reader(csvfile)
        header = {}
        for row in reader:
            
        command = "CREATE TABLE " + tablename + " ("
        for columndef in header:
            command += columndef + "BLOB" + ","
        command = command[:-1] #remove last comma 
        command += ")"
        #print(command); #for testing
        c.execute(command)
        
        
        for row in readfile:
            #print (row['code']) #testing
            fill = "INSERT INTO " + tablename + " VALUES ("
            for columndef in header: #iterate through the column names to be able to retrieve the values aligned with the column name
                fill += "'" + row[columndef] + "'" + ","  
            fill = fill[:-1] #remove last comma 
            fill += ")"
            c.execute(fill)
    #--------------------------------------------------------------------------------------------------



#==========================================================
courses = {"code":"TEXT", "mark":"INTEGER", "id":"INTEGER"}
createtable('courses.csv',"courses",courses)

peeps = {"name":"TEXT", "age":"INTEGER", "id":"INTEGER"}
createtable('peeps.csv',"peeps",peeps)

db.commit() #save changes
db.close()  #close database


