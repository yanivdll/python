# Source: https://gist.github.com/najibninaba/5062153
# 
# This script upload files (at the moment images and slideshows) to S3. 
#
# Credits:
# This script is inspired by macdrifter script, which can be found at  http://www.macdrifter.com/2012/05/upload-to-amazon-s3-from-dropbox-using-hazel.html
#

import boto
from boto.s3.connection import S3Connection
import pyperclip
import os
import sys
from datetime import date, datetime

# This is how Hazel passes in the file path
hazelFilePath = sys.argv[1]
contentType = sys.argv[2]

# This is where I store my log file for these links. It's a Dropbox file in my NVAlt notes folder
logFilePath = "~/Dropbox/Notes/Linkin_Logs.txt"
nowTime = str(datetime.now())


# This is the method that does all of the uploading and writing to the log file.
# The method is generic enough to work with any S3 bucket that is passed.
def uploadToS3(localFilePath, localFileType, S3Bucket):
    fileName = os.path.basename(localFilePath)

    # Determine the current month and year to create the upload path
    today = date.today()
    datePath = today.strftime("/%Y/%m/")

    # Connect to S3
    s3 = boto.connect_s3()
    bucket = s3.get_bucket(S3Bucket)
    
    # Set the folder name based on the content type image\slideshow
    if localFileType == 'slideshow':
        key = bucket.new_key('slideshows/' + fileName)
    else:
        key = bucket.new_key('images' + datePath + fileName)

    # Upload file to S3
    key.set_contents_from_filename(localFilePath)
    key.set_acl('public-read')

    # Log the url of the hosted file
    logfile = open(logFilePath, "a")
    
    # Create the URL for the image
    imageLink = 'http://' + S3Bucket + '/' + key.name

    try:
        # %% encode the file name and append the URL to the log file
        logfile.write(nowTime+'  '+imageLink+'\n')
        pyperclip.copy(imageLink)
    finally:
        logfile.close()

# The body of the script.
uploadToS3(hazelFilePath, contentType,'media.prodissues.com')
