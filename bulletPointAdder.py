#! /usr/local/bin/python3

# bulletPointAdder.py - adds wikipedia bullet points to
# the start of every line passed through the clipboard

import sys, pyperclip, pprint

text = pyperclip.paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '- ' + lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)