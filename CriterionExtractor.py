# -*- coding: utf-8 -*-
"""
Created on Wed May  1 18:52:32 2019

@author: Anton
"""

#Import desired modules
import pandas as pd
import numpy as np
#creates a dictionary for later use
kista = {}
#Opens a dataframe of the file
df = pd.read_csv('test1rattad.csv')


#Iterates over the desired columns, if rattad > 0 it is a succesfull retrieval
for index, row in df.iterrows():


            
#For every row the script extracts correct answer, difficulty and subject. The key in the dictionary
#is named after thos variables, in case there is already such a key in the dictionary the script will update the value for that key



        
    if row['runda'] != '?':
        if row['rattad'] == 0.0:
            y = (row['subject'],row['correct_answer'],row['difficulty'])
            if y not in kista:
                kista[y] = 0
        elif row['rattad'] > 0.0:

            
#If the key doesn't exist the script adds the new key and assigns the value 1 to it
            y = (row['subject'],row['correct_answer'],row['difficulty'])
            if y in kista:
                x = kista[y]
                u = x + 1
                kista[y] = u
            else:
                kista[y] = 1

#Creates a list from the dictionary
k2 = [ [k,v] for k, v in kista.items() ]
k3 = []
#For every n in the list k2 and for every item in n the loop replaces undesired characters with nothing
for n in k2:
    for j in n:
        if j == '(':
            k3.append('')
        elif j == ')':
            k3.append('')
        elif j == ',':
            k3.append('')
        else:
            k3.append(j)
    
k4 = []
#Does the same thing as above but skips ints and floats
for i in k3:
    if isinstance(i, int) == True:
        k4.append(i)
        continue
    elif isinstance(i, float) == True:
        k4.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                k4.append(j)
                continue
            elif isinstance(j, float) == True:
                k4.append(j)
                continue
            else:
                k4.append(j.replace('(', '').replace(')', '').replace(',', ''))
            
#Creates an array for the list k4
data = np.array(k4)
#Gets the size from k4 and divides it by 4 since there are 4 desired values
size = int((data.size)/4)
print(size)
#Reshapes the list to 4 columns
data2 = data.reshape(size,4)
#Creates a dataframe from the reshaped list and adds the desired column names
data3 = pd.DataFrame(data2, columns=['subject', 'correct_answer', 'difficulty', 'criterion'])
#Rmoves alla NaN values from the dataframe
data4 = data3.dropna()
#Sorts the dataframe after subject and correct answer in a ascending oreder
data5 = data4.sort_values(['subject', 'correct_answer'], ascending =[1, 1])
#Prints the dataframe to a csv file for later use
data5.to_csv('KriteriumNy.csv')
