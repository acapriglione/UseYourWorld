import mraa
import time
import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()

ledPin = mraa.Gpio(13)
ledPin.dir(mraa.DIR_OUT)
servoPin = mraa.Gpio(7)
servoPin.dir(mraa.DIR_OUT)
Pin2 = mraa.Gpio(12)
Pin2.dir(mraa.DIR_OUT)
Pin3 = mraa.Gpio(8)
Pin3.dir(mraa.DIR_OUT)

from firebase import firebase
firebase = firebase.FirebaseApplication('http://useyourworld.firebaseio.com', None)

print("Entering Loop")
while(True):
    state = firebase.get('/users', None)
    print(state)
    if(state['Bedroom']['OverheadLights'] == 'on'):
        ledPin.write(1)
    else:
        ledPin.write(0)
    if(state['Bedroom']['Door'] == 'open'):
        servoPin.write(1)
    else:
        servoPin.write(0)
    if(state['Bedroom']['Locked'] == 'true'):
        Pin2.write(1)
    else:
        Pin2.write(0)
    if(state['Bedroom']['Window'] == 'open'):
        Pin3.write(1)
    else:
        Pin3.write(0)
    time.sleep(1)
