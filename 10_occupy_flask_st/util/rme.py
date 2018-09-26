#Indeed: Sarar Aseer, Hasif Ahmed
#SoftDev1 pd8
#K10 -- Jinja Tuning
#2018-09-24


import csv
import random
#source: https://realpython.com/python-csv/
#reads and returns a dictionary
def read(file): 
    f = open(file) #stores file info in file object "f"
    open_f = csv.DictReader(f) #open_f is a csv.reader object (DictReader is better bc you can just use the name of the column)
    employment = {}
    
    #for every line
    for row in open_f:
        employment[row['Job Class']]=float(row['Percentage']) #able to use bc of DictReader

    del employment['Total'] #removing bottom layer 
    return employment

def retjob(file): #returns random occupation based on percentage
    employment = read(file)
    chance = random.uniform(0,99.8) #uniform to attain random float 
    for i in employment:
        chance -= employment[i]
        if chance <= 0:  
            return i #return job 




