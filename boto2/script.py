#! /usr/bin/python3
from boto.s3.connection import S3Connection
import boto
from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d %H:%M:%S")
    d2 = datetime.strptime(d2, "%Y-%m-%d %H:%M:%S")
    return abs((d2 - d1).days)

def dateFormatter(unoformattedDate):
    year = unoformattedDate[:5]
    month = unoformattedDate[5:8]
    day = unoformattedDate[8:10]
    hour = unoformattedDate[12:19]
    date = year+month+day+" "+hour
    return date

location = "s3.eu-west-1.amazonaws.com"
bucketName = 'kds-uav-dev'
minimumDays = 7
aws_connection = S3Connection( host = location )
bucket = aws_connection.get_bucket( bucketName , validate=False)
uavs = bucket.list()
uavsOfIntrest = []
totalUavs = 0

for uav in uavs:
    lastModified = uav.__getattribute__('last_modified')
    date = dateFormatter(lastModified)
    currentDate = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    diff = days_between(date, currentDate)
    #print(lastModified)

    if diff <= minimumDays:
        uavsOfIntrest.append(uav)
        totalUavs += 1
        #print( date , " date modified - today's date = " , diff )

print(uavsOfIntrest)
print(totalUavs)


# DATE=$(date --date="7 days ago" "+%Y-%m-%d") && time aws s3api list-objects --bucket kds-uav-dev --query "Contents[?LastModified>='$DATE'].{Key: Key , LastModified: LastModified}"
# DATE=$(date '+%Y-%m-%d %H:%M:%S' --date="7 days ago") && time aws s3api list-objects --bucket kds-uav-dev --query "Contents[?LastModified>='$DATE'].{Key: Key , LastModified: LastModified}"
# date '+%Y-%m-%d %H:%M:%S' --date="7 days ago"