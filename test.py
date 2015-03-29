import mraa
import time
import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()

print "running"

from firebase import firebase
firebase = firebase.FirebaseApplication('https://useyourworld.firebaseio.com', None)
result = firebase.get('/users', None)
print result

x = mraa.Gpio(13)
x.dir(mraa.DIR_OUT)

x.write(1)
time.sleep(1)
x.write(0)
