import serial
from time import sleep
import paho.mqtt.client as paho
import sys
import json

#get args
args = ""
if len(sys.argv) > 1:
 args= sys.argv[1]
 print (args)

#serial config
ser = serial.Serial('/dev/ttyUSB3', baudrate = 115200, timeout = 5)
print(ser.name) 

#mqtt
broker="mqtt.maison.lan"
port=1883
client_id= "espnowhub"
topic= "espnowtest"
#client1= paho.Client(paho.CallbackAPIVersion.VERSION1, client_id)
client1= paho.Client(client_id)

#program
while True:
 if (ser.inWaiting() > 0):
  #serial_data = ser.readlines().decode('utf-8').rstrip().strip()
  serial_data = ser.readlines()
  for line in serial_data:
   device = (json.loads(line.decode('utf-8').rstrip().strip())['device'])
   #debug mode
   if args == "debug":
    print(line.decode('utf-8').rstrip().strip())
   client1.connect(broker,port, 10)
   client1.publish(topic+'/'+device,line,retain=True)
 client1.disconnect()
 sleep(1)
