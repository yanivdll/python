#! /usr/local/bin/python3
# findLargeFiles.py - walk through an entire tree and find files that are larger than 100mb

import os
import logging
logging.basicConfig(filename='/Users/ygilad/Library/Logs/Python/myPythonLogs.log', level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')

pwd = os.chdir('/Users/ygilad/temp')
outputFile = open('recursive_walk.txt','w')

def recursive_walk(folder):
	numOfFiles = 0
	for folderName, subfolders, filenames in os.walk(folder):
		if subfolders:
			for subfolder in subfolders:
				recursive_walk(subfolder)
		for filename in filenames:
			numOfFiles += 1
			try:
				if os.path.getsize(folderName + '/' + filename) > 100000000: 
					outputFile.write(folderName + '/' + filename + ': ' + str(os.path.getsize(folderName + '/' + filename)) + '\n')
			except OSError:
				logging.debug('Problem getting size for the file ' + filename)
	print('Done. %s files were processed.' %(numOfFiles))

recursive_walk('/Users/')
	