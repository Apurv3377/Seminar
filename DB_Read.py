#!/usr/bin/python
import json
import pymongo
import datetime
import string
import random
import os
import uuid
import time
import sys
import pprint
from datetime import timezone, datetime

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db=client.mongoengine_test
collection=db.post

def random_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))

i=0
f = open('/media/sf_DB_Readings/Readings.csv', 'w')


while i<100:
    vmid="vm"+random_generator(2,'1234')
    start = time.time()
    for vm in collection.find({"vmid": vmid}):
        pprint.pprint(vm)
    end = time.time()
    executionTime = (end - start) * 1000
    f.write("%d,%f\n" %(i, executionTime))
    i=i+1

    #i=i+1
    #start = time.time()
f.close()   
  
   
