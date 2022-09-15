import os
import machine, Pin
from sdcard import SDCard

class exec_sensors():
    def __init__(self, sensor):
        self.sensor = sensor

    def sdcard(self, folder_name: 'sd'):
        #1. connect the SD module GND pin to ESP8266 GND pin.
        #2. connect the SD module VCC pin to ESP8266 VIN pin.
        #3. connect the SD module MOSO pin to ESP8266 D6 / GPIO 12.
        #4. connect the SD module MOSI pin to ESP8266 D7 / GPIO 13.
        #5. connect the SD module SCK pin to ESP8266 D5 / GPIO 14.
        #6. connect the SD module CS pin to ESP8266 D8 / GPIO 15.
        
            try:
                sd = SDCard(machine.SPI(1), machine.Pin(15))
                os.mount(sd, '/' + folder_name)
                print('check {} {} in'.format(os.listdir('/' + folder_name), folder_name))
                os.chdir(folder_name)
                print('The work directory was moved to {}'.format(folder_name))
                print('SD Card contains:{}'.format(os.listdir()))
            
            except:
                print('SDCard pins can be wrong, check SDCard class output problems')

        
