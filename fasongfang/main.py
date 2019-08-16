
from simple import MQTTClient 
from machine import Pin 
import dht 
import network 
import time 
from machine import ADC
#import micropython-random 

 
 
#led = Pin(2,Pin.OUT,value=0)  
SERVER = "192.168.1.109" 
CLIENT_ID = "0TO17SZU94547OGY" 
TOPIC = "data" 

def run():     
  while True:         
    
     
    
    gpin_dht = Pin(2)
    d = dht.DHT11(gpin_dht)
    d.measure()
   
    
    temperture = d.temperature() 
    
    hum = d.temperature() 
    print(str(temperture))
    #temperture =100
        
    #temperature = random.randrange(150)
    
    print('Temperature: ' + str(temperture) + ' Celsius')
    #up_temp1 ="{\"sensorDatas\":[{\"sensorsId\":200314505,\"value\":"+str(temperature)+"}]}"
    up_temp1="{ \"value\":"+str(temperture) +" ,"+ "\"id\":"+str(hum)+" }"
    c.publish(TOPIC,up_temp1,retain=True)         
    print(up_temp1)
             
    time.sleep(3)
    
server=SERVER 
c = MQTTClient(CLIENT_ID,server) 
c.connect() 
print("Before MQTT publish") 
run() 
print("MQTT published...............")
    


