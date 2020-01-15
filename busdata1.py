from pykafka import KafkaClient
import json
from datetime import datetime
import uuid
import time

# KAFKA PRODUCER#####################################
'''
client = KafkaClient(hosts="localhost:9092")
topic = client.topics['busdata1']
producer=topic.get_sync_producer()

i=0
while True:
    message=("Hello" + str(i)).encode('ascii')
    producer.produce(message)
    print(message)
    i=i+1
'''
#####################################################
#Message Format Sending to Kafka
'''
data={
    'busline':'0001',
    'key':'0001_ajhdkajkdasjkgdh123',
    'timestamp':'20200111 07:35',
    'latitude':'52.52'
    'longitude':'46.46'
}
'''
#####################################################


open_file=open('./data/bus1.json')
json_data=json.load(open_file)
cordinates=json_data['features'][0]['geometry']['coordinates'] 

# print(cordinates)
def generate_uuid():
    return uuid.uuid4()

client = KafkaClient(hosts="localhost:9092")
topic = client.topics['busdata1']
producer=topic.get_sync_producer()


#Draft Message
data={}
data['busline']='0001'
def generate_checkpoint(cordinates):
    i=0
    while i<=len(cordinates):
        data['key']=data['busline'] + "_" + str(generate_uuid())
        data['timestamp']=str(datetime.utcnow())
        data['latitude']=cordinates[i][1]
        data['longitude']=cordinates[i][0]
        message=json.dumps(data)
        print(message)
        producer.produce(message.encode('ascii')) 
        time.sleep(1)
        # i=i+1
        
        if i==len(cordinates)-1:
            i=0
        else:
            i=i+1


generate_checkpoint(cordinates)

print(data)

