import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()

print "running"

from firebase import firebase
firebase = firebase.FirebaseApplication('https://glaring-torch-6986.firebaseio.com', None)
result = firebase.get('/users', None)
print result
{'1': 'John Doe'}
