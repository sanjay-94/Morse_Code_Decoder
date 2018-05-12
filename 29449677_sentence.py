#Name: Sanjay Kumar Ajith Kumar
#Student ID: 29449677
#Start Date: 30th April, 2018
#Last Modified: 3rd May, 2018

import re

#Sentence Analyser class
class SentenceAnalyser:
    #constructor which initializes a dictionary with the 3 types of sentences. 
    def __init__(self):
        self.sentence_types = {'clause': 0, 'complete': 0, 'question': 0}
    
    #Overwrite the str method to print the sentence type dictionary
    def __str__(self):
        output_str = ""
        for k, v in self.sentence_types.items():
            output_str += "The occurrence of {} sentence is {} time(s) \n".format(k, v)
        return output_str
    
    #Define the analyse_sentences function to find the sentence types in decoded sequence
    def analyse_sentences(self, decoded_sequence):
        #find clauses based on commas
        sentence_splits = decoded_sequence.split(',')
        for each_split in sentence_splits:
            if each_split != '':
                #if sequence ends in comma, increment clause 
                if each_split[-1] not in ['?', '.']:
                    if re.match("^[A-Za-z0-9\s]+$", each_split):
                        self.sentence_types['clause'] += 1
                #if sequence ends in question mark, increment question
                elif each_split[-1] == '?':
                    self.sentence_types['question'] += 1
                #if sequence ends in period, increment complete 
                elif each_split[-1] == '.':
                    self.sentence_types['complete'] += 1

    #function to reset the dictionary for each sequence to be decoded
    def reset_dict(self):
        self.sentence_types = {'clause': 0, 'complete': 0, 'question': 0}


