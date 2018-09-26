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
        employment[row['Job Class']]=float(row['Percentage']) 

    del employment['Total']
    return employment

def retjob(file):
    employment = read(file)
    chance = random.uniform(0,99.8)
    for i in employment:
        chance -= employment[i]
        if chance <= 0:  
            return i #return job 




