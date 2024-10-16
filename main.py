import network
import espnow
from time import sleep
from machine import UART
uart = UART(0, baudrate=115200, bits=8, parity=None, stop=1)

def espnow_rx():

    # A WLAN interface must be active to send()/recv()
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.disconnect()                # Disconnect from last connected WiFi SSID

    e = espnow.ESPNow()                  # Enable ESP-NOW
    e.active(True)

    while True:
        host, msg = e.recv()
        if msg:                          # wait for message
             uart.write(msg.decode('utf-8')+'\n')

if __name__ == "__main__":
    espnow_rx()
    
