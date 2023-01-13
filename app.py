import psutil
import pymongo

client = pymongo.MongoClient('mongo:27017')
db = client.monitor

while True:
    cpu_percent = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')

    data = {
        'cpu_percent': cpu_percent,
        'virtual_memory': virtual_memory.percent,
        'disk_usage': disk_usage.percent
    }

    db.metrics.insert_one(data)
