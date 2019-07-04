#! /usr/bin/python3
import Bucket
import Collection

bucket = Bucket.Bucket('testbucketboto11')
uavs = Collection.Collection().addUav(bucket.getUavs())
print (uavs)

