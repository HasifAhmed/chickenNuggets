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
    open_f = csv.reader(f) #open_f is a csv.reader object
    employment = {}
    
    #for every line
    for row in open_f:
        try:
            employment[row[0]]=float(row[1])
        except:
            continue
    
    chance = random.random() * 100
    jobs = list(employment.keys()) 
    x = 0 #responsible for the case of unemployed 
    wherearewe = 0 #used to adjust percentages
    for i in jobs:
        if chance < employment[i] + wherearewe: #checks the chance in the adjusted percentages 
            print(i) #prints job 
            x = 1
            break
        wherearewe = employment[i] + wherearewe #adjusts the range for percentages for the chance variable to view 
       
    if x == 0:
        print("Unemployed")


read('occupations.csv')

