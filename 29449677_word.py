#Name: Sanjay Kumar Ajith Kumar
#Student ID: 29449677
#Start Date: 30th April, 2018
#Last Modified: 3rd May, 2018

import re

#Word Analyser class
class WordAnalyser:
    #constructor which initializes an empty word dictionary
    def __init__(self):
        self.word_dict = {}
    
    #overwrite str method to print the word dictionary
    def __str__(self):
        output_str = ""
        for k, v in self.word_dict.items():
            output_str += "The occurrence of {} is {} time(s) \n".format(k, v)
        return output_str
    
    #define analyse_words to find the occurrences of each word in a sentence. 
    def analyse_words(self, decoded_sequence):
        word_list = decoded_sequence.split()
        for word in word_list:
            #from word strip the last character, if its .,? before storing it into word dictionary
            if word[-1] in ['.', ',', '?']:
                word = word[:-1]
            if (re.match("^[A-Za-z]*$", word) or re.match("^[0-9]*$", word)) and len(word) >= 1:
                if word in self.word_dict:
                    self.word_dict[word] += 1
                else:
                    self.word_dict[word] = 1

    #function to reset the dictionary for each sequence to be decoded
    def reset_dict(self):
        self.word_dict = {}