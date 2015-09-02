#! /usr/local/bin/python3
# mapIt.py - launchs google maps and locate the address from the
# clipboard or from the command line argument

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
    # Get address from the command line
    address = ' '.join(sys.argv[1:])
else:
    #TODO: Get address from the clipboard
    address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
