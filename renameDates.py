#! /usr/local/bin/python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format to Europene DD-MM-YYY format

import shutil, os, re

workingDir = '/Users/ygilad/Downloads/'

# Create regex that matchs files with American date format
datePattern = re.compile(r"""^(.*?) # all text before the date
	((0|1)?\d)-                     # one or two digits for the month
  ((0|1|2|3)?\d)-                 # one or two digits for the day
  ((19|20)\d\d)                   # four digits for the year
  (.*?)$                          # all text after the date
	""", re.VERBOSE)

#loop over the files in the working directory
for amerFilename in os.listdir(workingDir):
	mo = datePattern.search(amerFilename)

	# skip files without a date
	if mo == None:
		continue

	# get the different parts of the filename
	befoerPart = mo.group(1)
	monthPart = mo.group(2)
	dayPart = mo.group(4)
	yearPart = mo.group(6)
	afterPart = mo.group(8)

# form the europene format of the filename
	euroFilename = befoerPart + dayPart + '-' + monthPart + '-' + yearPart + afterPart

# get the full, absolut file path
	absWorkingDir = os.path.abspath(workingDir)
	amerFilename = os.path.join(absWorkingDir, amerFilename)
	euroFilename = os.path.join(absWorkingDir, euroFilename)

# rename the files
	print('Renaming %s to %s ...' % (amerFilename, euroFilename))

	shutil.move(amerFilename, euroFilename) #uncomment after test



