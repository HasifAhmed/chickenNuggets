#Kormed: Aleksandra Koroza, Hasif Ahmed
#SoftDev1 pd8
#06: StI/O: Divine your Destiny!
#2018-09-13

#TASK 1: Write a Python script to read in the file and
#build an appropriate dictionary from it.
#Make sure the percentages are stored as numbers.

import csv
import random
#source: https://realpython.com/python-csv/
#reads and returns a dictionary
def read(file):
    f = open(file) #stores file info in file object "f"
    open_f = csv.DictReader(f) #open_f is a csv.reader object
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
        if chance <= 0: #checks the chance in the adjusted percentages 
            return i #prints job 




