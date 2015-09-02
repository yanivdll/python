#! /usr/local/bin/python3
# migrateMiddlemanToPelican.py - move posts from middleman post directory to pelican's
# change the extension of the files from *.html.markdown to *.md

import os, shutil

# get a list of files in the post directory of middleman

srcFolder = '/Users/ygilad/dev/blog_bck/prodissues_heroku/source/posts/'
destFolder = '/Users/ygilad/dev/prodissues/content/'
srcFiles = list(os.listdir(srcFolder))


for i in srcFiles:
    if i.endswith('markdown'):
        oldFileName = (os.path.basename(i).split('.')[0])
        newFileName = oldFileName + '.md'

        # copy the file to the new folder
        shutil.copy(srcFolder + i, destFolder + newFileName)
        print(newFileName)
    
