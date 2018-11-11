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

documents_number = collection.count() * 200000

def random_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))

i=0
j=0
itr=0
MAX_ITR=int(sys.argv[1])
f = open('/media/sf_DB_Readings/Readings.csv', 'w')


startf = datetime.now();
while itr<MAX_ITR: 
    start = datetime.now();
    for index in range(documents_number):
        try:
            vmid="vm"+random_generator(2,'1234')
            #calculate the time for the insert
            timec=int((datetime.now() - start).total_seconds())
            for vm in collection.find("vmid": vmid):
                continue

            if timec==1:
                #print (timec, 'secs for',index)
                j=j+1
                f.write("%d,%d\n" %(j, index))
                itr=itr+1
                break
                   
        except:
            print ('Unexpected error:', sys.exc_info()[0], ', for index ', index)
            raise

f.close()
  
   
