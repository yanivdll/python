import boto
from boto.s3.connection import S3Connection
import os
import sys
import urllib
from datetime import date, datetime
import subprocess

# This is how Hazel passes in the file path
hazelFilePath = sys.argv[1]


# Obviously, you'll need your own keys
aws_key = sys.argv[2]
aws_secret = sys.argv[3]

# This is where I store my log file for these links. It's a Dropbox file in my NVAlt notes folder
logFilePath = "/Users/ygilad/Dropbox/Notes/Linkin_Logs.txt"
nowTime = str(datetime.now())

# Method to add to clipboard
def setClipboardData(data):
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.stdin.write(data)
    p.stdin.close()
    retcode = p.wait()

# This is the method that does all of the uploading and writing to the log file.
# The method is generic enough to work with any S3 bucket that is passed.
def uploadToS3(localFilePath, S3Bucket):
    fileName = os.path.basename(localFilePath)

    # Determine the current month and year to create the upload path
    today = date.today()
    datePath = today.strftime("/%Y/%m/")

    # Create the URL for the image
    imageLink = 'http://'+urllib.quote(S3Bucket+datePath+fileName)

    # Connect to S3
    s3 = S3Connection(aws_key, aws_secret)
    bucket = s3.get_bucket(S3Bucket)
    key = bucket.new_key(datePath+'/'+fileName)
    key.set_contents_from_filename(localFilePath)
    key.set_acl('public-read')
    logfile = open(logFilePath, "a")

    try:
        # %% encode the file name and append the URL to the log file
        logfile.write(nowTime+'  '+imageLink+'\n')
        setClipboardData(imageLink)
    finally:
        logfile.close()

# How's this for terrible design. The actual body of the script is one line. I'm my own worst enemy.
uploadToS3(hazelFilePath, 'media.prodissues.com')
