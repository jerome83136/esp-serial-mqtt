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
broker="1.2.3.4" #broker IP address or DNS name
port=1883 #broker port number
client_id= "espnowhub" #Client ID of this device when connectint to MQTT broker
topic= "espnowtest" #MQTT topic where all messages will be sent by this device
client1= paho.Client(client_id)

#program
#endless loop to read the output of the serial connection with the ESP device
while True:
 if (ser.inWaiting() > 0): # detect new data on serial output
  serial_data = ser.readlines() # read all lines and store them in "serial_data" variable
  for line in serial_data: # for each line; do bellow actions
   device = (json.loads(line.decode('utf-8').rstrip().strip())['device']) # extract the device name from serial data
   #debug mode
   if args == "debug":
    print(line.decode('utf-8').rstrip().strip())
   client1.connect(broker,port, 10)
   client1.publish(topic+'/'+device,line,retain=True)
 client1.disconnect()
 sleep(1)
