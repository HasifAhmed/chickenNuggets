#azrael - Jason Tung and Hasif Ahmed
#SoftDev1 pd8
#K17 -- Average
#2018-10-09
import copy
import sqlite3  # enable control of an sqlite database
import csv  # facilitates CSV I/O
import os

DB_FILE = "discobandit.db"

db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
c = db.cursor()  # facilitate db ops


# ==========================================================
# INSERT YOUR POPULATE CODE IN THIS ZONE

def createtable(filename, tablename):
    # creating the initial exec statement: declaring table name, columns and column definitions -------

    # --------------------------------------------------------------------------------------------------

    # executing row statements--------------------------------------------------------------------------
    with open(filename) as csvfile:
        reader = list(csv.DictReader(csvfile))
        headers = reader[0]
        command = "DROP TABLE IF EXISTS {0};".format(tablename)
        #print(command)
        c.execute(command)
        command = "CREATE TABLE IF NOT EXISTS {0}".format(tablename)
        command += "("
        for keys in headers:
                command+= keys + " BLOB,"
        command = command[:-1]+ ");"
        #print(command)
        #print(command)
        c.execute(command)
        headerstr = ""
        for header in headers:
            headerstr+=header + ","
        headerstr=headerstr[:-1]
        for row in reader:
            #print(row)
            vals = ""
            for k,v in row.items():
                vals += "'{0}'".format(v) + ","
            vals = vals[:-1]
            command = "INSERT INTO {0}({1}) VALUES({2});".format(tablename,headerstr, vals)
            #print(command)
            c.execute(command)
        #c.execute("SELECT * FROM {0};".format(tablename))
    # --------------------------------------------------------------------------------------------------

# ==========================================================
createtable("peeps.csv", 'peeps_info')
createtable('courses.csv', 'courses_info')

db.commit()  # save changes
db.close()  # close database


db = sqlite3.connect(DB_FILE)  # open if file exists, otherwise create
c = db.cursor()  # facilitate db ops

def createAvgtbl():
    avg = {} 
    count = []
    
    names = c.execute("SELECT name FROM peeps_info;") #pull the names of the students and put them into a list
    for n in names:
        #print(n[0]) #testing
        count.append(n[0])

    for name in count: #iterate through the list of names 
        total = 0
        num = 0.0
        #Have to execute every single time you want to iterate through the following data, or else it doesnt work
        info = c.execute("SELECT name, peeps_info.id, mark FROM peeps_info, courses_info WHERE peeps_info.id = courses_info.id;")
        for row in info: #iterate through the data
            if(name == row[0]): #if the name from the list matches the name from the row
                #print("Hello") #testing
                total += int(row[2]) #calculate the sum
                num += 1.0
        if( num != 0): #to avoid dividing by 0
            total /= num #calculate avg
            avg[name] = total #put into the dictionary
            #print(avg[name]) #testing
            
    c.execute("CREATE TABLE IF NOT EXISTS peeps_avg(name BLOB, average BLOB);") #create peeps_avg
    for k,v in avg.items(): #iterate through dictrionary with items() so u can access key and value 
        vals = ""
        vals += "'{0}'".format(k) + "," + "'{0}'".format(v) #what you are inputting 
        command = "INSERT INTO peeps_avg VALUES({0});".format(vals) #insert them 
        c.execute(command) #execute command 
    
        
    
    

createAvgtbl()
db.commit()  # save changes
db.close()  # close database


