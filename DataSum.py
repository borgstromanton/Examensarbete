# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:33:35 2019

@author: Anton
"""
#Import desired modules
#Pandas is used to create the dataframe
#numpy is used to create an array from lists
import pandas as pd
import numpy as np
#import and reads desired files
df1 = pd.read_csv('TestDirekt1.csv')
df2 = pd.read_csv('Testuppfoljning2Ny.csv')
df3 = pd.read_csv('Testuppfoljning3Ny.csv')
dfstudy1 = pd.read_csv('study.csv')
dfstudy2 = pd.read_csv('studyuppfoljning2.csv')
dfstudy3 = pd.read_csv('studyuppfoljning3.csv')



#Removes the undesired columns from the dataframes
datatest1 = df1.drop(['age','sex','runda','guess',  'cue', 'Unnamed: 0'],axis=1)
datatest2 = df2.drop(['age','sex','runda','guess',  'cue', 'Unnamed: 0'],axis=1)
datatest3 = df3.drop(['age','sex','runda','guess',  'cue', 'Unnamed: 0'],axis=1)
datastudy1 = dfstudy1.drop(['age','sex','runda','guess',  'cue', 'Unnamed: 0'],axis=1)
datastudy2 = dfstudy2.drop(['age','sex','runda','guess',  'cue', 'Unnamed: 0'],axis=1)
datastudy3 = dfstudy3.drop(['age','sex','runda','guess', 'cue', 'Unnamed: 0'],axis=1)

#Removes all NaN values
datatest1_NaN = datatest1.dropna()
datatest2_NaN = datatest2.dropna()
datatest3_NaN = datatest3.dropna()
datastudy1_NaN = datastudy1.dropna()
datastudy2_NaN = datastudy2.dropna()
datastudy3_NaN = datastudy3.dropna()


#Creates a new dataframe with the desired columns
dataframe_test1 = pd.DataFrame(datatest1_NaN, columns=['subject',  'rattad', 'difficulty', 'correct_answer' ])
dataframe_test2 = pd.DataFrame(datatest2_NaN, columns=['subject',  'rattad', 'difficulty', 'correct_answer' ])
dataframe_test3 = pd.DataFrame(datatest3_NaN, columns=['subject',  'rattad', 'difficulty', 'correct_answer' ])
dataframe_study1 = pd.DataFrame(datastudy1_NaN, columns=['subject',  'rattad', 'difficulty', 'correct_answer' ])
dataframe_study2 = pd.DataFrame(datastudy2_NaN, columns=['subject',  'rattad', 'difficulty', 'correct_answer' ])
dataframe_study3 = pd.DataFrame(datastudy3_NaN, columns=['subject',  'rattad', 'difficulty','correct_answer' ])



#Pivots the table so that all values are sorted the way they are going to be further analyzed in spss
dataframe_test1reset = dataframe_test1.reset_index().pivot_table(index='subject', columns=['difficulty','correct_answer'], values='rattad')
dataframe_test2reset = dataframe_test2.reset_index().pivot_table(index='subject', columns=['difficulty','correct_answer'], values='rattad')
dataframe_test3reset = dataframe_test3.reset_index().pivot_table(index='subject', columns=['difficulty','correct_answer'], values='rattad')
dataframe_study1reset = dataframe_study1.reset_index().pivot_table(index='subject', columns=['difficulty','correct_answer'], values='rattad')
dataframe_study2reset = dataframe_study2.reset_index().pivot_table(index='subject', columns=['difficulty','correct_answer'], values='rattad')
dataframe_study3reset = dataframe_study3.reset_index().pivot_table(index='subject', columns=['difficulty', 'correct_answer'], values='rattad')


#Calculates the sum of all the correct answers
dataframe_testSum1 = dataframe_test1reset.sum(axis = 1, skipna=True)
dataframe_testSum2 = dataframe_test2reset.sum(axis = 1, skipna=True)
dataframe_testSum3 = dataframe_test3reset.sum(axis = 1, skipna=True)
dataframe_studySum1 = dataframe_study1reset.sum(axis = 1, skipna=True)
dataframe_studySum2 = dataframe_study2reset.sum(axis = 1, skipna=True)
dataframe_studySum3 = dataframe_study3reset.sum(axis = 1, skipna=True)


#Creates a new column called antalrätt for the sum of the correct answers
dataframe_testFinal1 = pd.DataFrame(dataframe_testSum1, columns=['AntalRattTest1'])
dataframe_testFinal2 = pd.DataFrame(dataframe_testSum2, columns=['AntalRattTest2'])
dataframe_testFinal3 = pd.DataFrame(dataframe_testSum3, columns=['AntalRattTest3'])
dataframe_studyFinal1 = pd.DataFrame(dataframe_studySum1, columns=['AntalRattStudy1'])
dataframe_studyFinal2 = pd.DataFrame(dataframe_studySum2, columns=['AntalRattStudy2'])
dataframe_studyFinal3 = pd.DataFrame(dataframe_studySum3, columns=['AntalRattStudy3'])



#Creates dictionaries for every dataframe
listaEnkelTest1 = {}
listaSvarTest1 = {}
listaEnkelTest2 = {}
listaSvarTest2 = {}
listaEnkelTest3 = {}
listaSvarTest3 = {}
listaEnkelStudy1 = {}
listaSvarStudy1 = {}
listaEnkelStudy2 = {}
listaSvarStudy2 = {}
listaEnkelStudy3 = {}
listaSvarStudy3 = {}

#for every row check if difficulty is either 1 or 2 and if rattad is > 0.0 if it is 
#It adds the key to the dictionary, if the key already exists it updates the value
#It does this for all the corrected csvs and for all difficult and easy words for all the tests
for index, row in dataframe_test1.iterrows():
    if row['difficulty'] == 1.0 and row['rattad'] != 0.0:
        namn1 = (row['subject'])
        if namn1 not in listaSvarTest1:
            listaSvarTest1[namn1] = 1
        else:
            b = listaSvarTest1[namn1]
            a = b + 1
            listaSvarTest1[namn1] = a
        
    if row['difficulty'] == 2.0 and row['rattad'] != 0.0:
        namn = (row['subject'])
        if namn not in listaEnkelTest1:
            listaEnkelTest1[namn] = 1
        else:
            x = listaEnkelTest1[namn]
            u = x + 1
            listaEnkelTest1[namn] = u



##########################################################################
            
for index, row in dataframe_test2.iterrows():
    if row['difficulty'] == 1.0 and row['rattad'] != 0.0:
        namn1 = (row['subject'])
        if namn1 not in listaSvarTest2:
            listaSvarTest2[namn1] = 1
        else:
            b = listaSvarTest2[namn1]
            a = b + 1
            listaSvarTest2[namn1] = a
        
    if row['difficulty'] == 2.0 and row['rattad'] != 0.0:
        namn = (row['subject'])
        if namn not in listaEnkelTest2:
            listaEnkelTest2[namn] = 1
        else:
            x = listaEnkelTest2[namn]
            u = x + 1
            listaEnkelTest2[namn] = u


##########################################################################            
            
for index, row in dataframe_test3.iterrows():
    if row['difficulty'] == 1.0 and row['rattad'] != 0.0:
        namn1 = (row['subject'])
        if namn1 not in listaSvarTest3:
            listaSvarTest3[namn1] = 1
        else:
            b = listaSvarTest3[namn1]
            a = b + 1
            listaSvarTest3[namn1] = a
        
    if row['difficulty'] == 2.0 and row['rattad'] != 0.0:
        namn = (row['subject'])
        if namn not in listaEnkelTest3:
            listaEnkelTest3[namn] = 1
        else:
            x = listaEnkelTest3[namn]
            u = x + 1
            listaEnkelTest3[namn] = u

#############################################################################

for index, row in dataframe_study1.iterrows():
    if row['difficulty'] == 1.0 and row['rattad'] != 0.0:
        namn1 = (row['subject'])
        if namn1 not in listaSvarStudy1:
            listaSvarStudy1[namn1] = 1
        else:
            b = listaSvarStudy1[namn1]
            a = b + 1
            listaSvarStudy1[namn1] = a
        
    if row['difficulty'] == 2.0 and row['rattad'] != 0.0:
        namn = (row['subject'])
        if namn not in listaEnkelStudy1:
            listaEnkelStudy1[namn] = 1
        else:
            x = listaEnkelStudy1[namn]
            u = x + 1
            listaEnkelStudy1[namn] = u
          
            
################################################################################            

for index, row in dataframe_study2.iterrows():
    if row['difficulty'] == 1.0 and row['rattad'] != 0.0:
        namn1 = (row['subject'])
        if namn1 not in listaSvarStudy2:
            listaSvarStudy2[namn1] = 1
        else:
            b = listaSvarStudy2[namn1]
            a = b + 1
            listaSvarStudy2[namn1] = a
        
    if row['difficulty'] == 2.0 and row['rattad'] != 0.0:
        namn = (row['subject'])
        if namn not in listaEnkelStudy2:
            listaEnkelStudy2[namn] = 1
        else:
            x = listaEnkelStudy2[namn]
            u = x + 1
            listaEnkelStudy2[namn] = u


#################################################################################            
            
for index, row in dataframe_study3.iterrows():
    if row['difficulty'] == 1.0 and row['rattad'] != 0.0:
        namn1 = (row['subject'])
        if namn1 not in listaSvarStudy3:
            listaSvarStudy3[namn1] = 1
        else:
            b = listaSvarStudy3[namn1]
            a = b + 1
            listaSvarStudy3[namn1] = a
        
    if row['difficulty'] == 2.0 and row['rattad'] != 0.0:
        namn = (row['subject'])
        if namn not in listaEnkelStudy3:
            listaEnkelStudy3[namn] = 1
        else:
            x = listaEnkelStudy3[namn]
            u = x + 1
            listaEnkelStudy3[namn] = u
            


##################################################################################
#Converts the dictionaries to lists
#Removes all the undesired characters from the newly created lists

enkelTest1 = [ [k,v] for k, v in listaEnkelTest1.items() ]
enkelTest1_2 = []
for n in enkelTest1:
    for j in n:
        if j == '(':
            enkelTest1_2.append('')
        elif j == ')':
            enkelTest1_2.append('')
        elif j == ',':
            enkelTest1_2.append('')
        elif j == ':':
            enkelTest1_2.append('')
        else:
            enkelTest1_2.append(j)
    
enkelTest1_3 = []
for i in enkelTest1_2:
    if isinstance(i, int) == True:
        enkelTest1_3.append(i)
        continue
    elif isinstance(i, float) == True:
        enkelTest1_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                enkelTest1_3.append(j)
                continue
            elif isinstance(j, float) == True:
                enkelTest1_3.append(j)
                continue
            else:
                enkelTest1_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
                
    
svarTest1 = [ [k,v] for k, v in listaSvarTest1.items() ]
svarTest1_2 = []
for n in svarTest1:
    for j in n:
        if j == '(':
            svarTest1_2.append('')
        elif j == ')':
            svarTest1_2.append('')
        elif j == ',':
            svarTest1_2.append('')
        elif j == ':':
            svarTest1_2.append('')

        else:
            svarTest1_2.append(j)
    
svarTest1_3 = []
for i in svarTest1_2:
    if isinstance(i, int) == True:
        svarTest1_3.append(i)
        continue
    elif isinstance(i, float) == True:
        svarTest1_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                svarTest1_3.append(j)
                continue
            elif isinstance(j, float) == True:
                svarTest1_3.append(j)
                continue
            else:
                svarTest1_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
               
############################################################################################################                
                
enkelTest2 = [ [k,v] for k, v in listaEnkelTest2.items() ]
enkelTest2_2 = []
for n in enkelTest2:
    for j in n:
        if j == '(':
            enkelTest2_2.append('')
        elif j == ')':
            enkelTest2_2.append('')
        elif j == ',':
            enkelTest2_2.append('')
        else:
            enkelTest2_2.append(j)
    
enkelTest2_3 = []
for i in enkelTest2_2:
    if isinstance(i, int) == True:
        enkelTest2_3.append(i)
        continue
    elif isinstance(i, float) == True:
        enkelTest2_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                enkelTest2_3.append(j)
                continue
            elif isinstance(j, float) == True:
                enkelTest2_3.append(j)
                continue
            else:
                enkelTest2_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
                
    
svarTest2 = [ [k,v] for k, v in listaSvarTest2.items() ]
svarTest2_2 = []
for n in svarTest2:
    for j in n:
        if j == '(':
            svarTest2_2.append('')
        elif j == ')':
            svarTest2_2.append('')
        elif j == ',':
            svarTest2_2.append('')
        elif j == ':':
            svarTest2_2.append('')
        else:
            svarTest2_2.append(j)
    
svarTest2_3 = []
for i in svarTest2_2:
    if isinstance(i, int) == True:
        svarTest2_3.append(i)
        continue
    elif isinstance(i, float) == True:
        svarTest2_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                svarTest2_3.append(j)
                continue
            elif isinstance(j, float) == True:
                svarTest2_3.append(j)
                continue
            else:
                svarTest2_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
 

############################################################################################
               
enkelTest3 = [ [k,v] for k, v in listaEnkelTest3.items() ]
enkelTest3_2 = []
for n in enkelTest3:
    for j in n:
        if j == '(':
            enkelTest3_2.append('')
        elif j == ')':
            enkelTest3_2.append('')
        elif j == ',':
            enkelTest3_2.append('')
        elif j == ':':
            enkelTest3_2.append('')
        else:
            enkelTest3_2.append(j)
    
enkelTest3_3 = []
for i in enkelTest3_2:
    if isinstance(i, int) == True:
        enkelTest3_3.append(i)
        continue
    elif isinstance(i, float) == True:
        enkelTest3_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                enkelTest3_3.append(j)
                continue
            elif isinstance(j, float) == True:
                enkelTest3_3.append(j)
                continue
            else:
                enkelTest3_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
                
    
svarTest3 = [ [k,v] for k, v in listaSvarTest3.items() ]
svarTest3_2 = []
for n in svarTest3:
    for j in n:
        if j == '(':
            svarTest3_2.append('')
        elif j == ')':
            svarTest3_2.append('')
        elif j == ',':
            svarTest3_2.append('')
        elif j == ':':
            svarTest3_2.append('')
        else:
            svarTest3_2.append(j)
    
svarTest3_3 = []
for i in svarTest3_2:
    if isinstance(i, int) == True:
        svarTest3_3.append(i)
        continue
    elif isinstance(i, float) == True:
        svarTest3_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                svarTest3_3.append(j)
                continue
            elif isinstance(j, float) == True:
                svarTest3_3.append(j)
                continue
            else:
                svarTest3_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
                
 


################################################################################################               
enkelstudy1 = [ [k,v] for k, v in listaEnkelStudy1.items() ]
enkelStudy1_2 = []
for n in enkelstudy1:
    for j in n:
        if j == '(':
            enkelStudy1_2.append('')
        elif j == ')':
            enkelStudy1_2.append('')
        elif j == ',':
            enkelStudy1_2.append('')
        elif j == ':':
            enkelStudy1_2.append('')
        else:
            enkelStudy1_2.append(j)
    
enkelStudy1_3 = []
for i in enkelStudy1_2:
    if isinstance(i, int) == True:
        enkelStudy1_3.append(i)
        continue
    elif isinstance(i, float) == True:
        enkelStudy1_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                enkelStudy1_3.append(j)
                continue
            elif isinstance(j, float) == True:
                enkelStudy1_3.append(j)
                continue
            else:
                enkelStudy1_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
                
    
svarStudy1 = [ [k,v] for k, v in listaSvarStudy1.items() ]
svarStudy1_2 = []
for n in svarStudy1:
    for j in n:
        if j == '(':
            svarStudy1_2.append('')
        elif j == ')':
            svarStudy1_2.append('')
        elif j == ',':
            svarStudy1_2.append('')
        elif j == ':':
            svarStudy1_2.append('')
        else:
            svarStudy1_2.append(j)
    
svarStudy1_3 = []
for i in svarStudy1_2:
    if isinstance(i, int) == True:
        svarStudy1_3.append(i)
        continue
    elif isinstance(i, float) == True:
        svarStudy1_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                svarStudy1_3.append(j)
                continue
            elif isinstance(j, float) == True:
                svarStudy1_3.append(j)
                continue
            else:
                svarStudy1_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
 

####################################################################################               
enkelStudy2 = [ [k,v] for k, v in listaEnkelStudy2.items() ]
enkelStudy2_2 = []
for n in enkelStudy2:
    for j in n:
        if j == '(':
            enkelStudy2_2.append('')
        elif j == ')':
            enkelStudy2_2.append('')
        elif j == ',':
            enkelStudy2_2.append('')
        elif j == ':':
            enkelStudy2_2.append('')
        else:
            enkelStudy2_2.append(j)
    
enkelStudy2_3 = []
for i in enkelStudy2_2:
    if isinstance(i, int) == True:
        enkelStudy2_3.append(i)
        continue
    elif isinstance(i, float) == True:
        enkelStudy2_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                enkelStudy2_3.append(j)
                continue
            elif isinstance(j, float) == True:
                enkelStudy2_3.append(j)
                continue
            else:
                enkelStudy2_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
                
    
svarStudy2 = [ [k,v] for k, v in listaSvarStudy2.items() ]
svarStudy2_2 = []
for n in svarStudy2:
    for j in n:
        if j == '(':
            svarStudy2_2.append('')
        elif j == ')':
            svarStudy2_2.append('')
        elif j == ',':
            svarStudy2_2.append('')
        elif j == ':':
            svarStudy2_2.append('')
        else:
            svarStudy2_2.append(j)
    
svarStudy2_3 = []
for i in svarStudy2_2:
    if isinstance(i, int) == True:
        svarStudy2_3.append(i)
        continue
    elif isinstance(i, float) == True:
        svarStudy2_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                svarStudy2_3.append(j)
                continue
            elif isinstance(j, float) == True:
                svarStudy2_3.append(j)
                continue
            else:
                svarStudy2_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
                
#######################################################################################################
                
enkelStudy3 = [ [k,v] for k, v in listaEnkelStudy3.items() ]
enkelStudy3_2 = []
for n in enkelStudy3:
    for j in n:
        if j == '(':
            enkelStudy3_2.append('')
        elif j == ')':
            enkelStudy3_2.append('')
        elif j == ',':
            enkelStudy3_2.append('')
        elif j == ':':
            enkelStudy3_2.append('')
        else:
            enkelStudy3_2.append(j)
    
enkelStudy3_3 = []
for i in enkelStudy3_2:
    if isinstance(i, int) == True:
        enkelStudy3_3.append(i)
        continue
    elif isinstance(i, float) == True:
        enkelStudy3_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                enkelStudy3_3.append(j)
                continue
            elif isinstance(j, float) == True:
                enkelStudy3_3.append(j)
                continue
            else:
                enkelStudy3_3.append(j.replace('(', '').replace(')', '').replace(',', ''))
                
    
svarStudy3 = [ [k,v] for k, v in listaSvarStudy3.items() ]
svarStudy3_2 = []
for n in svarStudy3:
    for j in n:
        if j == '(':
            svarStudy3_2.append('')
        elif j == ')':
            svarStudy3_2.append('')
        elif j == ',':
            svarStudy3_2.append('')
        elif j == ':':
            svarStudy3_2.append('')
        else:
            svarStudy3_2.append(j)
    
svarStudy3_3 = []
for i in svarStudy3_2:
    if isinstance(i, int) == True:
        svarStudy3_3.append(i)
        continue
    elif isinstance(i, float) == True:
        svarStudy3_3.append(i)
        continue
    else:
        for j in i:
            if isinstance(j, int) == True:
                svarStudy3_3.append(j)
                continue
            elif isinstance(j, float) == True:
                svarStudy3_3.append(j)
                continue
            else:
                svarStudy3_3.append(j.replace('(', '').replace(')', '').replace(',', ''))

        
    
##################################################################################################
#Makes a dataframe from the list
#First i makes an array from the list
#Then the size of the array is measured
#The array is reshaped to desired size
#A dataframe is created with the desired columns
nyArrayEnkelTest1 = np.array(enkelTest1_3)
size0 = int((nyArrayEnkelTest1.size)/2)
nyArrayEnkelTest1_1 = nyArrayEnkelTest1.reshape(size0,2)
nyArrayEnkelTest1_2 = pd.DataFrame(nyArrayEnkelTest1_1, columns=['subject', 'antalRattEnkelTest1'])

nyArraySvarTest1 = np.array(svarTest1_3)
size1 = int((nyArraySvarTest1.size)/2)
nyArraySvarTest1_1 = nyArraySvarTest1.reshape(size1,2)
nyArraySvarTest1_2 = pd.DataFrame(nyArraySvarTest1_1, columns=['subject', 'antalRattSvarTest1'])
#print(enkelTest2)
nyArrayEnkelTest2 = np.array(enkelTest2_3)
size2 = int((nyArrayEnkelTest2.size)/2)
nyArrayEnkelTest2_1 = nyArrayEnkelTest2.reshape(size2,2)
nyArrayEnkelTest2_2 = pd.DataFrame(nyArrayEnkelTest2_1, columns=['subject', 'antalRattEnkelTest2'])

print(svarTest2_3)
nyArraySvarTest2 = np.array(svarTest2_3)
size3 = int((nyArraySvarTest2.size)/2)
size3_2 = size3 + 1
nyArraySvarTest2_1 = nyArraySvarTest2.reshape(size3,2)
nyArraySvarTest2_2 = pd.DataFrame(nyArraySvarTest2_1, columns=['subject', 'antalRattSvarTest2'])

nyArrayEnkelTest3 = np.array(enkelTest3_3)
size4 = int((nyArrayEnkelTest3.size)/2)
nyArrayEnkelTest3_1 = nyArrayEnkelTest3.reshape(size4,2)
nyArrayEnkelTest3_2 = pd.DataFrame(nyArrayEnkelTest3_1, columns=['subject', 'antalRattEnkelTest3'])

nyArraySvarTest3 = np.array(svarTest3_3)
size5 = int((nyArraySvarTest3.size)/2)
nyArraySvarTest3_1 = nyArraySvarTest3.reshape(size5,2)
nyArraySvarTest3_2 = pd.DataFrame(nyArraySvarTest3_1, columns=['subject', 'antalRattSvarTest3'])


#################################################################################################################


nyArrayEnkelStudy1 = np.array(enkelStudy1_3)
size = int((nyArrayEnkelStudy1.size)/2)
nyArrayEnkelStudy1_1 = nyArrayEnkelStudy1.reshape(size,2)
nyArrayEnkelStudy1_2 = pd.DataFrame(nyArrayEnkelStudy1_1, columns=['subject', 'antalRattEnkelStudy1'])

nyArraySvarStudy1 = np.array(svarStudy1_3)
size = int((nyArraySvarStudy1.size)/2)
nyArraySvarStudy1_1 = nyArraySvarStudy1.reshape(size,2)
nyArraySvarStudy1_2 = pd.DataFrame(nyArraySvarStudy1_1, columns=['subject', 'antalRattSvarStudy1'])

nyArrayEnkelStudy2 = np.array(enkelStudy2_3)
size = int((nyArrayEnkelStudy2.size)/2)
nyArrayEnkelStudy2_1 = nyArrayEnkelStudy2.reshape(size,2)
nyArrayEnkelStudy2_2 = pd.DataFrame(nyArrayEnkelStudy2_1, columns=['subject', 'antalRattEnkelStudy2'])

nyArraySvarStudy2 = np.array(svarStudy2_3)
size = int((nyArraySvarStudy2.size)/2)
nyArraySvarStudy2_1 = nyArraySvarStudy2.reshape(size,2)
nyArraySvarStudy2_2 = pd.DataFrame(nyArraySvarStudy2_1, columns=['subject', 'antalRattSvarStudy2'])

nyArrayEnkelStudy3 = np.array(enkelStudy3_3)
size = int((nyArrayEnkelStudy3.size)/2)
nyArrayEnkelStudy3_1 = nyArrayEnkelStudy3.reshape(size,2)
nyArrayEnkelStudy3_2 = pd.DataFrame(nyArrayEnkelStudy3_1, columns=['subject', 'antalRattEnkelStudy3'])

nyArraySvarStudy3 = np.array(svarStudy3_3)
size = int((nyArraySvarStudy3.size)/2)
nyArraySvarStudy3_1 = nyArraySvarStudy3.reshape(size,2)
nyArraySvarStudy3_2 = pd.DataFrame(nyArraySvarStudy3_1, columns=['subject', 'antalRattSvarStudy3'])





###########################################################################################################################

#Merging all the dataframe so all the values from all the test is in one big dataframe

df_outer = pd.merge(dataframe_testFinal1, nyArrayEnkelTest1_2, on='subject', how='outer')
df_outer1 = pd.merge(df_outer, nyArraySvarTest1_2, on='subject', how='outer')

df_outer2 = pd.merge(dataframe_testFinal2, nyArrayEnkelTest2_2, on='subject', how='outer')
df_outer3 = pd.merge(df_outer2, nyArraySvarTest2_2, on='subject', how='outer')

df_outer4 = pd.merge(dataframe_testFinal3, nyArrayEnkelTest3_2, on='subject', how='outer')
df_outer5 = pd.merge(df_outer4, nyArraySvarTest3_2, on='subject', how='outer')

df_outer6 = pd.merge(dataframe_studyFinal1, nyArrayEnkelStudy1_2, on='subject', how='outer')
df_outer7 = pd.merge(df_outer6, nyArraySvarStudy1_2, on='subject', how='outer')

df_outer8 = pd.merge(dataframe_studyFinal2, nyArrayEnkelStudy2_2, on='subject', how='outer')
df_outer9 = pd.merge(df_outer8, nyArraySvarStudy2_2, on='subject', how='outer')

df_outer10 = pd.merge(dataframe_studyFinal3, nyArrayEnkelStudy3_2, on='subject', how='outer')
df_outer11 = pd.merge(df_outer10, nyArraySvarStudy3_2, on='subject', how='outer')



df_outer12 = pd.merge(df_outer1, df_outer3, on='subject', how='outer')

df_outerTEST = pd.merge(df_outer12, df_outer5, on='subject', how='outer')

df_outer14 = pd.merge(df_outer7, df_outer9, on='subject', how='outer')

df_outerSTUDY = pd.merge(df_outer14, df_outer11, on='subject', how='outer')
#Prints dataframe to csv
df_outerSTUDY.to_csv('StudySamladNy.csv')
df_outerTEST.to_csv('TestSamladNy.csv')




