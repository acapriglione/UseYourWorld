import requests.packages.urllib3.contrib.pyopenssl
requests.packages.urllib3.contrib.pyopenssl.inject_into_urllib3()

from firebase import firebase
firebase = firebase.FirebaseApplication('https://glaring-torch-6986.firebaseio.com', None)
new_user = {'name' : 'BlackBeard', 'title' : 'pirate'}

result = firebase.put('/users', 'servo', new_user)
print(result)


