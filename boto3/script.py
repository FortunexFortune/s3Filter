#! /usr/bin/python3
import Bucket
import Collection

bucket = Bucket.Bucket('kds-uav-dev')
uavs = Collection.Collection().addUav(bucket.getUavs())
print (uavs)

