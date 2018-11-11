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
import csv
from datetime import timezone, datetime

 
if len(sys.argv) < 2:
    sys.exit("You must supply number of secs you want to monitor the performance")
elif len(sys.argv) > 2:
    job_id = sys.argv[2]  
    
# obtain a mongo connection
from pymongo import MongoClient
client = MongoClient('localhost', 27017)

# obtain a handle to the random database
db=client.mongoengine_test
collection=db.first_t_c
 
documents_number = collection.count() * 200000
batch_number = 5 * 1000;
job_id = '1'
j=0
itr=0
MAX_ITR=int(sys.argv[1])
total_docs=0
job_name = 'Job#' + job_id
pid=os.getpid()

#random data generation
def random_generator(size=6, chars=string.ascii_uppercase):
    return ''.join(random.choice(chars) for x in range(size))

def random_hexgenerator():
    hexN="0x"+uuid.uuid4().hex
    return hexN[:18]
def timestamp_gen():
    ts=int(datetime.now(tz=timezone.utc).timestamp() * 1000)
    return ts

#orig_stdout = sys.stdout
f = open('/media/sf_DB_Readings/Readings_pers_%s.csv' % pid, 'w+')
#sys.stdout=f
 

batch_documents = [i for i in range(batch_number)];

startf = datetime.now();
while itr<MAX_ITR: 
    start = datetime.now();
    for index in range(documents_number):
        try:
            ts = timestamp_gen()
            value = random.random()
            syscall_nr=random.randint(1,101)
            syscall_name=random_generator(6,"abcdefghijklmnopqrstuvwxyz")
            dtb=random_hexgenerator()
            rsp=random_hexgenerator()
            rip=random_hexgenerator()
            pid=random.randint(1,10000)
            vmid="vm"+random_generator(2,'1234')
            logtype=random_generator(3,'xyz')
            document = {
                'value' : value,
                'syscall_nr':syscall_nr,
                'syscall_name':syscall_name,
                'dtb':dtb,
                'rsp':rsp,
                'rip':rip,
                'pid':pid,
                'vmid':vmid,
                'logtype':logtype,
                'ts':ts 
                }
            #creating array/batch of documents to insert 
            batch_documents[index % batch_number] = document
            
            if (index + 1) % batch_number == 0:
                collection.insert(batch_documents)
                index += 1;
            
            #calculate the time for the insert
            timec=int((datetime.now() - start).total_seconds())
            
            #if index % 4000 == 0: 
               # print (' inserted ', index, ' documents.')

            if timec==1:
                #print (timec, 'secs for',index)
                j=j+1
                f.write("%d,%d\n" %(j, index))
                itr=itr+1
                total_docs=total_docs + index
                break
                   
        except:
            print ('Unexpected error:', sys.exc_info()[0], ', for index ', index)
            raise
#sys.stdout = orig_stdout
print (job_name, ' inserted ',total_docs, ' in ', (datetime.now() - startf).total_seconds(), 's')
f.close()
