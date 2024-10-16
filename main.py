import network
import espnow
from time import sleep
from machine import UART
#uart = UART(0, 115200) # 1st argument: UART number: Hardware UART #1
uart = UART(0, baudrate=115200, bits=8, parity=None, stop=1)

#while True:
# uart.write('keepalive\n')
# sleep(1)

def espnow_rx():

    # A WLAN interface must be active to send()/recv()
    sta = network.WLAN(network.STA_IF)
    sta.active(True)
    sta.disconnect()                # Disconnect from last connected WiFi SSID

    e = espnow.ESPNow()                  # Enable ESP-NOW
    e.active(True)

    #peer = b'p\x04\x1d3T\x88'   # MAC address of peer's wifi interface
    #e.add_peer(peer)                     # Sender's MAC registration

    while True:
        host, msg = e.recv()
#        uart.write('keepalive\n')
        if msg:                          # wait for message
             uart.write(msg.decode('utf-8')+'\n')
#            print(msg.decode('utf-8'))

if __name__ == "__main__":
    espnow_rx()
    
