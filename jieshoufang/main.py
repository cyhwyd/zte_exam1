
from simple import MQTTClient
from machine import Pin
import network
import time
import ujson


SERVER = "192.168.1.109"
CLIENT_ID = "umqtt_clientDwwyydd"
TOPIC = "#"
c=None

def sub_cb(topic, msg):
    global state
    print((topic, msg))
    print(msg.decode())
    obj=ujson.loads(msg.decode())
    print(obj)
    value1=obj['value'] 
    sensorsId1=obj['id'] 
    print("温度传感器:"+str(sensorsId1)+"值为:"+str(value1)+"摄氏度")  
    
    

#Catch exceptions,stop program if interrupted accidentally in the 'try'
def a():
  server=SERVER
  c = MQTTClient(CLIENT_ID, server)     #create a mqtt client
  c.set_callback(sub_cb) #set callback
  c.connect()                               #connect mqtt
  c.subscribe(TOPIC)                        #client subscribes to a topic
  print("Connected to %s, subscribed to %s topic" % (server, TOPIC))
  while True:
    c.check_msg()                            #wait message 
    time.sleep(10)

a()
