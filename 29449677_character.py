#Name: Sanjay Kumar Ajith Kumar
#Student ID: 29449677
#Start Date: 30th April, 2018
#Last Modified: 3rd May, 2018

import re

#Character Analyser class
class CharacterAnalyser:
    #In constructor, initialize an empty dictionary to hold characters in a sequence
    def __init__(self):
        self.character_dict = {}
    
    #Overwrite str method to print the character dictionary
    def __str__(self):
        output_str = ""
        for k, v in self.character_dict.items():
            output_str += "The occurrence of {} is {} time(s) \n".format(k, v)
        return output_str
    
    #Define the analyse_characters function to find the characters in a decoded sequence
    def analyse_characters(self, decoded_sequence):
        #change characters to upper case for uniqueness
        character_list = [char.upper() for char in decoded_sequence]
        for char in character_list:
            #store only A-Z and 0-9 characters in dictionary as per assignment requirement. 
            if re.match("[A-Z0-9]", char):
                #create new entry or increment an existing entry in character dictionary
                if char in self.character_dict:
                    self.character_dict[char] += 1
                else:
                    self.character_dict[char] = 1
    
    #function to reset the dictionary for each sequence to be decoded
    def reset_dict(self):
        self.character_dict = {}
