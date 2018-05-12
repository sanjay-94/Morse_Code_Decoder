#Name: Sanjay Kumar Ajith Kumar
#Student ID: 29449677
#Start Date: 30th April, 2018
#Last Modified: 3rd May, 2018

#using a different import because file names start with numbers
_de = __import__('29449677_decoder')
_ca = __import__('29449677_character')
_wa = __import__('29449677_word')
_sa = __import__('29449677_sentence')
import re

#colors
FAIL = '\033[91m'
BOLD = '\033[1m'
ENDC = '\033[0m'

#decoder function returns a list of decoded strings
def decode(de, input_list):
    #define a local list to hold all the decoded sequences
    decoded_list = []
    for inp in input_list:
        if de.decode(inp) != "":
            decoded_list.append(de.decode(inp))
    return decoded_list

def character_analyser(ca, decoded_list):
    print(BOLD + "--- Character Analyser ---" + ENDC)
    for string in decoded_list:
        print("For ", string)
        ca.analyse_characters(string)
        print(str(ca))
        ca.reset_dict()

def word_analyser(wa, decoded_list):
    print(BOLD + "--- Word Analyser ---" + ENDC)
    for string in decoded_list:
        print("For ", string)
        wa.analyse_words(string)
        print(str(wa))
        wa.reset_dict()

def sentence_analyser(sa, decoded_list):
    print(BOLD + "--- Sentence Analyser ---" + ENDC)
    for string in decoded_list:
        print("For ", string)
        sa.analyse_sentences(string)
        print(str(sa))
        sa.reset_dict()

#Main function
def main():
    #initializing all the 4 classes
    de = _de.Decoder()
    ca = _ca.CharacterAnalyser()
    wa = _wa.WordAnalyser()
    sa = _sa.SentenceAnalyser()

    #input_list holds the list of sequences entered by the user
    input_list = []
    input_count = 0
    while True:
        #each sequence is stored in input_str
        input_str = input("Enter the Morse Code (Press <E> to end input): ")
        #check for the escape character and break accordingly
        if(input_str == 'e' or input_str == 'E'):
            print(BOLD + "--- You entered " + str(input_count) + " morse codes ---" + ENDC)
            for item in input_list:
                print(str(input_list.index(item) + 1) + ": " + item)
            break
        #check for invalid characters
        elif not re.match("^[01*]*$", input_str):
            print(FAIL + "Invalid characters found. Allowed characters are 0, 1, *. " + ENDC)
            continue
        #check for minimum number of characters in the input
        elif len(input_str) < 1:
            print(FAIL + "Minimum of 1 character is required in the input." + ENDC)
            continue
        else:
            #if everything is alright, append the input_string to the input_list
            input_list.append(input_str)
            input_count += 1

    #call the decode function to decode all the input strings
    decoded_list = decode(de, input_list)
    decoded_count = len(decoded_list)
    
    if decoded_count > 0:
        #print all the decoded strings
        print(BOLD + "--- Decoded " + str(decoded_count) + " Sequences ---" + ENDC)
        for string in decoded_list:
            print(str(decoded_list.index(string) + 1) + ": " + string)

        #show user menu options and allow user to select appropriate analysis
        while True:
            print(BOLD + "--- Select an operation ---" + ENDC)
            print("1. Analyse Characters\n2. Analyse words\n3. Analyse Sentences\n4. Quit")
            user_inp = int(input("Enter your choice: "))
            if user_inp == 1:
                character_analyser(ca, decoded_list)
            elif user_inp == 2:
                word_analyser(wa, decoded_list)
            elif user_inp == 3:
                sentence_analyser(sa, decoded_list)
            elif user_inp == 4:
                break
            else:
                print(FAIL + "Error: Enter a valid option" + ENDC)

if __name__ == "__main__":
    main()