#! /usr/local/bin/python3
# removeRepeatWords.py - find and remove repeat words

import pyperclip, re

text = str(pyperclip.paste())

#regex definitions for reapeated spaces
repeatSpacesRegex = re.compile(r'\b(\s)+\1+\b', 'm') 

#regex definitions for reapeated words
repeatWordsRegex = re.compile(r'\b((\w+)\s+)\1\b', re.IGNORECASE|re.DOTALL)

#remove the extra spaces
repeatSpces = repeatSpacesRegex.findall(text)

if len(repeatSpces) > 1:
    text = repeatSpacesRegex.sub(r'\1', text)
    print(str(len(repeatSpces)) + ' repeat spaces were removed.')

#remove repeated words
repeatWords = repeatWordsRegex.findall(text)

if len(repeatWords) > 0:
    print('List of repeated words:' + str(repeatWords))
    text = repeatWordsRegex.sub(r'\1', text)
    print('Repaired text is waiting in clipboard.')
else:
    print('Nice work. No repeat words were find.')

pyperclip.copy(text)
