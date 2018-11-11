#!/usr/bin/python
import sys
import os
import pymongo
import time
import random
import json
import datetime
import string
import uuid
import subprocess
import multiprocessing

 
cpu_count = multiprocessing.cpu_count()
 
# obtain a mongo connection
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# obtain a handle to the random database
db=client.mongoengine_test
collection=db.first_t_c

if len(sys.argv) < 2:
    sys.exit("You must supply number of secs you want to monitor the performance")
    
secs_to_run=int(sys.argv[1])
total_docs_now=collection.count()
total_documents_count = total_docs_now * 1000;
inserted_documents_count = 0
sleep_seconds = 1
sleep_count = 0
secs_to_script_write_1 = int(secs_to_run/cpu_count)
print (secs_to_script_write_1)
 
for i in range(cpu_count):
    secs_to_script_write_1_1 = str(secs_to_script_write_1)
    #print (secs_to_script_write_1_1)
    subprocess.Popen(['python', 'DB_Write_1.py',secs_to_script_write_1_1, str(i)])

 
#start = datetime.now();
 
#while (inserted_documents_count < total_documents_count) is True:
#    inserted_documents_count = collection.count()
#    if (sleep_count > 0 and sleep_count % 60 == 0):  
#        print 'Inserted ', inserted_documents_count, ' documents.'     
#    if (inserted_documents_count < total_documents_count):
#        sleep_count += 1
#        time.sleep(sleep_seconds)   
 
#print 'Inserting ', total_documents_count, ' took ', (datetime.now() - start).total_seconds(), 's'  
