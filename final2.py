#!/usr/local/bin/python3
""" Program for extract information of a document txt"""

import sys

exit_options_lst = ["Yes","No"]
menu_lst = ["Size of the word and number of words(1: 20)","Word and number of times that it is displayed(and: 15)","Words that are from the same size(3: and, the)","Exit from menu selection"]
tables_titles = ["Length","Count","Word(s)"]
count_words_dict = {}
words_dict = {}
words_by_char_num = {}
histogram_bars = ""
if __name__ =="__main__": 
    read_console = sys.argv
    len_read_console = len(read_console)
    read_console.reverse()
    read_console.pop()
    while True:
        if len_read_console == 1 or len(read_console) == 0:
            #Read the input of the user(it should be the name of a document and direction if is needed)
            doc_name = input("Enter the name of your document, add the path if is not in the same folder than the program: ")      
        else:
            doc_name = read_console.pop()
        #If user put the \ instead of / in the path it is changed
        if doc_name.find("\\"):
            doc_name = doc_name.replace("\\","/")
        #if the document name is not wrote by the user with the extension it is added
        if not doc_name.endswith(".txt"):
            doc_name = doc_name + ".txt"
        #If the document exist it will do the following code    
        try:
            #Document open in read mode
            obj_text = open(doc_name,"r")
            #The text is splitted in a list
            words_lst = obj_text.read().split()
            obj_text.close()
            #The list is traversed word per word
            for word in words_lst:
                special_char = 0
                word_sanitized = word
                #each character per word is verified
                for char in word:
                    #if the character is not in the range of numbers or upper alphabet special_char is increased by 1 and the
                    #character in the list is replaced by ""
                    if not 65 <= ord(char.upper()) <= 91 or 30 <= ord(char) <= 39:
                        special_char += 1
                        word_sanitized = word_sanitized.replace(char,"")
                #Get the length of each word
                len_word = len(word) - special_char
                #If the word contain 0 characters it could be that a "word" was composed by special characters is not used
                if len_word > 0:         
                    #if the word exist in the dictionary the current value is increased by 1 else the key word is created with 1 as value
                    words_dict[word_sanitized.lower()] = words_dict.get(word_sanitized.lower(), 0) + 1
                    #If the length exist in the dictionary the current value is increased by 1 else the key word is created with 1 as value
                    count_words_dict[len_word] = count_words_dict.get(len_word, 0) + 1  
                    #If the keyword not exist in the dictionary a set is assigned to that keyword
                    if words_by_char_num.get(len_word, "") == "":
                        words_by_char_num[len_word] = {word_sanitized.lower()}
                    else:    
                        #if the keyword exist in the dictionary the new word is added to the set
                        words_by_char_num[len_word].add(word_sanitized.lower()) 
            while True:                         
                #A menu is printed
                user_selection = input("What do you want to do?\n1.-{0}\n2.-{1}\n3.-{2}\n4.-{3}\n".format(menu_lst[0],menu_lst[1],menu_lst[2],menu_lst[3]))
                #A table with the size of the words and how many times in the text were displayed with the same size
                if user_selection == "1":
                    print("-"*20)
                    print("|{0:^8}|{1:^9}|".format(tables_titles[0],tables_titles[1]))     
                    print("-"*20)   
                    for length_words, counted_words in count_words_dict.items():
                        print("|{0:^8}|{1:^9}|".format(length_words, counted_words))
                    print("-"*20)
                    while True:
                        histogram_option = input("Do you want to print the Histogram? Yes/No: ")
                        if histogram_option.lower() == "yes":
                            #Get the max value in the values from the data dictionary
                            max_value_data_y = max(count_words_dict.values())
                            #Get the max value in the keys from the data dictionary
                            max_value_x = max(count_words_dict.keys()) + 1
                            #Get the max value that will be displayed as max in Y
                            max_value_y = (int(max_value_data_y / 100) + 1) * 100
                            #Iterate in reverse from the max value to -21(It allow to put 0 and the line with numbers)
                            for value_y in range(max_value_y,-21,-20):
                                histogram_bars = ""
                                verify_existing_length = 1
                                #Iterate over the dictionary for get the values for each bar per level(max_value_y is the first level)
                                #It save *** or 3 white spaces in the histogram_bars variable per bar
                                for length_words, counted_words in count_words_dict.items():
                                    while verify_existing_length != length_words:
                                        verify_existing_length += 1
                                        histogram_bars += "   ".rjust(4)
                                    else:
                                        if counted_words >= value_y and value_y != -20:
                                            histogram_bars += "***".rjust(4)
                                        elif value_y  == -20: 
                                            #In this specific case the histogram_bars save each number of the last line in X instead of *** and 3 white spaces
                                            histogram_bars = " " + "  ".join(str(num).rjust(2).ljust(1) for num in range(1,max_value_x + 1))
                                        else:
                                            histogram_bars += "   ".rjust(4)  
                                    verify_existing_length += 1 
                                #get the spaces necesaries for the Y side(vertical side of the histogram)
                                left_pad = 2 + len(str(max_value_y)) + (len(str(max_value_y)) - len(str(value_y)))
                                #Put the values and spaces in the vertcal side of the histogram
                                if value_y%100 != 0:
                                    left_pad += len(str(value_y))
                                    value_y = "|".rjust(left_pad)
                                elif value_y == 0:
                                    #This part is for put the --+- in the first line X when is 0
                                    histogram_bars = "--+-"*max_value_x
                                    #This part is for put -* instead of -| when is 0
                                    value_y = str(value_y).rjust(left_pad - 2) + " -+"
                                else:
                                    value_y = str(value_y).rjust(left_pad) + " -|"
                                print("{0}".format(value_y)+"{0}".format(histogram_bars))   
                            break            
                        elif histogram_option.lower() == "no":
                            break
                        else:
                            print("The entered answer don't exist, please enter a correct answer")
                    
                #Display a table with each word and how many times it was displayed in the text    
                elif user_selection == "2": 
                    print("-"*37)
                    print("|{0:^25}|{1:^9}|".format(tables_titles[2],tables_titles[1]))     
                    print("-"*37) 
                    for word, counted_words in words_dict.items():
                        print("|{0:^25}|{1:^9}|".format(word, counted_words))
                    print("-"*37)
                #Display a table with the size of the word and the diferent words displayed in the text without be repeated    
                elif user_selection == "3":
                    print("-"*61)
                    print("|{0:^8}|{1:^50}|".format(tables_titles[2],tables_titles[1]))     
                    print("-"*61) 
                    for length_words, words in words_by_char_num.items():
                        words_lst = list(words)
                        words_join = ", ".join(words_lst)
                        #Get the position in the string where it will be splitted
                        delimited_line = int((50/(length_words + 2)) * length_words)
                        #Will print the table with the current word's lenght and words that are between 50 positions in the string
                        while len(words_join) > 50 and words_join != "":
                            print("|{0:^8}|{1:^50}|".format(length_words, words_join[:delimited_line]))
                            words_join = words_join[delimited_line:]
                        else:
                            print("|{0:^8}|{1:^50}|".format(length_words, words_join))
                    print("-"*61)
                
                elif user_selection == "4":
                    break
                else:
                    print("You entered an invalid option, please enter a value between 1 and 4")
        #If the path provided is wrong the following message will be displayed
        except Exception:
            print("something went wrong with the path, verify that your path is correct")
        #Ask if the user want to enter another text or if the user want to finish the program
        while True:    
            if len_read_console > 1:
                print("You have {0} more documents for verify, you can continue or finish the program".format(len(read_console)))
            cont_exit = input("Do you want to finish the program? {0}: ".format("/".join(exit_options_lst))) 
            if cont_exit.lower() != "yes" and cont_exit.lower() != "no":
                print("The entered answer don't exist, please enter a correct answer")
            else:
                break
        if cont_exit.lower() == "yes":
            break