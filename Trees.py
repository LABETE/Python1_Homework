#!/usr/local/bin/python3
"""Program sort Upper case and after lower case words"""

text = input("Input your text: ")
words = text.split()
upperlst = []
lowerlst = []
for word in words:
#    for c in word:
#        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#            upperlst.append(word)
#            break
    if not word.isupper() and not word.islower() and word.isalpha() or word.isupper():
        upperlst.append(word)
#    if not word in upperlst:
    else:
        lowerlst.append(word)

#finallst= upperlst + lowerlst
for iteration, value in enumerate(upperlst + lowerlst):
    print(value)