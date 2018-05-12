#Name: Sanjay Kumar Ajith Kumar
#Student ID: 29449677
#Start Date: 30th April, 2018
#Last Modified: 3rd May, 2018

#colors
FAIL = '\033[91m'
ENDC = '\033[0m'

#Decoder class
class Decoder:
    
    #Decoder constructor which initializes a dictionary of morse codes and its values. 
    def __init__(self):
        self.mc_dict = {'01': 'A','1000': 'B','1010': 'C','100': 'D','0': 'E','0010': 'F','110': 'G','0000': 'H','00': 'I','0111': 'J','101': 'K','0100': 'L','11': 'M','10': 'N','111': 'O','0110': 'P','1101': 'Q','010': 'R','000': 'S','1': 'T','001': 'U','0001': 'V','011': 'W','1001': 'X','1011': 'Y','1100': 'Z','11111': '0','01111': '1','00111': '2','00011': '3','00001': '4','00000': '5','10000': '6','11000': '7','11100': '8','11110': '9','010101': '.','110011': ',','001100': '?'}
    
    #Overwrite str method to print the Morse Code dictionary
    def __str__(self):
        str_output = "--- Morse Code Dictionary ---\n"
        for k, v in self.mc_dict.items():
            str_output += k + ": " + v + "\n"
        return str_output
    
    #Define the decode functionality with sequence holding the final decoded string
    def decode(self, morse_code_sequence):
        character_list = morse_code_sequence.split('*')
        sequence = ""
        #As per the assignment, sequences must end with either ?.,
        if character_list[-1] not in ['010101', '110011', '001100']:
            print("While decoding " + morse_code_sequence + FAIL + "\n\tDecode Error: All sequences must end in either ,.?" + ENDC)
            return sequence
        #word_spacing: used to handle *** or space scenario
        word_spacing = False
        for item in character_list:
            #if present, then print the character corresponding to it, add the character to sequence and
            #append the count of that character in alpha_num_dict
            if item in self.mc_dict.keys():
                sequence += self.mc_dict[item]
                word_spacing = False
            
            #A blank space will be rendered as 2 consecutive empty strings ''. Using word_spacing to check for spaces
            elif (item == '' and word_spacing == False):
                word_spacing = True
            elif(item == '' and word_spacing == True):
                print(end='')
                sequence += ' '
                word_spacing = False
            
            #if the character is not there in dictionary, print invalid character error and break decoding
            else:
                sequence = ''
                print("While decoding " + morse_code_sequence + FAIL + "\n\tDecode Error: Encountered an Invalid Character" + ENDC)
                return sequence
        return sequence