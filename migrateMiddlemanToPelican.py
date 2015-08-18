#! /usr/local/bin/python3
# migrateMiddlemanToPelican.py - move posts from middleman post directory to pelican's
# change the extension of the files from *.html.markdown to *.md

import os

#get a list of files in the post directory of middleman

srcFolder = '/Users/ygilad/dev/prodissues/source/posts/'
destFolder = '/Users/ygilad/dev/python/prodissues/content/'

srcFiles = list(os.listdir(srcFolder))

for i in srcFiles:
    oldFileName = (os.path.basename(i).split('.')[0])
    newFileName = oldFileName + '.md'

    #TODO: copy the file to the new folder
    print(newFileName)
    
