#!/usr/local/bin/python3
"""Program save inputs and display the saved text when is the program start"""

file_saved = open('saving_inputs.txt', 'a')
file_saved.close()
file_saved = open('saving_inputs.txt', 'r')
print(file_saved.read())
while True:
    text_input = input("Enter text: ")
    if not text_input:
        break
    file_saved = open('saving_inputs.txt', 'a')
    file_saved.write(text_input)
    file_saved.close()
    file_saved = open('saving_inputs.txt', 'r')
    print(file_saved.read())
    file_saved.close()
