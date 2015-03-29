import time
from firebase import firebase
firebase = firebase.FirebaseApplication('https://useyourworld.firebaseio.com', None)

i = False
while(i == False):
    try:
        input_file = open("pleasework.txt", 'r')
        for line in input_file:
            print(line)
        input_file.close()
        if(line == 'waveOut'):
            result = firebase.put('/users/Bedroom', 'Door', 'open')
        elif(line == 'waveIn'):
            result = firebase.put('/users/Bedroom', 'Door', 'closed')
        elif(line == 'fingersSpread'):
            result = firebase.put('/users/Bedroom', 'OverheadLights', 'on')
        elif(line == 'fist'):
            result = firebase.put('/users/Bedroom', 'OverheadLights', 'off')
        time.sleep(0.5)
    except:
        print("Failed")
        
