#!/usr/local/bin/python3
import sys
lst_modifications = []
current_testcase = 0
try:
   testcases_num = int(input("Enter the number of test cases: "))
except ValueError:
   print("The entered value is not an int")
   sys.exit()
   
while current_testcase < testcases_num:
    word = input("Enter word: ")
    if word == "":
        break
    acum_modifications = 0
    word_lst = []
    word_lst2 = []
    if word.lower() != word[::-1].lower():
        half_len = round(len(word)/2)
        for num, c in enumerate(word):
            if num < half_len:
                word_lst.append(ord(c))
            else:
                word_lst2.append(ord(c))
        ascii2 = 0
        for ascii in word_lst2:            
            if ascii == word_lst[ascii2]:
                ascii2 += 1
            else:
                acum_modifications = acum_modifications + (ascii - word_lst[ascii2])
                ascii2 += 1
    lst_modifications.append(acum_modifications)
    current_testcase += 1
       
for val in lst_modifications:
    print("Modifications: {0}".format(val))