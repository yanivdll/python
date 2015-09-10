#! /usr/local/bin/python3
# removeRepeatWords.py - find and remove repeat words
import logging
logging.basicConfig(filename='/Users/ygilad/Library/Logs/Python/myPythonLogs.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

logging.disable(logging.CRITICAL)

import pyperclip, re

text = str(pyperclip.paste())

#regex definitions for reapeated spaces
repeatSpacesRegex = re.compile(r'\b(\s)+\1+\b') 

#regex definitions for reapeated words
repeatWordsRegex = re.compile(r'\b(\w+)\b[\s\r\n]*(\1[\s\r\n])+', re.IGNORECASE|re.DOTALL)

#remove the extra spaces
repeatSpces = repeatSpacesRegex.findall(text)

if len(repeatSpces) > 1:
    text = repeatSpacesRegex.sub(r'\1', text)
    print(str(len(repeatSpces)) + ' repeat spaces were removed.')

#remove repeated words
repeatWords = repeatWordsRegex.findall(text)
logging.debug(repeatWords)

if len(repeatWords) > 0:
    text = repeatWordsRegex.sub(r'{~~\1 \2~>\1 ~~}{>>repeating words<<}', text)

pyperclip.copy(text)
