# -*- coding: utf-8 -*-

"""

Created on Tue Apr 16 09:03:35 2019



@author: Anton

"""


import re





#Creates an empty list
trials = []



from dataclasses import dataclass, asdict




#Creates pattern for the for loop to match with the raw data
match_log_frame_start = r'[\t\W]+\*\*\* LogFrame Start \*\*\*'

match_cue = r'[\t\W]+Attribute1:'

match_guess = r'[\t\W]*test(i|I)tem(1?)\.RESP:'

match_test_guess = r'[\t\W]*target.RESP:'

match_correct_answer = r'[\t\W]*Attribute2:'

match_difficulty = r'[\t\W]*Attribute3:'

match_runda = r'[\t\W]*runda:'

match_subject =  r'[\W]*Subject:'

match_session = r'[\W]+Session:'

match_sex = r'[\W]*Sex:'
match_age = r'[\W]*Age:'
@dataclass(init=False)

class Trial:
    #Vilken runda det är
    
    runda : int
    
    #Cue Ordet

    cue: str

    # Gissning

    guess: str

    # Rätt Svar

    correct_answer: str

    # Svårighetsgrad

    difficulty: int

    rattad: int
    
    subject: int
    age: int
    sex: str
    

    def __init__(self):
        
        self.subject = None
        self.age = None
        self.sex = None
        
        self.runda = None
        
        self.cue = None

        self.guess = None

        self.correct_answer = None

        self.difficulty = None

        self.rattad = None
        

    def valid(self):

        return hasattr(self, 'cue')

    def __str__(self):
#Creates lists for the dataframe
        return f'Subject: {self.subject} Age: {self.age}, Sex: {self.sex}, Runda: {self.runda}, Cue: {self.cue}, Guess: {self.guess}, Correct_answer: {self.correct_answer}, Difficulty: {self.difficulty}, Corrected: {self.rattad}.'

        
#Recieves a string, strips it from excess and then returns the value as a string
def get_value(line):
    value = line.split(':')[1].strip()
    if value == '':

        return None



    return str(value)

#Recieves a string, strips it from excess and the returns the value as a int
def get_valueInt(line):
    value = line.split(':')[1].strip()
    if value == '':

        return None


    return int(value)

#Recieves a string, strips it and replaces every key that might have been pressed by mistake
def get_guess(line):
    value = line.split(':')[1].strip().replace('{ENTER}', "").replace(" ", "").replace('{SPACE}', "").replace('{SHIFT}', "").replace("{CAPSLOCK}", "").replace("{LEFTARROW}", "").replace("{RIGHTBRACKET}", "").replace("{CONTROL}", "").replace("{SHIFT}", "").replace("{TAB}", "").replace("{RIGHTBRACKET}", "").replace("?UNKOWN?", "" ).replace("{NUMLOCK}", "").replace("{LEFTBRACKET}", "")
    return str(value)



    
def get_runda(line):
    value = line.split(':')[1].strip()
    return value


#Opens a file  assigns current_trial to None
with open('input', 'r') as file:
    current_trial = None
#Starts a for loop for file that keeps track of index and iters over every line in the file
    for (num, line) in enumerate(file.readlines(), start=1):
#Sets up global variables for later use
        global svar
        global gissning2
        global subject
        global runda
        global sex
        global age
#Matches subject, sex, age and match log frame, appends it to the list and to the class       
        if re.match(match_subject, line):
            subject = get_valueInt(line)
        if re.match(match_sex, line):
            sex = get_value(line)
        if re.match(match_age, line):
            age = get_valueInt(line)
        if re.match(match_runda, line):
            runda = get_runda(line)
            
        if re.match(match_log_frame_start, line):
            if current_trial is not None and current_trial.valid():
                trials.append(current_trial)

            current_trial = Trial()            
        
#Matches the cue and also adds sex and age to the list
        elif re.match(match_cue, line):
            current_trial.cue = get_value(line)
            current_trial.sex = sex
            current_trial.age = age
#Matches the correct answer and also the subject
        elif re.match(match_correct_answer, line):
            svar = get_value(line)
            current_trial.correct_answer = get_value(line)
            current_trial.subject = subject


            
#Matches the subjects guess and adds it to the list            
        elif re.match(match_guess, line):
            gissning = get_guess(line)
            gissning2 = gissning.lower()
            current_trial.guess = get_guess(line)
            
#If the guess is correct it will add a value 1 if the guess is wrong it will add the value zero
#If the code doesnt know if the guess is correct or wrong it will print the correct answer and guess and wait for input from the user
#to judge if the guess is correct or not, i the user enters y(yes) the script will give the value 1 if anything else the script will add value 0
            if gissning2 == svar:
                current_trial.rattad = 1
            elif gissning2 == "vetej":
                current_trial.rattad = 0
            elif gissning2 == "VETEJ":
                current_trial.rattad = 0
            elif gissning2 == "":
                current_trial.rattad = 0
            elif gissning2 == 'vetinte':
                current_trial.rattad = 0
            elif gissning2 == 'dontknow':
                current_trial.rattad = 0
            elif gissning2 != svar:
                print(num+1, svar, gissning2)
                rattning = input()

                if rattning == "y":
                    current_trial.rattad = 1
                else:
                    current_trial.rattad = 0

#Does the same thing as above but on the guess from the test rounds.
        
        elif re.match(match_test_guess, line):
            gissning = get_guess(line)
            current_trial.guess = get_guess(line)
            gissning = get_guess(line)
            gissning2 = gissning.lower()
            current_trial.guess = get_guess(line)
            

            if gissning2 == svar:
                current_trial.rattad = 1
            elif gissning2 == "vetej":
                current_trial.rattad = 0
            elif gissning2 == "VETEJ":
                current_trial.rattad = 0
            elif gissning2 == "":
                current_trial.rattad = 0
            elif gissning2 == 'vetinte':
                current_trial.rattad = 0
            elif gissning2 == 'dontknow':
                current_trial.rattad = 0
            elif gissning2 != svar:
                print(num+1, svar, gissning2)
                rattning = input()

                if rattning == "y":
                    current_trial.rattad = 1
                else:
                    current_trial.rattad = 0


        elif re.match(match_difficulty, line):
            current_trial.difficulty = get_value(line)
        


#Returns a dictionary 
asdf = [asdict(f) for f in trials]


import pandas as pd
#Converts the dictionary to a dataframe
baba = pd.DataFrame(asdf)

#Prints dataframe to a csv file
baba.to_csv('output.csv')