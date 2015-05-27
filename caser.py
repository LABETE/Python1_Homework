#!/usr/local/bin/python3
""" Program for give format to strings"""

import sys

def capitalize_text(text):
    """ Function return a string capitalized. """
    return text.capitalize()

def title_text(text):
    """ Function return a string formated as title. """
    return text.title()

def upper_text(text):
    """ Function return a string formated as upper case. """
    return text.upper()
    
def lower_text(text):
    """ Function return a string formated as lower case. """
    return text.lower()    
    
def exit_program(text=False):
    """ Function for exit from the program """
    print("Goodbye for now!")
    sys.exit()

def dispatch_table(**options):
    """ Function return all selectable options with his functions as a dict """
    return options
        
if __name__ == "__main__":      
    #get all options with functions
    format_options = dispatch_table(capitalize=capitalize_text, title=title_text, upper=upper_text, lower=lower_text, exit=exit_program)  
    while True:
        str_inp = ''
        #get the options as a list
        lst_keys = list(format_options.keys())
        #get an string from the user
        opt = input('Enter an option {0} or {1}: '.format(', '.join(lst_keys[:-1]),' '.join(lst_keys[-1:]))).lower()
        if opt:
            if opt != 'exit':
                #if selected option is not exit the program display a request waiting for an input
                str_inp = input('Enter a string: ')
            #Get the function using the opt as a key  
            opt = format_options.get(opt, None)
            print(opt(str_inp))
        else:
            print("Invalid option, enter a valid value")