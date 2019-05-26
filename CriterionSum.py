# -*- coding: utf-8 -*-
"""
Created on Mon May 13 10:46:49 2019

@author: Anton
"""
#Imports desired modules
import numpy as np
import pandas as pd
#Imports the desired files
df = pd.read_csv('KriteriumNy.csv')
df2 = pd.read_csv('TestDirekt1.csv')
df3 = pd.read_csv('Testuppfoljning2Ny.csv')
df4 = pd.read_csv('Testuppfoljning3Ny.csv')


#Creates dictionaries for the desired values that will be used later
listaEnkel1 = {}
listaSvar1 = {}
listaEnkel2 = {}
listaSvar2 = {}
listaEnkel3 = {}
listaSvar3 = {}
#Removing the undesired variables from the dataframes
dfny = df.drop(['Unnamed: 0'], axis = 1)
df2ny = df2.drop(['age', 'sex', 'Unnamed: 0', 'runda', 'guess', 'cue','difficulty'],axis=1)
df3ny = df3.drop(['age', 'sex', 'Unnamed: 0', 'runda', 'guess', 'cue','difficulty'],axis=1)
df4ny = df4.drop(['age', 'sex', 'Unnamed: 0', 'runda', 'guess', 'cue','difficulty'],axis=1)
#Sorts the values in ascending order on subject and correct answer
dfny2 = dfny.sort_values(['subject', 'correct_answer'], ascending =[1, 1])
df2ny2 = df2ny.sort_values(['subject', 'correct_answer'], ascending =[1, 1])
df3ny2 = df3ny.sort_values(['subject', 'correct_answer'], ascending =[1, 1])
df4ny2 = df4ny.sort_values(['subject', 'correct_answer'], ascending =[1, 1])
#Resets the index
dfny3 = dfny2.reset_index() 
df2ny3 = df2ny2.reset_index()
df3ny3 = df3ny2.reset_index()
df4ny3 = df4ny2.reset_index()
#Filling the NaN values with zeros
dfny4 = dfny3.fillna(0)
df2ny4 = df2ny3.fillna(0)
df3ny4 = df3ny3.fillna(0)
df4ny4 = df4ny3.fillna(0)

#Merges the lists in order to calculate the values
dfmergadtest1 =  pd.merge(dfny4, df2ny4, left_index=True, right_index=True)
dfmergadtest2 =  pd.merge(dfny4, df3ny4, left_index=True, right_index=True)
dfmergadtest3 =  pd.merge(dfny4, df4ny4, left_index=True, right_index=True)

#Loops that assigns criteiron values to the lists. Criterion value is sorted by subject
for index, row in dfmergadtest1.iterrows():
    if row['criterion'] == 1 and row['difficulty'] == 2.0 and row['rattad'] != 0.0:
                namn = (row['subject_y'])
                if namn not in listaEnkel1:
                    listaEnkel1[namn] = 1
                else:
                    b = listaEnkel1[namn]
                    a = b + 1
                    listaEnkel1[namn] = a



for index0, row0 in dfmergadtest1.iterrows():
    if row0['criterion'] == 1 and row0['difficulty'] == 1.0 and row0['rattad'] != 0.0:
                namn0 = (row0['subject_y'])
                if namn0 not in listaSvar1:
                    listaSvar1[namn0] = 1
                else:
                    b0 = listaSvar1[namn0]
                    a0 = b0 + 1
                    listaSvar1[namn0] = a0

for index1, row1 in dfmergadtest2.iterrows():
    if row1['criterion'] == 1 and row1['difficulty'] == 2.0 and row1['rattad'] != 0.0:
                namn1 = (row1['subject_y'])
                if namn1 not in listaEnkel2:
                    listaEnkel2[namn1] = 1
                else:
                    b1 = listaEnkel2[namn1]
                    a1 = b1 + 1
                    listaEnkel2[namn1] = a1



for index2, row2 in dfmergadtest2.iterrows():
    if row2['criterion'] == 1 and row2['difficulty'] == 1.0 and row2['rattad'] != 0.0:
                namn2 = (row2['subject_y'])
                if namn2 not in listaSvar2:
                    listaSvar2[namn2] = 1
                else:
                    b2 = listaSvar2[namn2]
                    a2 = b2 + 1
                    listaSvar2[namn2] = a2

for index3, row3 in dfmergadtest3.iterrows():
    if row3['criterion'] == 1 and row3['difficulty'] == 2.0 and row3['rattad'] != 0.0:
                namn3 = (row3['subject_y'])
                if namn3 not in listaEnkel3:
                    listaEnkel3[namn3] = 1
                else:
                    b3 = listaEnkel3[namn3]
                    a3 = b3 + 1
                    listaEnkel3[namn3] = a3



for index4, row4 in dfmergadtest3.iterrows():
    if row4['criterion'] == 1 and row4['difficulty'] == 1.0 and row4['rattad'] != 0.0:
                namn4 = (row4['subject_y'])
                if namn4 not in listaSvar3:
                    listaSvar3[namn4] = 1
                else:
                    b4 = listaSvar3[namn4]
                    a4 = b4 + 1
                    listaSvar3[namn4] = a4


#Converting dictionaries to lists
#Removing undesired characters from lists
enkel1 = [ [k,v] for k, v in listaEnkel1.items() ]
enkel2 = []
for n in enkel1:
    for j in n:
        if j == '(':
            enkel2.append('')
        elif j == ')':
            enkel2.append('')
        elif j == ',':
            enkel2.append('')
        elif j == ':':
            enkel2.append('')
        else:
            enkel2.append(j)
    
enkel3 = []
for i in enkel2:
    if isinstance(i, int) == True:
        enkel3.append(i)
        continue
    elif isinstance(i, float) == True:
        enkel3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                enkel3.append(j)
                continue
            elif isinstance(j, float) == True:
                enkel3.append(j)
                continue
            else:
                enkel3.append(j.replace('(', '').replace(')', '').replace(',', ''))




svar1 = [ [k,v] for k, v in listaSvar1.items() ]
svar2 = []
for n in svar1:
    for j in n:
        if j == '(':
            svar2.append('')
        elif j == ')':
            svar2.append('')
        elif j == ',':
            svar2.append('')
        elif j == ':':
            svar2.append('')
        else:
            svar2.append(j)
    
svar3 = []
for i in svar2:
    if isinstance(i, int) == True:
        svar3.append(i)
        continue
    elif isinstance(i, float) == True:
        svar3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                svar3.append(j)
                continue
            elif isinstance(j, float) == True:
                svar3.append(j)
                continue
            else:
                svar3.append(j.replace('(', '').replace(')', '').replace(',', ''))


enkeltest2 = [ [k,v] for k, v in listaEnkel2.items() ]
enkeltest2_2 = []
for n in enkeltest2:
    for j in n:
        if j == '(':
            enkeltest2_2.append('')
        elif j == ')':
            enkeltest2_2.append('')
        elif j == ',':
            enkeltest2_2.append('')
        elif j == ':':
            enkeltest2_2.append('')
        else:
            enkeltest2_2.append(j)
    
enkeltest2_3 = []
for i in enkeltest2_2:
    if isinstance(i, int) == True:
        enkeltest2_3.append(i)
        continue
    elif isinstance(i, float) == True:
        enkeltest2_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                enkeltest2_3.append(j)
                continue
            elif isinstance(j, float) == True:
                enkeltest2_3.append(j)
                continue
            else:
                enkeltest2_3.append(j.replace('(', '').replace(')', '').replace(',', ''))




svartest2_1 = [ [k,v] for k, v in listaSvar2.items() ]
svartest2_2 = []
for n in svartest2_1:
    for j in n:
        if j == '(':
            svartest2_2.append('')
        elif j == ')':
            svartest2_2.append('')
        elif j == ',':
            svartest2_2.append('')
        elif j == ':':
            svartest2_2.append('')
        else:
            svartest2_2.append(j)
    
svartest2_3 = []
for i in svartest2_2:
    if isinstance(i, int) == True:
        svartest2_3.append(i)
        continue
    elif isinstance(i, float) == True:
        svartest2_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                svartest2_3.append(j)
                continue
            elif isinstance(j, float) == True:
                svartest2_3.append(j)
                continue
            else:
                svartest2_3.append(j.replace('(', '').replace(')', '').replace(',', ''))

enkeltest3_1 = [ [k,v] for k, v in listaEnkel3.items() ]
enkeltest3_2 = []
for n in enkeltest3_1:
    for j in n:
        if j == '(':
            enkeltest3_2.append('')
        elif j == ')':
            enkeltest3_2.append('')
        elif j == ',':
            enkeltest3_2.append('')
        elif j == ':':
            enkeltest3_2.append('')
        else:
            enkeltest3_2.append(j)
    
enkeltest3_3 = []
for i in enkeltest3_2:
    if isinstance(i, int) == True:
        enkeltest3_3.append(i)
        continue
    elif isinstance(i, float) == True:
        enkeltest3_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                enkeltest3_3.append(j)
                continue
            elif isinstance(j, float) == True:
                enkeltest3_3.append(j)
                continue
            else:
                enkeltest3_3.append(j.replace('(', '').replace(')', '').replace(',', ''))



svartest3_1 = [ [k,v] for k, v in listaSvar3.items() ]
svartest3_2 = []
for n in svartest3_1:
    for j in n:
        if j == '(':
            svartest3_2.append('')
        elif j == ')':
            svartest3_2.append('')
        elif j == ',':
            svartest3_2.append('')
        elif j == ':':
            svartest3_2.append('')
        else:
            svartest3_2.append(j)
    
svartest3_3 = []
for i in svartest3_2:
    if isinstance(i, int) == True:
        svartest3_3.append(i)
        continue
    elif isinstance(i, float) == True:
        svartest3_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                svartest3_3.append(j)
                continue
            elif isinstance(j, float) == True:
                svartest3_3.append(j)
                continue
            else:
                svartest3_3.append(j.replace('(', '').replace(')', '').replace(',', ''))

###########################################################################################################
#Creating an array
#Calculates the size of the array
#Reshapes the array
#Creates a dataframe with the desired columns                
        
nyArrayEnkelTest1 = np.array(enkel3)
size0 = int((nyArrayEnkelTest1.size)/2)
nyArrayEnkelTest1_2 = nyArrayEnkelTest1.reshape(size0,2)           
nyArrayEnkelTest1_3 = pd.DataFrame(nyArrayEnkelTest1_2, columns=['subject', 'antalRattEnkelTest1'])

nyArraySvarTest1 = np.array(svar3)
size1 = int((nyArraySvarTest1.size)/2)
nyArraySvarTest1_2 = nyArraySvarTest1.reshape(size1,2)
nyArraySvarTest1_3 = pd.DataFrame(nyArraySvarTest1_2, columns=['subject', 'antalRattSvarTest1'])

nyArrayEnkelTest2 = np.array(enkeltest2_3)
size2 = int((nyArrayEnkelTest2.size)/2)
nyArrayEnkelTest2_2 = nyArrayEnkelTest2.reshape(size2,2)
nyArrayEnkelTest2_3 = pd.DataFrame(nyArrayEnkelTest2_2, columns=['subject', 'antalRattEnkelTest2'])

nyArraySvarTest2 = np.array(svartest2_3)
size3 = int((nyArraySvarTest2.size)/2)
nyArraySvarTest2_2 = nyArraySvarTest2.reshape(size3,2)
nyArraySvarTest2_3 = pd.DataFrame(nyArraySvarTest2_2, columns=['subject', 'antalRattSvarTest2'])

nyArraytestEnkelTest3 = np.array(enkeltest3_3)
size4 = int((nyArraytestEnkelTest3.size)/2)
nyArrayEnkelTest3_2 = nyArraytestEnkelTest3.reshape(size4,2)
nyArrayEnkelTest3_3 = pd.DataFrame(nyArrayEnkelTest3_2, columns=['subject', 'antalRattEnkelTest3'])

nyArraySvarTest3 = np.array(svartest3_3)
size5 = int((nyArraySvarTest3.size)/2)
nyArraySvarTest3_2 = nyArraySvarTest3.reshape(size5,2)
nyArraySvarTest3_3 = pd.DataFrame(nyArraySvarTest3_2, columns=['subject', 'antalRattSvarTest3'])

#Merges dataframes so that all the desired values are on the same dataframe
df_outer = pd.merge(nyArrayEnkelTest1_3, nyArraySvarTest1_3, on='subject', how='outer')
df_outer2 = pd.merge(nyArrayEnkelTest2_3, nyArraySvarTest2_3, on='subject', how='outer')
df_outer3 = pd.merge(nyArrayEnkelTest3_3, nyArraySvarTest3_3, on='subject', how='outer')
df_outer4 = pd.merge(df_outer, df_outer2, on='subject', how='outer')
df_outer5 = pd.merge(df_outer4, df_outer3, on='subject', how='outer' )


#Prints dataframe to csv file
df_outer5.to_csv('CriterionLevel1Ny.csv')

