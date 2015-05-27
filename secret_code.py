#!/usr/local/bin/python3
"""Program create a secret code."""

options = ('Enter Code', 'Extract code from txt')
secret_code = ""; selected_option = ""; ordinary_code = ""
while True:
    selected_option = input("What you want to do? {0[0]} or {0[1]}: ".format(options))
    if not selected_option:
        break
    #Receive an input in the program
    if selected_option.lower() == "enter code":
        ordinary_code = input("Enter your code: ")   
    #Reveive the input from a document
    if selected_option.lower() == "extract code from txt":
        document_name = input("Enter the document name without extension: ")
        print(document_name + ".txt")
        doc = open(document_name + ".txt", 'a+')
        doc.seek(0)
        ordinary_code = doc.read()
        doc.close()
        print(ordinary_code) 
    for character in reversed(ordinary_code):
        secret_code += chr(ord(character) + 1)
    print("The secret code is: {0}".format(secret_code))    
    secret_code = ""