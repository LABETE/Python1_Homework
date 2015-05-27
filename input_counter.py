#!/usr/local/bin/python3
"""Count input order of the words"""

wordsdict = {}
wordsset = set()
lenset = 0
while True:
    wordslst = input("Enter text(Press Enter key for finish): ").split()
    if not wordslst:
        print("Finished")
        break
    for word in wordslst:
        wordsset.add(word.lower())
        if len(wordsset) > lenset:
            lenset += 1
            wordsdict[word] = lenset
    for value in wordsdict.keys():
        print(value, ":", wordsdict[value])
        