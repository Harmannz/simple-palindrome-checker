'''Program to print information on words and palindromes from a file
   Author: Harman Singh
   Version: 9 May 2014 '''

import os

def main():
    ''' Main function: prompt for filename, print various statistics
    about the words in the file'''
    infile = input ("Please enter filename: ")
    while not os.path.isfile(infile):
        print(infile, "not found...")
        infile = input("Please enter filename: ")
    
    words = get_words_from_file(infile)
    
    print(infile, "loaded ok.")
    print("{} valid words found.".format(len(words)))
    print()
    print("First word: {}".format(words[0]))
    print("Last word: {}".format(words[-1]))
    
    print_average_word(words)
    print_max_word(words)
    print_unique_words(words)
    print_palindromes(words)


# ----------------------------------------------
def get_words_from_file(filename):
    ''' gets all the words from the file and returns them as a list'''
    lines = open(filename, 'r', encoding="utf-8").read()
    to_return_list = []
    for word in lines.split():
        word = word.strip('\n"-:\';,.').lower()
        if word.isalpha():
            to_return_list.append(word)
    
    return to_return_list
# ----------------------------------------------



def print_palindromes(words):
    ''' prints all the palindromes greater than 2 characters'''
    set_of_palindromes = set()
    for word in words:
        is_palindrome = word == word[::-1]
        if len(word) > 2 and is_palindrome:
            set_of_palindromes.add((word))
    
    #can group the following code into a new print function
    count = 0
    while count < 3:
        print('')
        count += 1
        
    if len(set_of_palindromes) > 0:
        print('The following palindromes were found:')
        for palindrome in sorted(set_of_palindromes):
            print(' ' + palindrome)
    else:
        print ('No palindromes were found, how boring:(')



def print_average_word(words):
    '''Calculates and prints the average word length in the given set of
        program words taken from the file with the given name.
        '''
    total_length = 0
    for word in words:
        total_length += len(word)
    average = total_length / len(words)
    print("Avg word length = {:.2f}".format(average))



def print_max_word(words):
    '''Calculates and prints the maximum word length in the given set of
        program words taken from the file with the given name.
        '''
    if len(words) > 0:
        max_length = len(words[0])
        for word in words:
            word_length = len(word)
            if word_length > max_length:
                max_length = word_length
                
    print('Max word length =', max_length)
   


def print_unique_words(words):
    '''Calculates and prints the number of unique words in the given set of
        program words taken from the file with the given name.
        '''
    unique_words = set()
    for word in words:
        unique_words.add(word)
    print()
    print("{} unique words found.".format(len(unique_words)))
    
    print_unique_word_length(unique_words)
    

def print_unique_word_length(unique_word):
    '''Calculates and prints the average unique word length in the given 
    set of program words taken from the file with the given name.
        '''
    total_length = 0
    for word in unique_word:
        total_length += len(word)
    average = total_length / len(unique_word)
    print("Avg unique word length = {:.2f}".format(average))


main()