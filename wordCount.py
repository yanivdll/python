#! /usr/local/bin/python3

# wordCount.py - create an index of use words and number of uses

import sys, pyperclip, re

text = pyperclip.paste()
text = text.lower() #this will make sure we count each word only once
wordDict = {}

for i in text.split():
    if i.isalpha():
        if i in wordDict.keys():
            wordDict[i] += 1
        else:
            wordDict.setdefault(i, 1)

print(('Unique words: ' + str(len((wordDict)))).center(50,'*') )
for w in sorted(wordDict, key=wordDict.get, reverse=True):
    if wordDict[w] > 1:
        print ((wordDict[w] * '-') + '> ' + str(wordDict[w]) + ' ' + w)
