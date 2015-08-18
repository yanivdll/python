#! /usr/local/bin/python3
# mcb.pyw - multiclipboard

# usage:
# python mcb.pyw save <spam> - saves clipbord to keyword
# python mcb.pyw <keyword> - loads keyword to clipboard
# python mcb.pyw list - loads all keywords to clipboard

import shelve, sys, pyperclip

mcbShelf = shelve.open('mcb')

# save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    
mcbShelf.close()
