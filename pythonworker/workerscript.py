from datetime import datetime
import random
import time
import psutil

import os

from influxdb_client import InfluxDBClient, BucketRetentionRules, Point, WritePrecision
from influxdb_client.rest import ApiException
from influxdb_client.client.write_api import SYNCHRONOUS

#get env from system
token = os.getenv("DOCKER_INFLUXDB_INIT_ADMIN_TOKEN")
org = os.getenv("DOCKER_INFLUXDB_INIT_ORG")
bucket = os.getenv("DOCKER_INFLUXDB_BUCKET_Python")

#wait until influxdb is up.
time.sleep(5)

#setup db connection.
with InfluxDBClient(url="http://influxdb:8086", token=token, org=org) as client:

   buckets_api = client.buckets_api()

#create new bucket for Python data"
   try:
      created_bucket = buckets_api.create_bucket(bucket_name=bucket, org=org)

#exeption handling if the Bucket already exists.    
   except ApiException as e:
      print(f'Exception body type: {type(e.body)}')
      if  'bucket with name python already exists' not in e.body:
         raise e

      print('bucket with name already exists')
      pass
      
#get and write data into influxdb.
   while True:
        write_api = client.write_api(write_options=SYNCHRONOUS)
        svmem = psutil.virtual_memory()
        usedcpu = str(svmem.percent)
        data = "mem,host=host1 used_percent="+ usedcpu
        write_api.write(bucket, org, data)
        time.sleep(10)



