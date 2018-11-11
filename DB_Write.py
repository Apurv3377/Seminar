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
from datetime import timezone, datetime

from mongoengine import *
connect('mongoengine_test', host='localhost', port=27017)

#from pymongo import MongoClient

#client = MongoClient('localhost', 27017) #making connection to MongoClient


class FirstTC(Document):
    syscall_nr = IntField(min_value=None, max_value=None)
    syscall_name = StringField(required=True)
    dtb = StringField(required=True, max_length=50)
    rsp = StringField(required=True, max_length=20)
    rip = StringField(required=True, max_length=20)
    pid = IntField(min_value=None, max_value=None)
    ts = IntField(min_value=None, max_value=None)
    vmid = StringField(required=True, max_length=20)
    logtype = StringField(required=True, max_length=20)


        #return Math.round(new Date().getTime()); /* timestamp in milliseconds */


#print ("hello")

def random_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_hexgenerator():
    hexN="0x"+uuid.uuid4().hex
    return hexN[:18]

def timestamp_gen():
    ts=int(datetime.now(tz=timezone.utc).timestamp() * 1000)
    return ts


i=0
orig_stdout = sys.stdout
f = open('/media/sf_DB_Readings/Readings.csv', 'w')
sys.stdout=f
comm=","


while i<10000:

    i=i+1
    start = time.time()
    post_1 = FirstTC(
   syscall_nr=random.randint(1,101),
   syscall_name=random_generator(6,"abcdefghijklmnopqrstuvwxyz"),
   dtb=random_hexgenerator(),
   rsp=random_hexgenerator(),
   rip=random_hexgenerator(),
   pid=random.randint(1,10000),
   ts= timestamp_gen(),
   vmid="vm"+random_generator(2,'1234'),
   logtype=random_generator(3,'xyz')
   )
    post_1.save()  # This will perform an insert
    end=time.time()
    executionTime = (end - start) * 1000 # Convert to ms
    print (i,comm,executionTime)

sys.stdout = orig_stdout
    #f.write(",%f\n" % executionTime)
f.close()



print("saved")


#os.system('mongoexport --db mongoengine_test --collection post --pretty --out output.json > /dev/null 2>&1')
