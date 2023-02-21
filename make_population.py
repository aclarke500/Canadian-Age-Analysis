import pandas as pd
import random as rand
import matplotlib.pyplot as plt

# grab third (0 based) column from csv file and convert to list
age_meta_data=pd.read_csv("ages.csv").iloc[:,[2]].values.tolist()
ages=[]

for i in range(len(age_meta_data)):
    # grab data from list of list
    age = age_meta_data[i][0]
    # round after
    ages.append(round(1000*age))

buckets = []

sum_of_prev = 0 # sum of all prev elements

for i in range(len(ages)):
    buckets.append(sum_of_prev+ages[i])
    sum_of_prev+=ages[i]



max_num=sum(ages)


ages = [] # fuck it we clearing the variable

for c in range(10000):
    choice = rand.randint(0, max_num)

    for i in range(len(buckets)):
        if choice < buckets[i]:
            ages.append(i)
            break

tally = []

for i in range(101):
    tally.append(0)


for a in ages:
    tally[a]+=1



x_values=[]

for i in range(101):
    x_values.append(i)



